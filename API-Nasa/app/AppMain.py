from tkinter import *

from api_data.about_api import about_api, about_neows, about_donki
from api_data.donki_data import donki_dict
from api_data.neows_data import neows_names

color = {'VT': "#160E3D", 'BK': "black", 'WT': "white", 'GR': "grey20"}


class AppMain:

    def __init__(self):

        self.menu_selected = None

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
        self.box_left.pack(side=LEFT)

        frame_button = Frame(f_left)
        cont = 1
        while cont < 7:
            if cont == 1:
                self.but_test_1 = Button(frame_button, width=8, command=self.select_item, text="Select")
                self.but_test_1.grid(row=cont, column=0)
            else:
                Button(frame_button, state=DISABLED, width=8).grid(row=cont, column=0)
            cont += 1
        frame_button.pack(side=LEFT)

        f_left.grid(row=1, column=1)

        f_right = Frame(self.__f_body)

        frame_button = Frame(f_right)
        cont = 1
        while cont < 7:
            if cont == 1:
                self.but_test_2 = Button(frame_button, width=8, command=self.test_but2, text="----")
                self.but_test_2.grid(row=cont, column=0)
            else:
                Button(frame_button, state=DISABLED, width=8).grid(row=cont, column=0)
            cont += 1
        frame_button.pack(side=LEFT)

        self.box_right = Listbox(f_right, bg=color['GR'], fg=color['BK'], bd=10, width=35)
        self.box_right.pack(side=LEFT)

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
                donki_parameter = donki[1]()
            except TypeError:
                self.txt_under.insert(END, f'Error: Try again')
            else:
                for i in donki_parameter[1]:
                    pmt_str = f'{i}\n'
                    self.txt_under.insert(END, pmt_str)

        else:
            self.txt_under.insert(END, 'Blank')

    def test_but2(self):
        self.txt_under.delete(1.0, END)
        self.txt_under.insert(END, "--- press")

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
