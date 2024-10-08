import webbrowser
from tkinter import *

import webview

from access.actions_donki import get_donki
from access.actions_neows import update_and_save_neows_data
from api_data.about_api import about_api, about_neows, about_donki
from api_data.donki_data import donki_names
from api_data.neows_data import neows_names

from app.app_config import color


def _open_link(type_link, local_to_open='inside'):
    if local_to_open == 'inside':
        webview.create_window(f'{type_link}', type_link)
        webview.start()
    elif local_to_open == 'outside':
        webbrowser.open(type_link)


class AppMain:

    def __init__(self):
        self.donki = None
        self.neo_ws = None

        self.activate_entries = False

        self.menu_selected = None
        self.item_selected = None

        self.entry_field = dict()
        self.all_buttons = dict()

        self.current_local = list()
        self._path = ['../', ('neows', 'donki'), 'item']
        self.current_local.append(self._path[0])

        self.__root = Tk()

        self.__root.title("AppMain")
        self.__root.geometry("+300+100")
        self.__root.resizable(True, True)
        self.__root.config(bg=color['VT'])

        _menu = Menu(self.__root, bd=10)

        menu_browse = Menu(_menu, tearoff=0)
        menu_browse.add_command(label='NEOWS', command=self.show_menu_neows)
        menu_browse.add_command(label='DONKI', command=self.show_menu_donki)
        _menu.add_cascade(label='Browse_APIs', menu=menu_browse)

        menu_options = Menu(_menu, tearoff=0)
        menu_options.add_command(label='Initial setting', command=self.initial_settings)
        menu_options.add_command(label='NeoWs update data', command=self.update_neows)
        _menu.add_cascade(label='Options', menu=menu_options)

        self.__root.config(menu=_menu)

        __f_head = Frame(self.__root, bg=color['VT'])

        label_head = Label(__f_head, font=("Arial", 10, "bold"), bg=color['VT'], fg=color['WT'])
        label_head.config(text="**{NASA}: Open Innovation Team **   ")
        label_head.pack(side=LEFT)

        try:
            img_logo = PhotoImage(file=r'assets\logo.png')
        except FileNotFoundError:
            try:
                img_logo = PhotoImage(file=r'..\assets\logo.png')
            except FileNotFoundError:
                label_logo = Label(__f_head, text='img\n[XXX]')
                label_logo.pack(side=LEFT)
            else:
                label_logo = Label(__f_head, image=img_logo)
                label_logo.pack(side=LEFT)
        else:
            label_logo = Label(__f_head, image=img_logo)
            label_logo.pack(side=LEFT)

        __f_head.pack(side=TOP)

        __f_body = Frame(self.__root, bg=color['VT'])

        f_left = Frame(__f_body)

        self.select_button = Button(f_left, text=">>   Select ", width=8, bd=8, bg=color['GR_drk'])
        self.select_button.config(command=self.select_item)
        self.select_button.pack(fill=X)

        list_l_block = Frame(f_left)
        self.listbox_left = Listbox(list_l_block, bg=color['GR_drk'], fg=color['WT'], bd=10, width=45, height=11)
        self.listbox_left.grid(row=0, column=0)

        x_list_left = Scrollbar(list_l_block, orient=HORIZONTAL, command=self.listbox_left.xview)
        x_list_left.grid(row=1, column=0, sticky=W + E)
        self.listbox_left.config(xscrollcommand=x_list_left.set)
        list_l_block.pack(side=LEFT, fill=BOTH)

        buttons_block = Frame(f_left)
        cont = 0
        while cont < 8:
            self.all_buttons[f'{cont}'] = Button(buttons_block, text='---', state=DISABLED, width=22, bd=2)
            self.all_buttons[f'{cont}'].grid(row=cont, column=0)
            cont += 1
        buttons_block.pack(side=LEFT)

        f_left.grid(row=1, column=1)

        f_right = Frame(__f_body)

        self.return_button = Button(f_right, text=" Return   <<", width=8, bd=8, bg=color['GR_drk'])
        self.return_button.config(command=self.do_return, state=NORMAL)
        self.return_button.pack(fill=X)

        entries_block = Frame(f_right)
        cont = 0
        while cont < 8:
            self.entry_field[f'{cont}'] = Entry(entries_block, width=14, font=("Consolas", 14, "bold"), bg=color['BG'])
            self.entry_field[f'{cont}'].config(state=DISABLED, disabledbackground=color['GR'])
            self.entry_field[f'{cont}'].grid(row=cont, column=0)
            cont += 1
        entries_block.pack(side=LEFT)

        list_r_block = Frame(f_right)
        self.listbox_right = Listbox(list_r_block, bg=color['GR_drk'], fg=color['BK'], bd=10, width=45, height=11)
        self.listbox_right.grid(row=0, column=0)

        x_list_right = Scrollbar(list_r_block, orient=HORIZONTAL, command=self.listbox_right.xview)
        x_list_right.grid(row=1, column=0, sticky=W + E)
        self.listbox_right.config(xscrollcommand=x_list_right.set)
        list_r_block.pack(side=LEFT, fill=BOTH)

        f_right.grid(row=1, column=2)

        f_under = Frame(__f_body)

        txt_block = Frame(f_under)
        self.txt_under = Text(txt_block, bg=color['BK'], fg=color['WT'], bd=20, width=110)
        self.txt_under.grid(row=0, column=0)

        x_txt_under = Scrollbar(txt_block, orient=HORIZONTAL, command=self.txt_under.xview)
        x_txt_under.grid(row=1, column=0, sticky=W + E)
        self.txt_under.config(xscrollcommand=x_txt_under.set)

        y_txt_under = Scrollbar(txt_block, orient=VERTICAL, command=self.txt_under.yview)
        y_txt_under.grid(row=0, column=1, sticky=N + S)
        self.txt_under.config(yscrollcommand=y_txt_under.set)
        txt_block.pack(fill=X)

        f_under.grid(row=2, column=1, columnspan=2)

        __f_body.pack(side=TOP)

        __f_foot = Frame(self.__root, bg=color['VT'])

        label_foot = Label(__f_foot, font=("Arial", 7, "bold"), bg=color['VT'], fg=color['WT'])
        label_foot.config(text="Office of the Chief Information Officer: 'nasa-data@lists.arc.nasa.gov'")
        label_foot.pack()

        __f_foot.pack(side=BOTTOM)

        self.initial_settings()

        self.__root.mainloop()

    def initial_settings(self):
        self.menu_selected = None

        self.current_local = self._path[0]

        for i in self.all_buttons:
            self.all_buttons[i].config(state=DISABLED, text='---')

        if self.activate_entries:
            self.activate_entries = False
            for i in self.entry_field:
                self.entry_field[i].config(state=NORMAL)
                self.entry_field[i].delete(0, END)
                self.entry_field[i].config(state=DISABLED)

        self._initial_msg()
        self._initial_list()

    def _initial_msg(self):
        self.txt_under.delete(1.0, END)
        self.txt_under.insert(END, about_api)

    def _initial_list(self):
        self.listbox_left.delete(0, END)
        self.listbox_right.delete(0, END)

    def update_neows(self):
        update_and_save_neows_data()
        self.__root.destroy()
        AppMain()

    def show_menu_neows(self):
        self.initial_settings()

        self.menu_selected = 'neows'
        self.current_local = self._path[1][0]

        self.listbox_left.delete(0, END)
        for i in neows_names:
            self.listbox_left.insert(END, i)

        self.txt_under.delete(1.0, END)
        self.txt_under.insert(END, about_neows)

    def show_menu_donki(self):
        self.initial_settings()

        self.menu_selected = 'donki'
        self.current_local = self._path[1][1]

        self.listbox_left.delete(0, END)
        for i in donki_names:
            self.listbox_left.insert(END, i)

        self.txt_under.delete(1.0, END)
        self.txt_under.insert(END, about_donki)

    def do_return(self):
        if self.current_local == self._path[1][0] or self.current_local == self._path[1][1]:
            self.initial_settings()
            print("return1")

        elif (self.current_local == (self._path[1][0], self._path[2]) or
              self.current_local == (self._path[1][1], self._path[2])):

            self.activate_entries = False

            for i in self.entry_field:
                self.entry_field[i].config(state=NORMAL)
                self.entry_field[i].delete(0, END)
                self.entry_field[i].config(state=DISABLED)

            if self.current_local[0] == self._path[1][0]:
                self.show_menu_neows()
                print('return2')

            elif self.current_local[0] == self._path[1][1]:
                self.show_menu_donki()
                print('return3')

        else:
            pass

    def select_item(self):
        self.txt_under.delete(1.0, END)
        self.listbox_right.delete(0, END)

        self.item_selected = self.listbox_left.get(ANCHOR)

        try:
            title_string = f'--{self.menu_selected.title()}:  [  {self.item_selected.title()}  ]--\n\n\n\n'
            self.txt_under.insert(END, title_string)
        except AttributeError:
            self.txt_under.insert(END, f'[Error]:--\n\n\n\n')
        else:
            if self.menu_selected == 'neows':

                try:
                    self.neo_ws = neows_names[self.item_selected]
                except KeyError:
                    self.txt_under.insert(END, f'Error: Try again')
                else:
                    self.current_local = self._path[1][0], self._path[2]

                    self.listbox_left.delete(0, END)
                    self.listbox_left.insert(END, self.item_selected)

                    basic_data = self.neo_ws.basic_data()

                    self.listbox_right.insert(END, f'{" " * 8}**(Basic Information)**')
                    self.listbox_right.insert(END, *basic_data)

                    tch_data = self.neo_ws.technical_data()

                    self.listbox_right.insert(END, f'{" " * 8}**(Technical information)**')
                    self.listbox_right.insert(END, *tch_data)

                    links_data = self.neo_ws.links_data()

                    self.listbox_right.insert(END, f'{" " * 8}**(links)**')
                    self.listbox_right.insert(END, *links_data)

                    avd_data = self.neo_ws.advanced_data()

                    self.txt_under.insert(END, f'{" " * 8}**(Advanced):**\n\n')
                    for i in avd_data:
                        avd_str = f'--- {i}:\n\n{avd_data[i]}\n\n\n'
                        self.txt_under.insert(END, avd_str)

                    self.all_buttons[f'{0}'].config(state=NORMAL, text="Estimated diameter",
                                                    command=lambda: self._neo_ws_advanced('estimated_diameter'))
                    self.all_buttons[f'{1}'].config(state=NORMAL, text="Close approach data",
                                                    command=lambda: self._neo_ws_advanced('close_approach_data'))
                    self.all_buttons[f'{2}'].config(state=NORMAL, text="Orbital data",
                                                    command=lambda: self._neo_ws_advanced('orbital_data'))

                    self.all_buttons[f'{6}'].config(state=NORMAL, text="Link source",
                                                    command=lambda: _open_link(self.neo_ws['links']['self']))
                    self.all_buttons[f'{7}'].config(state=NORMAL, text="Jet Propulsion Laboratory",
                                                    command=lambda: _open_link(self.neo_ws['nasa_jpl_url']))

            elif self.menu_selected == 'donki':

                self.donki = donki_names.get(self.item_selected)

                try:
                    about_parameter = self.donki[1]()
                except TypeError:
                    self.txt_under.insert(END, f'Error: Try again')
                else:
                    self.current_local = self._path[1][1], self._path[2]

                    self.listbox_left.delete(0, END)
                    self.listbox_left.insert(END, self.item_selected)

                    parameters_rules = about_parameter['parameters'][0]
                    self.listbox_right.insert(END, *parameters_rules)

                    parameters_amount = about_parameter['parameters'][1]
                    for i in self.entry_field:
                        if int(i) < int(parameters_amount):
                            self.entry_field[i].config(state=NORMAL, bd=1)
                        else:
                            self.entry_field[i].config(state=DISABLED)

                    parameters_names = about_parameter['parameters'][2]
                    for i in self.all_buttons:
                        if int(i) < int(parameters_amount):
                            self.all_buttons[f'{i}'].config(text=parameters_names[int(i)])
                        else:
                            self.all_buttons[f'{i}'].config(text='---')

                    self._processing_donki(parameters_names)

            else:
                self.txt_under.insert(END, 'Blank')

    def _neo_ws_advanced(self, data):

        self.txt_under.delete(2.0, END)

        advanced_title = data.replace("_", " ")
        self.txt_under.insert(END, f'\n\n\n     Advanced: {advanced_title.title()}    \n\n\n')

        adv_selected = self.neo_ws.advanced_data(data)
        for i in adv_selected:
            if data == 'orbital_data':
                if i != 'orbit_class':
                    self.txt_under.insert(END, f'> {i.replace("_", " ").title()}:  {adv_selected[i]}\n\n')
                elif i == 'orbit_class':
                    self.txt_under.insert(END, f'> {i.replace("_", " ").title()}:\n')
                    for j in adv_selected[i]:
                        self.txt_under.insert(END, f'   >> {j.replace("_", " ").title()}: {adv_selected[i][j]}\n')
            else:
                self.txt_under.insert(END, f'\n\n * [{i.title()}]:\n\n')
                for j in adv_selected[i]:
                    self.txt_under.insert(END, f'> {j.replace("_", " ").title()}: {adv_selected[i][j]}\n')

    def _processing_donki(self, parameters_names):

        donki_data = None

        try:
            if not self.activate_entries:
                parameters_default = {i: '' for i in parameters_names}
                data_type = self.donki[0](**parameters_default)

                donki_data = get_donki(data_type)

            elif self.activate_entries:
                parameters_captured = self._get_donki_parameters(parameters_names)
                data_type = self.donki[0](**parameters_captured)

                donki_data = get_donki(data_type)

        except Exception as ex:
            self.txt_under.insert(END, f'Error[processing]: {ex}')

        else:
            self.txt_under.insert(END, f'[Data type:{type(donki_data)} // Has:({len(donki_data)})items]\n\n\n\n')
            self.activate_entries = True

            cont = 0
            for i in donki_data:
                self.txt_under.insert(END, f'>> Item[{cont}]: {len(i)} elements  << : \n\n\n')
                for j in i:
                    self.txt_under.insert(END, f'**({j})** =  [  {i[j]}  ] ;\n\n')

                self.txt_under.insert(END, f'\n{"-" * 100}\n\n\n')
                cont += 1

    def _get_donki_parameters(self, parameters_names):

        parameters = dict()

        cont = 0
        while cont < len(parameters_names):
            for i in parameters_names:
                parameters[i] = self.entry_field[f'{cont}'].get()

                cont += 1

        return parameters
