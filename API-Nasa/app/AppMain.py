from tkinter import *

from api_data.about_api import about_api, about_neows, about_donki
from api_data.donki_data import donki_dict
from api_data.neows_data import neows_names
from app.app_configurations import color


class AppMain:

    def __init__(self):

        self.menu_selected = None
        self.entry_field = dict()
        self.all_buttons = dict()

        self.__root = Tk()

        img_logo = PhotoImage(file=r'..\assets\logo.png')

        self.__root.title("AppMain")
        self.__root.geometry("+300+150")
        self.__root.resizable(False, False)
        self.__root.config(bg=color['VT'])

        self.menu = Menu(self.__root, bd=10)
        self.__root.config(menu=self.menu)

        self.menu.add_command(label='NEOWS', command=self.show_neows)
        self.menu.add_command(label='DONKI', command=self.show_donkis)

        self.__f_head = Frame(self.__root, bg=color['VT'])

        label_head = Label(self.__f_head, font=("Arial", 10, "bold"), bg=color['VT'], fg=color['WT'])
        label_head.config(text="**{NASA}: Open Innovation Team **   ")
        label_head.pack(side=LEFT)

        label_logo = Label(self.__f_head, image=img_logo)
        label_logo.pack(side=LEFT)

        self.__f_head.pack(side=TOP)

        self.__f_body = Frame(self.__root, bg=color['VT'])

        f_left = Frame(self.__f_body)

        self.box_left = Listbox(f_left, bg=color['GR'], fg=color['WT'], bd=10, width=35)
        self.box_left.pack(side=LEFT, fill=Y)

        frame_buttons = Frame(f_left)
        cont = 0
        while cont < 8:
            if cont == 2:
                self.all_buttons[f'{cont}'] = Button(frame_buttons, width=8, command=self.select_item, text="Select")
                self.all_buttons[f'{cont}'].grid(row=cont, column=0)
            else:
                self.all_buttons[f'{cont}'] = Button(frame_buttons, state=DISABLED, width=8)
                self.all_buttons[f'{cont}'].grid(row=cont, column=0)
            cont += 1
        frame_buttons.pack(side=LEFT)

        f_left.grid(row=1, column=1)

        f_right = Frame(self.__f_body)

        frame_entries = Frame(f_right)
        cont = 0
        while cont < 8:
            self.entry_field[f'{cont}'] = Entry(frame_entries, width=8, font=("Consolas", 14, "bold"))
            self.entry_field[f'{cont}'].config(state=DISABLED)
            self.entry_field[f'{cont}'].grid(row=cont, column=0)
            cont += 1
        frame_entries.pack(side=LEFT)

        self.box_right = Listbox(f_right, bg=color['GR'], fg=color['BK'], bd=10, width=35)
        self.box_right.pack(side=LEFT, fill=Y)

        f_right.grid(row=1, column=2)

        f_under = Frame(self.__f_body)
        self.txt_under = Text(f_under, bg=color['BK'], fg=color['WT'], bd=10)
        self.txt_under.pack()
        f_under.grid(row=2, column=1, columnspan=2)

        self.__f_body.pack(side=TOP)

        self.__f_foot = Frame(self.__root, bg=color['VT'])

        label_foot = Label(self.__f_foot, font=("Arial", 7, "bold"), bg=color['VT'], fg=color['WT'])
        label_foot.config(text="Office of the Chief Information Officer: 'nasa-data@lists.arc.nasa.gov'")
        label_foot.pack()

        self.__f_foot.pack(side=BOTTOM)

        self.initial_msn()

        self.__root.mainloop()

    def initial_msn(self):
        self.txt_under.delete(1.0, END)
        self.txt_under.insert(END, about_api)

    def select_item(self):
        self.txt_under.delete(1.0, END)
        self.box_right.delete(0, END)

        item_selected = self.box_left.get(ANCHOR)

        try:
            self.txt_under.insert(END, f'--{self.menu_selected.title()}:  [  {item_selected}  ]--\n\n\n\n')
        except AttributeError:
            self.txt_under.insert(END, '[Error]--\n\n\n\n')

        if self.menu_selected == 'neows':
            neo_ws = neows_names.get(item_selected)

            try:
                basic_data = neo_ws.basic_data()
                avd_data = neo_ws.advanced_data()
                tch_data = neo_ws.technical_data()

            except AttributeError:
                self.txt_under.insert(END, f'Error: Try again')

            else:
                self.box_right.insert(END, '     **(Basic Information)**')
                for i in basic_data:
                    basic_str = f'{i}: {basic_data[i]}'
                    self.box_right.insert(END, basic_str)

                self.box_right.insert(END, '     **(Technical information)**')
                for i in tch_data:
                    tch_str = f'{i}: {tch_data[i]}'
                    self.box_right.insert(END, tch_str)

                self.txt_under.insert(END, '     **(Advanced Information)**\n\n')
                for i in avd_data:
                    avd_str = f'--- {i}:\n\n{avd_data[i]}\n\n\n'
                    self.txt_under.insert(END, avd_str)

        elif self.menu_selected == 'donki':
            donki = donki_dict.get(item_selected)

            try:
                about_parameter = donki[1]()
            except TypeError:
                self.txt_under.insert(END, f'Error: Try again')
            else:
                parameters_rules = about_parameter['parameters'][0]
                parameters_amount = about_parameter['parameters'][1]

                for i in parameters_rules:
                    pmt_str = f'{i}\n'
                    self.txt_under.insert(END, pmt_str)

                for i in self.entry_field:
                    if int(i) < (int(parameters_amount)):
                        self.entry_field[i].config(state=NORMAL)
                    else:
                        self.entry_field[i].config(state=DISABLED)
        else:
            self.txt_under.insert(END, 'Blank')

    def show_neows(self):
        self.menu_selected = 'neows'

        self.box_left.delete(0, END)
        for i in neows_names:
            self.box_left.insert(END, i)

        self.txt_under.delete(1.0, END)
        self.txt_under.insert(END, about_neows)

    def show_donkis(self):
        self.menu_selected = 'donki'

        self.box_left.delete(0, END)
        for i in donki_dict:
            self.box_left.insert(END, i)

        self.txt_under.delete(1.0, END)
        self.txt_under.insert(END, about_donki)


AppMain()
