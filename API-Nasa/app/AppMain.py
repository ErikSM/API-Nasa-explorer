from tkinter import *


color = {'VT': "#160E3D", 'BK': "black", 'WT': "white"}


class AppMain:

    def __init__(self):

        self.__root = Tk()

        img_logo = PhotoImage(file=r'..\assets\logo.png')

        self.__root.title("AppMain")
        self.__root.geometry("+300+400")
        self.__root.resizable(False, False)
        self.__root.config(bg=color['VT'])

        self.__f_head = Frame(self.__root, bg=color['VT'])

        label_head = Label(self.__f_head, font=("Arial", 10, "bold"), bg=color['VT'], fg=color['WT'])
        label_head.config(text="**{NASA}: Open Innovation Team **   ")
        label_head.pack(side=LEFT)

        label_logo = Label(self.__f_head, image=img_logo)
        label_logo.pack(side=LEFT)

        self.__f_head.pack(side=TOP)

        self.__f_body = Frame(self.__root, bg=color['VT'])

        f_left = Frame(self.__f_body)

        self.box_left = Listbox(f_left, bg=color['BK'], fg=color['WT'], bd=10, width=35)
        self.box_left.pack(side=LEFT)

        frame_button = Frame(f_left)
        cont = 1
        while cont < 7:
            if cont == 1:
                self.but_test_1 = Button(frame_button, width=8, command=self.test_1, text="test 1")
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
                self.but_test_2 = Button(frame_button, width=8, command=self.test_2, text="test 2")
                self.but_test_2.grid(row=cont, column=0)
            else:
                Button(frame_button, state=DISABLED, width=8).grid(row=cont, column=0)
            cont += 1
        frame_button.pack(side=LEFT)

        self.box_right = Listbox(f_right, bg=color['BK'], fg=color['WT'], bd=10, width=35)
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

        self.__root.mainloop()

    def test_1(self):
        self.txt_under.delete(1.0, END)
        self.txt_under.insert(END, "teste 1")

    def test_2(self):
        self.txt_under.delete(1.0, END)
        self.txt_under.insert(END, "teste 2")


AppMain()
