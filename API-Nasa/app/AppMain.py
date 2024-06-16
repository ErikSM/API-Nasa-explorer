from tkinter import *


color = {'VT': "#160E3D", 'BK': "black", 'WT': "white"}


class AppMain:

    def __init__(self):
        self.__root = Tk()

        self.__root.title("AppMain")
        self.__root.geometry("+300+400")
        self.__root.resizable(False, False)
        self.__root.config(bg=color['VT'])

        self.__f_head = Frame(self.__root, bg=color['VT'])
        label_head = Label(self.__f_head, font=("Arial", 10, "bold"), bg=color['VT'], fg=color['WT'])
        label_head.config(text="* {NASA}: Open Innovation Team")
        label_head.pack()
        self.__f_head.pack(side=TOP)

        self.__f_body = Frame(self.__root, bg=color['VT'])

        f_left = Frame(self.__f_body)
        self.box_left = Listbox(f_left, bg=color['BK'], fg=color['WT'], bd=10)
        self.box_left.pack()
        f_left.grid(row=1, column=1)

        f_right = Frame(self.__f_body)
        self.box_right = Listbox(f_right, bg=color['BK'], fg=color['WT'], bd=10)
        self.box_right.pack()
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


AppMain()
