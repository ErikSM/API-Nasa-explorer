from tkinter import *

from api_data.about_api import about_api, about_neows, about_donki
from api_data.donki_data import donki_names
from api_data.neows_data import neows_names
from app.app_configurations import color


class AppMain:

    def __init__(self):

        self.menu_selected = None
        self.item_selected = None

        self.entry_field = dict()
        self.all_buttons = dict()

        self.__root = Tk()

        img_logo = PhotoImage(file=r'..\assets\logo.png')

        self.__root.title("AppMain")
        self.__root.geometry("+300+100")
        self.__root.resizable(False, False)
        self.__root.config(bg=color['VT'])

        _menu = Menu(self.__root, bd=10)
        self.__root.config(menu=_menu)

        _menu.add_command(label='NEOWS', command=self.show_menu_neows)
        _menu.add_command(label='DONKI', command=self.show_menu_donki)

        __f_head = Frame(self.__root, bg=color['VT'])

        label_head = Label(__f_head, font=("Arial", 10, "bold"), bg=color['VT'], fg=color['WT'])
        label_head.config(text="**{NASA}: Open Innovation Team **   ")
        label_head.pack(side=LEFT)

        label_logo = Label(__f_head, image=img_logo)
        label_logo.pack(side=LEFT)

        __f_head.pack(side=TOP)

        __f_body = Frame(self.__root, bg=color['VT'])

        f_left = Frame(__f_body)
        self.select_button = Button(f_left, text="Select", width=8, bd=8, bg=color['GR_drk'])
        self.select_button.config(command=self.select_item)
        self.select_button.pack(fill=X)

        self.listbox_left = Listbox(f_left, bg=color['GR_drk'], fg=color['WT'], bd=10, width=35)
        self.listbox_left.pack(side=LEFT, fill=Y)

        buttons_block = Frame(f_left)
        cont = 0
        while cont < 8:
            self.all_buttons[f'{cont}'] = Button(buttons_block, text='---', state=DISABLED, width=22, bd=2)
            self.all_buttons[f'{cont}'].grid(row=cont, column=0)
            cont += 1
        buttons_block.pack(side=LEFT)
        f_left.grid(row=1, column=1)

        f_right = Frame(__f_body)
        self.return_button = Button(f_right, text="return", width=8, bd=8, bg=color['GR_drk'])
        self.return_button.config(command=self.initial_settings)
        self.return_button.pack(fill=X)

        entries_block = Frame(f_right)
        cont = 0
        while cont < 8:
            self.entry_field[f'{cont}'] = Entry(entries_block, width=14, font=("Consolas", 14, "bold"), bg=color['BG'])
            self.entry_field[f'{cont}'].config(state=DISABLED, disabledbackground=color['GR'])
            self.entry_field[f'{cont}'].grid(row=cont, column=0)
            cont += 1
        entries_block.pack(side=LEFT)

        self.listbox_right = Listbox(f_right, bg=color['GR_drk'], fg=color['BK'], bd=10, width=35)
        self.listbox_right.pack(side=LEFT, fill=Y)
        f_right.grid(row=1, column=2)

        f_under = Frame(__f_body)
        self.txt_under = Text(f_under, bg=color['BK'], fg=color['WT'], bd=20)
        self.txt_under.pack()
        f_under.grid(row=2, column=1, columnspan=2)

        __f_body.pack(side=TOP)

        __f_foot = Frame(self.__root, bg=color['VT'])

        label_foot = Label(__f_foot, font=("Arial", 7, "bold"), bg=color['VT'], fg=color['WT'])
        label_foot.config(text="Office of the Chief Information Officer: 'nasa-data@lists.arc.nasa.gov'")
        label_foot.pack()

        __f_foot.pack(side=BOTTOM)

        self.initial_settings()

        self.__root.mainloop()

    def _initial_msg(self):
        self.txt_under.delete(1.0, END)
        self.txt_under.insert(END, about_api)

    def _initial_list(self):
        self.listbox_left.delete(0, END)
        self.listbox_right.delete(0, END)

    def initial_settings(self):
        self.menu_selected = None

        for i in self.all_buttons:
            self.all_buttons[i].config(text='---')
        for i in self.entry_field:
            self.entry_field[i].config(state=DISABLED)

        self._initial_msg()
        self._initial_list()

    def show_menu_neows(self):
        self.initial_settings()
        self.menu_selected = 'neows'

        self.listbox_left.delete(0, END)
        for i in neows_names:
            self.listbox_left.insert(END, i)

        self.txt_under.delete(1.0, END)
        self.txt_under.insert(END, about_neows)

    def show_menu_donki(self):
        self.initial_settings()
        self.menu_selected = 'donki'

        self.listbox_left.delete(0, END)
        for i in donki_names:
            self.listbox_left.insert(END, i)

        self.txt_under.delete(1.0, END)
        self.txt_under.insert(END, about_donki)

    def select_item(self):
        self.txt_under.delete(1.0, END)
        self.listbox_right.delete(0, END)

        self.item_selected = self.listbox_left.get(ANCHOR)

        try:
            self.txt_under.insert(END, f'--{self.menu_selected.title()}:  [  {self.item_selected.title()}  ]--\n\n\n\n')
        except AttributeError:
            self.txt_under.insert(END, '[Error]--\n\n\n\n')

        if self.menu_selected == 'neows':
            neo_ws = neows_names.get(self.item_selected)

            try:
                basic_data = neo_ws.basic_data()
                avd_data = neo_ws.advanced_data()
                tch_data = neo_ws.technical_data()

            except AttributeError:
                self.txt_under.insert(END, f'Error: Try again')

            else:
                self.listbox_right.insert(END, '     **(Basic Information)**')
                for i in basic_data:
                    basic_str = f'{i}: {basic_data[i]}'
                    self.listbox_right.insert(END, basic_str)

                self.listbox_right.insert(END, '     **(Technical information)**')
                for i in tch_data:
                    tch_str = f'{i}: {tch_data[i]}'
                    self.listbox_right.insert(END, tch_str)

                self.txt_under.insert(END, '     **(Advanced Information)**\n\n')
                for i in avd_data:
                    avd_str = f'--- {i}:\n\n{avd_data[i]}\n\n\n'
                    self.txt_under.insert(END, avd_str)

                self.all_buttons[f'{1}'].config(state=NORMAL, text="More Information")

        elif self.menu_selected == 'donki':
            donki = donki_names.get(self.item_selected)

            try:
                about_parameter = donki[1]()
            except TypeError:
                self.txt_under.insert(END, f'Error: Try again')
            else:
                parameters_rules = about_parameter['parameters'][0]
                parameters_amount = about_parameter['parameters'][1]
                parameters_names = about_parameter['parameters'][2]

                for i in parameters_rules:
                    pmt_str = f'{i}\n'
                    self.txt_under.insert(END, pmt_str)

                for i in self.entry_field:
                    if int(i) < int(parameters_amount):
                        self.entry_field[i].config(state=NORMAL, bd=1)
                    else:
                        self.entry_field[i].config(state=DISABLED)

                for i in self.all_buttons:
                    if int(i) < int(parameters_amount):
                        self.all_buttons[f'{i}'].config(text=parameters_names[int(i)])
                    else:
                        self.all_buttons[f'{i}'].config(text='---')
        else:
            self.txt_under.insert(END, 'Blank')



AppMain()
