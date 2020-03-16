from tkinter import *
import tkinter.messagebox
from random import randrange
import os
from func import intesection_func


class Main:
    A = set()
    B = set()
    C = set()
    U = set()  # universal set
    operation_Z = set()
    D_initial = ''  # value of initial expression
    D_simplified = ''  # value of initial expression
    i = 0  # iterator for next operation in initial expression
    j = 0  # iterator for next operation in simplified expression
    errors = False
    resultz2 = set()
    rand_down = 0
    rand_up = 200
    def __init__(self, main):
        self.main = root

        # menu
        main_menu = Menu(root)
        elements_of_menu = Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="Windows", menu=elements_of_menu)
        elements_of_menu.add_command(label="Window 2", command=self.window2)
        elements_of_menu.add_command(label="Window 3", command=self.window3)
        elements_of_menu.add_command(label="Window 4", command=self.window4)
        elements_of_menu.add_command(label="Window 5", command=self.window5)
        elements_of_menu.add_command(label="Configuration of random", command=self.window6)
        elements_of_menu.add_command(label="Quit", command=lambda: root.quit())
        root.config(menu=main_menu)

        # frame for information
        text_frame = Frame(root, bg='#002451')
        text_frame.pack(fill=X, pady=5)

        lab_label = Label(text_frame, text="Лабораторна робота №1", fg='#F9F9F9', bg='#002451', font=("Ubuntu", 30), justify=CENTER, anchor='center')
        lab_label.pack(side=TOP, fill=X, pady=20, ipady=5)
        name_label = Label(text_frame, font=('Ubuntu', 15), text="Виконав: Чопик Назар Олегович", bg='#002451', fg='#A9B7C6')
        group_label = Label(text_frame, font=("Ubuntu", 15), text="Група: ІВ-91", anchor='w', bg='#002451', fg='#A9B7C6')
        name_label.pack(pady=5)
        group_label.pack(pady=5)

        # separated frame for entry and label
        frame_for_variant = Frame(text_frame, bg='#002451')
        frame_for_variant.pack()
        number_in_list_label = Label(frame_for_variant, fg='#A9B7C6', font=("Ubuntu", 15), text="Номер у списку:", bg='#002451')
        number_in_list_label.grid(row=0, column=0)
        self.number_entry = Entry(frame_for_variant, width=2, font=35, bg='#284C79', relief=FLAT, fg='#A9B7C6')
        self.number_entry.grid(row=0, column=1)

        # separated frame for button 'Variant' and label
        frame_for_variant2 = Frame(text_frame, bg='#002451')
        frame_for_variant2.pack()
        variant_button = Button(frame_for_variant2, bg='#002451', fg='#A9B7C6', text='Variant', relief=GROOVE, padx=8, pady=2, activebackground='#284C79',
                                command=self.determine_the_variant)
        variant_button.grid(row=0, column=0)
        self.variant_label = Label(frame_for_variant2, font=30, bg='#002451', fg='#A9B7C6')
        self.variant_label.grid(row=0, column=1)

        frame_for_label = Frame(root, bg='#002451')
        frame_for_label.pack(fill=X)
        set_label = Label(frame_for_label, bg='#A9B7C6', fg="#141781", font=("Ubuntu", 20), text="Задання множин")
        set_label.pack(side=TOP, fill=X)
        ################################################################################################################
        # second main frame
        calculation_frame = Frame(root, bg='#002451')
        calculation_frame.pack()

        # scales
        self.s1 = Scale(calculation_frame, orient=HORIZONTAL, length=300, from_=0, to=50, tickinterval=5, resolution=1, font=("Arial", 10), bg='#002451', fg='#A9B7C6',
                        highlightbackground='#002451', activebackground='#FF8C00')
        self.s2 = Scale(calculation_frame, orient=HORIZONTAL, length=300, from_=0, to=50, tickinterval=5, resolution=1, font=("Arial", 10), fg='#A9B7C6', bg='#002451',
                        highlightbackground='#002451', activebackground='#FF8C00')
        self.s3 = Scale(calculation_frame, orient=HORIZONTAL, length=300, from_=0, to=50, tickinterval=5, resolution=1, font=("Arial", 10), fg='#A9B7C6', bg='#002451',
                        highlightbackground='#002451', activebackground='#FF8C00')
        self.s1.grid(row=0, column=0)
        self.s2.grid(row=1, column=0)
        self.s3.grid(row=2, column=0)

        # random buttons
        b_power_A = Button(calculation_frame, width=15, text="Generate A", font=("Arial", 10), bg='#FF8C00', activebackground='#284C79', command=self.power_A)
        b_power_A.grid(row=0, column=1, padx=20)
        b_power_B = Button(calculation_frame, width=15, text="Generate B", font=("Arial", 10), bg='#FF8C00', activebackground='#284C79', command=self.power_B)
        b_power_B.grid(row=1, column=1, padx=20)
        b_power_C = Button(calculation_frame, width=15, text="Generate C", font=("Arial", 10), bg='#FF8C00', activebackground='#284C79', command=self.power_C)
        b_power_C.grid(row=2, column=1, padx=20)

        # entries
        self.e_A = Entry(calculation_frame, width=40, font=("Arial", 13), bg='#284C79', fg='#A9B7C6')
        self.e_A.grid(row=0, column=2)
        self.e_B = Entry(calculation_frame, width=40, font=("Arial", 13), bg='#284C79', fg='#A9B7C6')
        self.e_B.grid(row=1, column=2)
        self.e_C = Entry(calculation_frame, width=40, font=("Arial", 13), bg='#284C79', fg='#A9B7C6')
        self.e_C.grid(row=2, column=2)

        # confirms buttons
        b_power_A = Button(calculation_frame, width=15, text="Confirm A", font=("Arial", 10), bg='#FF8C00', command=self.set_A, activebackground='#284C79')
        b_power_A.grid(row=0, column=3, padx=5)
        b_power_B = Button(calculation_frame, width=15, text="Confirm B", font=("Arial", 10), bg='#FF8C00', command=self.set_B, activebackground='#284C79')
        b_power_B.grid(row=1, column=3, padx=5)
        b_power_C = Button(calculation_frame, width=15, text="Confirm C", font=("Arial", 10), bg='#FF8C00', command=self.set_C, activebackground='#284C79')
        b_power_C.grid(row=2, column=3, padx=5)

        # frame for universal_set set
        un_frame = Frame(root, bg='#002451')
        un_frame.pack(fill=X)
        universal_set_button = Button(un_frame, width=16, text="Set the range of\n universal set", font=("Arial", 12), bg='#FF8C00', activebackground='#284C79',
                                      command=self.universal_set)
        self.universal_entry_down = Entry(un_frame, width=10, font=("Arial", 17), bg='#284C79', fg='#A9B7C6')
        self.universal_entry_up = Entry(un_frame, width=10, font=("Arial", 17), bg='#284C79', fg='#A9B7C6')

        universal_set_button.pack(side=LEFT, pady=10)
        self.universal_entry_down.pack(side=LEFT, padx=10, pady=10)
        self.universal_entry_up.pack(side=LEFT, padx=10, pady=10)

    def window2(self):
        self.win2 = Toplevel(root)
        self.win2.title("Window 2")
        self.win2.configure(background='#002451')
        self.win2.resizable(width=False, height=False)
        l_X = Label(self.win2, text="A = ", font=("Arial", 20), bg='#002451', fg='#A9B7C6')
        l_Y = Label(self.win2, text="B = ", font=("Arial", 20), bg='#002451', fg='#A9B7C6')
        l_Z = Label(self.win2, text="C = ", font=("Arial", 20), bg='#002451', fg='#A9B7C6')
        l_D = Label(self.win2, text="D = ", font=("Arial", 20), bg='#002451', fg='#A9B7C6')
        l_func = Label(self.win2, text=r"D = ¬C ∩ (A\C) ∩ (B\C)) ∩ (¬C ∪ B)", font=("Arial", 20), bg='#002451', fg='#A9B7C6')
        l_step = Label(self.win2, text="Operation", font=("Arial", 20), bg='#002451', fg='#A9B7C6')
        l_X.grid(row=0)
        l_Y.grid(row=1)
        l_Z.grid(row=2)
        l_func.grid(row=3, columnspan=2)
        l_step.grid(row=5)
        l_D.grid(row=6)

        self.tA = Text(self.win2, width=100, height=4, font=("Arial", 10), wrap=WORD, bg='#284C79', fg='#A9B7C6', relief=FLAT, yscrollcommand=set())
        self.tB = Text(self.win2, width=100, height=4, font=("Arial", 10), wrap=WORD, bg='#284C79', fg='#A9B7C6', relief=FLAT, yscrollcommand=set())
        self.tC = Text(self.win2, width=100, height=4, font=("Arial", 10), wrap=WORD, bg='#284C79', fg='#A9B7C6', relief=FLAT, yscrollcommand=set())
        self.tD = Text(self.win2, width=100, height=7, font=("Arial", 10), wrap=WORD, bg='#284C79', fg='#A9B7C6', relief=FLAT, yscrollcommand=set())
        self.t_step = Text(self.win2, width=100, height=5, font=("Arial", 10), wrap=WORD, bg='#284C79', fg='#A9B7C6', relief=FLAT, yscrollcommand=set())
        self.tA.grid(row=0, column=1, padx=3, pady=5)
        self.tB.grid(row=1, column=1, padx=3, pady=5)
        self.tC.grid(row=2, column=1, padx=3, pady=5)
        self.t_step.grid(row=5, column=1, padx=3, pady=5)
        self.tD.grid(row=6, column=1, padx=3, pady=5)

        self.tA.insert(INSERT, list(self.A))
        self.tB.insert(INSERT, list(self.B))
        self.tC.insert(INSERT, list(self.C))
        self.b_step = Button(self.win2, width=15, text="Calculate", font=("Arial", 10), bg='#FF8C00', activebackground='#284C79', command=self.initial_func)
        self.b_step.grid(row=4, columnspan=2)
        b_save = Button(self.win2, width=15, text="Save", font=("Arial", 10), bg='#FF8C00', activebackground='#284C79', command=self.save_initial_func)
        b_save.grid(row=7, columnspan=2)

    def window3(self):
        self.win3 = Toplevel(root)
        self.win3.title("Window 3")
        self.win3.configure(background='#002451')
        self.win3.resizable(width=False, height=False)
        l_X = Label(self.win3, text="A = ", font=("Arial", 20), bg='#002451', fg='#A9B7C6')
        l_Y = Label(self.win3, text="B = ", font=("Arial", 20), bg='#002451', fg='#A9B7C6')
        l_Z = Label(self.win3, text="C = ", font=("Arial", 20), bg='#002451', fg='#A9B7C6')
        l_D = Label(self.win3, text="D = ", font=("Arial", 20), bg='#002451', fg='#A9B7C6')
        l_func = Label(self.win3, text=r"D = ¬C ∩ A ∩ B", font=("Arial", 20), bg='#002451', fg='#A9B7C6')
        l_step = Label(self.win3, text="Operation", font=("Arial", 20), bg='#002451', fg='#A9B7C6')
        l_X.grid(row=0)
        l_Y.grid(row=1)
        l_Z.grid(row=2)
        l_func.grid(row=3, columnspan=2)
        l_step.grid(row=5)
        l_D.grid(row=6)

        self.tA3 = Text(self.win3, width=100, height=4, font=("Arial", 10), wrap=WORD, bg='#284C79', fg='#A9B7C6', relief=FLAT, yscrollcommand=set())
        self.tB3 = Text(self.win3, width=100, height=4, font=("Arial", 10), wrap=WORD, bg='#284C79', fg='#A9B7C6', relief=FLAT, yscrollcommand=set())
        self.tC3 = Text(self.win3, width=100, height=4, font=("Arial", 10), wrap=WORD, bg='#284C79', fg='#A9B7C6', relief=FLAT, yscrollcommand=set())
        self.tD3 = Text(self.win3, width=100, height=7, font=("Arial", 10), wrap=WORD, bg='#284C79', fg='#A9B7C6', relief=FLAT, yscrollcommand=set())
        self.t_step3 = Text(self.win3, width=100, height=5, font=("Arial", 10), wrap=WORD, bg='#284C79', fg='#A9B7C6', relief=FLAT, yscrollcommand=set())
        self.tA3.grid(row=0, column=1, padx=3, pady=5)
        self.tB3.grid(row=1, column=1, padx=3, pady=5)
        self.tC3.grid(row=2, column=1, padx=3, pady=5)
        self.t_step3.grid(row=5, column=1, padx=3, pady=5)
        self.tD3.grid(row=6, column=1, padx=3, pady=5)

        self.tA3.insert(INSERT, list(self.A))
        self.tB3.insert(INSERT, list(self.B))
        self.tC3.insert(INSERT, list(self.C))
        self.b_step3 = Button(self.win3, width=15, text="Calculate", font=("Arial", 10), bg='#FF8C00', activebackground='#284C79', command=self.simplified_func)
        self.b_step3.grid(row=4, columnspan=2)
        b_save3 = Button(self.win3, width=15, text="Save", font=("Arial", 10), bg='#FF8C00', activebackground='#284C79', command=self.save_simplified_func)
        b_save3.grid(row=7, columnspan=2)

    def window4(self):

        self.win4 = Toplevel(root)
        self.win4.title("Windows 4")
        self.win4.configure(background='#002451')
        self.win4.resizable(width=False, height=False)
        frame1 = Frame(self.win4, bg='#002451')
        frame1.pack(fill=X)
        l_X = Label(frame1, text="X = C =", font=("Arial", 20), bg='#002451', fg='#A9B7C6')
        l_Y = Label(frame1, text="Y = B =", font=("Arial", 20), bg='#002451', fg='#A9B7C6')
        l_Z = Label(frame1, text="Z = X ∩ Y =", font=("Arial", 20), bg='#002451', fg='#A9B7C6')
        l_X.grid(row=0)
        l_Y.grid(row=1)
        l_Z.grid(row=3)

        self.tX4 = Text(frame1, width=100, height=5, font=("Arial", 10), bg='#284C79', fg='#A9B7C6', relief=FLAT, yscrollcommand=set())
        self.tY4 = Text(frame1, width=100, height=5, font=("Arial", 10), bg='#284C79', fg='#A9B7C6', relief=FLAT, yscrollcommand=set())
        self.tZ4 = Text(frame1, width=100, height=5, font=("Arial", 10), bg='#284C79', fg='#A9B7C6', relief=FLAT, yscrollcommand=set())
        self.tX4.grid(row=0, column=1, padx=5, pady=5)
        self.tY4.grid(row=1, column=1, padx=5, pady=5)
        self.tZ4.grid(row=3, column=1, padx=5, pady=5)

        self.tX4.insert(INSERT, list(self.C))
        self.tY4.insert(INSERT, list(self.B))

        frame2 = Frame(self.win4, bg='#002451')
        frame2.pack(fill=X, side=TOP)
        b_step = Button(frame2, width=15, text="Calculate Z", font=("Arial", 10), bg='#FF8C00', activebackground='#284C79', command=self.calculate_Z)
        b_step.pack(side=TOP)
        b_save = Button(frame2, width=15, text="Save", font=("Arial", 10), bg='#FF8C00', activebackground='#284C79', command=self.save_Z)
        b_save.pack(side=TOP, pady=7)
        '''write save function'''

    def window5(self):
        def readD1():
            path = os.getcwd()
            with open(path + '\saved_initial_func.txt', 'r', encoding='utf-8') as file:
                x = file.read()
                tD1.delete(1.0, END)
                tD1.insert(1.0, x)
        def readD2():
            path = os.getcwd()
            with open(path + '\saved_simplified_func.txt', 'r', encoding='utf-8') as file:
                x = file.read()
                tD2.delete(1.0, END)
                tD2.insert(1.0, x)

        def readZ1():
            path = os.getcwd()
            with open(path + '\saved_Z_func.txt', 'r', encoding='utf-8') as file:
                x = file.read()
                tZ1.delete(1.0,END)
                tZ1.insert(1.0, x)

        def calculate_Z2():
            self.resultz2 = (self.C).intersection(self.B)
            tZ2.delete(1.0, END)
            tZ2.insert(1.0, self.resultz2)

        def difference_D():
            path = os.getcwd()
            with open(path + '\saved_initial_func.txt', 'r', encoding='utf-8') as file:
                D1 = file.read()
            with open(path + '\saved_simplified_func.txt', 'r', encoding='utf-8') as file:
                D2 = file.read()

            if set(D1) == set(D2):
                difference_DL.configure(text='D1 = D2')
            else:
                difference_DL.configure(text='D1 != D2')

        def difference_Z():
            path = os.getcwd()
            with open(path + '\saved_Z_func.txt', 'r', encoding='utf-8') as file:
                Z1 = file.read()

            if set(str(self.resultz2)) == set(Z1):
                difference_ZL.configure(text='Z1 = Z2')
            else:
                difference_ZL.configure(text='Z1 != Z2')


        self.win5 = Toplevel(root)
        self.win5.title("Windows 5")
        self.win5.configure(background='#002451')
        self.win5.resizable(width=False, height=False)

        l_D1 = Label(self.win5, text="D1 = ", font=("Arial", 20), bg='#002451', fg='#A9B7C6')
        l_D1.grid(row=0, column=0)
        l_D2 = Label(self.win5, text="D2 = ", font=("Arial", 20), bg='#002451', fg='#A9B7C6')
        l_D2.grid(row=2, column=0)
        l_Z1 = Label(self.win5, text="Z1 = ", font=("Arial", 20), bg='#002451', fg='#A9B7C6')
        l_Z1.grid(row=4, column=0)
        l_Z2 = Label(self.win5, text="Z2 = ", font=("Arial", 20), bg='#002451', fg='#A9B7C6')
        l_Z2.grid(row=6, column=0)

        tD1 = Text(self.win5, width=100, height=3, font=("Arial", 10), wrap=WORD, bg='#284C79', fg='#A9B7C6', relief=FLAT, yscrollcommand=set())
        tD1.grid(row=0, column=1, pady=10)
        b_readD1 = Button(self.win5, width=7, text="Read D1", font=("Arial", 15), bg='#FF8C00', activebackground='#284C79', command=readD1)
        b_readD1.grid(row=1, column=1, padx=5, pady=3)

        tD2 = Text(self.win5, width=100, height=3, font=("Arial", 10), wrap=WORD, bg='#284C79', fg='#A9B7C6', relief=FLAT, yscrollcommand=set())
        tD2.grid(row=2, column=1, pady=10)
        b_readD2 = Button(self.win5, width=7, text="Read D2", font=("Arial", 15), bg='#FF8C00', activebackground='#284C79', command=readD2)
        b_readD2.grid(row=3, column=1, padx=5, pady=3)

        tZ1 = Text(self.win5, width=100, height=3, font=("Arial", 10), wrap=WORD, bg='#284C79', fg='#A9B7C6', relief=FLAT, yscrollcommand=set())
        tZ1.grid(row=4, column=1, pady=10)
        b_readZ1 = Button(self.win5, width=7, text="Read Z1", font=("Arial", 15), bg='#FF8C00', activebackground='#284C79', command=readZ1)
        b_readZ1.grid(row=5, column=1, padx=5, pady=3)

        tZ2 = Text(self.win5, width=100, height=3, font=("Arial", 10), wrap=WORD, bg='#284C79', fg='#A9B7C6', relief=FLAT, yscrollcommand=set())
        tZ2.grid(row=6, column=1, pady=10)
        b_readZ2 = Button(self.win5, width=7, text="Read Z2", font=("Arial", 15), bg='#FF8C00', activebackground='#284C79', command=calculate_Z2)
        b_readZ2.grid(row=7, column=1, padx=5, pady=3)

        frame = Frame(self.win5, bg='#002451')
        frame.grid(row=8, column=1, pady=15,sticky=W)

        difference_D = Button(frame, width=15, text="Difference D", font=("Arial", 13), bg='#284C79',fg='#A9B7C6', relief=FLAT, activebackground='#284C79', command=difference_D)
        difference_D.grid(row=0, column=0, pady=10)
        difference_DL = Label(frame, text='', fg='#A9B7C6', bg='#002451', font=20)
        difference_DL.grid(row=0, column=1, padx=10, pady=10)


        difference_ZB = Button(frame, text="Difference Z", font=("Arial",13), width=15,fg='#A9B7C6', bg='#284C79', relief=FLAT, activebackground='#284C79', command =difference_Z)
        difference_ZL = Label(frame, text='', fg='#A9B7C6', bg='#002451', font=20)
        difference_ZB.grid(row=1, column=0, pady=5)
        difference_ZL.grid(row=1, column=1, padx=10, pady=10)


    def window6(self):
        def rand_down():
            self.rand_down = int(config_en_down.get())
            config_en_down.delete(0,END)
            config_en_down.insert(INSERT, self.rand_down)

        def rand_up():
            self.rand_up = int(config_en_up.get())
            config_en_up.delete(0, END)
            config_en_up.insert(INSERT, self.rand_up)
            self.rand_up += 1

        self.win6 = Toplevel(root)
        self.win6.title("Configuration of random")
        self.win6.configure(background='#002451')
        self.win6.resizable(width=False, height=False)
        frame1 = Frame(self.win6, bg='#002451')
        frame1.pack(fill=X)
        main_label = Label(frame1, fg='#A9B7C6', font=("Ubuntu", 30), text="Configurate random", bg='#002451')
        main_label.pack(fill=X,padx=10,pady=10)

        frame2 = Frame(self.win6, bg='#002451')
        frame2.pack()
        config_b_down = Button(frame2, width=15, text="Set DOWN", font=("Arial", 10), bg='#FF8C00', activebackground='#284C79', command=rand_down)
        config_en_down = Entry(frame2, width=10, font=("Arial", 13), bg='#284C79', fg='#A9B7C6')
        config_b_down.grid(row=0, column=0, sticky=NE, padx=10, pady=5)
        config_en_down.grid(row=0, column=1,sticky=NE, pady=5)
        config_en_down.insert(INSERT, self.rand_down)

        config_en_up = Entry(frame2, width=10, font=("Arial", 13), bg='#284C79', fg='#A9B7C6')
        config_b_up = Button(frame2, width=15, text="Set UP", font=("Arial", 10), bg='#FF8C00', activebackground='#284C79', command=rand_up)
        config_b_up.grid(row=1, column=0, sticky=NE, padx=10, pady=5)
        config_en_up.grid(row=1, column=1, sticky=NE, pady=5)
        config_en_up.insert(INSERT, self.rand_up)

        frame3 = Frame(self.win6, bg='#002451')
        frame3.pack(side=RIGHT)
        my_l = Label(frame3, fg='#A9B7C6', font=("Times", 10), text="Made by Naz", bg='#002451')
        my_l.pack(side=RIGHT)


    # functional block
    def determine_the_variant(self):
        if self.number_entry.get() != '' and self.number_entry.get().isnumeric():
            G = 91
            N = int(self.number_entry.get())
            M = "IV"
            print("Моя група: ", M + "-", G)
            print("Мій номер у групі:", N)
            if M == "ІО":
                N += 2
            result = (N + G % 60) % 30 + 1
            print("Мій варіант:", result)
            self.variant_label.configure(text=result)

    # random set
    def power_A(self):
        A = set()
        while len(A) != self.s1.get():
            A.add(randrange(self.rand_down, self.rand_up))
        self.e_A.delete(0, END)
        self.e_A.insert(0, list(A))

    def power_B(self):
        B = set()
        while len(B) != self.s2.get():
            B.add(randrange(self.rand_down, self.rand_up))
        self.e_B.delete(0, END)
        self.e_B.insert(0, list(B))

    def power_C(self):
        C = set()
        while len(C) != self.s3.get():
            C.add(randrange(self.rand_down, self.rand_up))
        self.e_C.delete(0, END)
        self.e_C.insert(0, list(C))

    def set_A(self):
        input_A = self.A = str(self.e_A.get()).split()
        temp = set()
        for i in input_A:
            if i.isnumeric():
                i = int(i)
                temp.add(i)
        self.A = temp

    def set_B(self):
        input_B = (str(self.e_B.get()).split())
        temp = set()
        for i in input_B:
            if i.isnumeric():
                i = int(i)
                temp.add(i)
        self.B = temp


    def set_C(self):
        input_C = (str(self.e_C.get()).split())
        temp = set()
        for i in input_C:
            if i.isnumeric():
                i = int(i)
                temp.add(i)
        self.C = temp

    def default_U(self):
        max_nums = []
        down = 0
        max_nums.append(max(self.A))
        max_nums.append(max(self.B))
        max_nums.append(max(self.C))
        up = max(max_nums)
        for i in range(int(down), int(up) + 1):
            self.U.add(i)

    def universal_set(self):
        self.U.clear()
        down = self.universal_entry_down.get()
        up = self.universal_entry_up.get()
        max_nums = []

        if (down.isnumeric()) and (up.isnumeric()):
            if int(down) < int(up):
                for i in range(int(down), int(up) + 1):
                    self.U.add(i)
            else:
                self.default_U()
        else:
            self.default_U()


    # functions fow window 2
    def initial_func(self):
        try:
            if str(self.U) == 'set()':
                self.default_U()
        except:
            tkinter.messagebox.showerror('ValueError', 'Empty sets\n\nFill the input field')
            self.errors = True

        if self.i == 0:
            if not self.errors:
                self.b_step.configure(text='Next')
                # A\C
                self.operation1 = self.A - self.C
                self.D_initial = f'{self.U - self.C} ∩ ({self.operation1}) ∩ ({self.B} \ {self.C}) ∩ ({self.U - self.C} ∪ {self.B})'
                self.tD.delete(1.0, END)
                self.tD.insert(INSERT, self.D_initial)

                self.t_step.delete(1.0, END)
                self.t_step.insert(INSERT, f'1. A\C \n{self.A} \ {self.C} = {self.operation1}')
                self.i += 1
            elif self.errors:
                self.i = 0
                self.errors = False
                self.win2.destroy()


        elif self.i == 1:
            # B\C
            self.operation2 = self.B - self.C
            self.D_initial = f'{self.U - self.C} ∩ ({self.operation1}) ∩ ({self.operation2}) ∩ ({self.U - self.C} ∪ {self.B})'
            self.tD.delete(1.0, END)
            self.tD.insert(INSERT, self.D_initial)

            self.t_step.delete(1.0, END)
            self.t_step.insert(INSERT, f'2. B\C \n{self.B} \ {self.C} = {self.operation2}')
            self.i += 1

        elif self.i == 2:
            # ¬C ∪ B
            self.operation3 = (self.U - self.C).union(self.B)
            self.D_initial = f'{self.U - self.C} ∩ ({self.operation1}) ∩ ({self.operation2}) ∩ ({self.operation3})'
            self.tD.delete(1.0, END)
            self.tD.insert(INSERT, self.D_initial)

            self.t_step.delete(1.0, END)
            self.t_step.insert(INSERT, f'3. ¬C ∪ B \n{self.U - self.C} ∪ {self.B} = {self.operation3}')
            self.i += 1

        elif self.i == 3:
            # ¬C ∩ (A\C)
            self.operation4 = (self.U - self.C) & self.operation1
            self.D_initial = f'({self.operation4}) ∩ ({self.operation2}) ∩ ({self.operation3})'

            self.tD.delete(1.0, END)
            self.tD.insert(INSERT, self.D_initial)
            self.t_step.delete(1.0, END)
            self.t_step.insert(INSERT, f'4. ¬C ∩ (A\C) \n{self.U - self.C} ∩ {self.operation1} = {self.operation4}')
            self.i += 1

        elif self.i == 4:
            # (¬C ∩ (A\C)) ∩ (B\C)
            self.operation5 = self.operation4 & self.operation2

            self.D_initial = f'({self.operation5}) ∩ ({self.operation3})'
            self.tD.delete(1.0, END)
            self.tD.insert(INSERT, self.D_initial)
            self.t_step.delete(1.0, END)
            self.t_step.insert(INSERT, f'5. (¬C ∩ (A\C)) ∩ (B\C) \n{self.operation4} ∩ {self.operation2} = {self.operation5}')
            self.i += 1

        elif self.i == 5:
            # ((¬C ∩ (A\C) ∩ (B\C)) ∩ (¬C ∪ B)
            self.operation6 = self.operation5 & self.operation3
            self.D_initial = f'({self.operation5} ∩ {self.operation3})'
            self.tD.delete(1.0, END)
            self.tD.insert(INSERT, self.D_initial)
            self.t_step.delete(1.0, END)
            self.t_step.insert(INSERT, f'6. ((¬C ∩ (A\C) ∩ (B\C)) ∩ (¬C ∪ B) \n{self.operation5} ∩ {self.operation3} = {self.operation6}')
            self.i += 1

        elif self.i == 6:
            self.tD.delete(1.0, END)
            self.D_initial = self.operation6
            self.tD.insert(INSERT, self.operation6)
            self.t_step.delete(1.0, END)
            self.t_step.insert(INSERT, 'ANSWER')
            self.i += 1

        else:
            self.tD.delete(1.0, END)
            self.t_step.delete(1.0, END)
            self.i = 0
            self.b_step.configure(text='Calculate')


    def simplified_func(self):
        try:
            if str(self.U) == 'set()':
                self.default_U()
        except:
            tkinter.messagebox.showerror('ValueError', 'Empty sets\n\nFill the input field')
            self.errors = True

        if self.j == 0:
            if not self.errors:
                self.b_step3.configure(text='Next')
                #  D = ¬C ∩ A ∩ B
                self.operation1_3 = (self.U - self.C) & self.A
                self.D_simplified = f'{self.operation1_3} ∩ ({self.A})'
                self.tD3.delete(1.0, END)
                self.tD3.insert(INSERT, self.D_simplified)

                self.t_step3.delete(1.0, END)
                self.t_step3.insert(INSERT, f'1. ¬C ∩ A \n{self.U-self.C} ∩ {self.A} = {self.operation1_3}')
                self.j += 1
            elif self.errors:
                self.j = 0
                self.errors = False
                self.win3.destroy()

        elif self.j == 1:
            
            self.operation2_3 = (self.operation1_3) & (self.B)
            self.D_simplified = f'{self.operation1_3} ∩ ({self.B})'
            self.tD3.delete(1.0, END)
            self.tD3.insert(INSERT, self.D_simplified)

            self.t_step3.delete(1.0, END)
            self.t_step3.insert(INSERT, f'2. (¬C ∩ A) ∩ B\n{self.operation1_3} ∩ {self.B} = {self.operation2_3}')
            self.j += 1

        

        elif self.j == 2:
            self.tD3.delete(1.0, END)
            self.tD3.insert(INSERT, self.operation2_3)
            self.t_step3.delete(1.0, END)
            self.t_step3.insert(INSERT, 'ANSWER')
            self.j += 1

        else:
            self.tD3.delete(1.0, END)
            self.t_step3.delete(1.0, END)
            self.j = 0
            self.b_step3.configure(text='Calculate')



    def save_initial_func(self):
        path = os.getcwd()
        with open(path + '\saved_initial_func.txt', 'w', encoding='utf-8') as file:
            file.write(str(self.D_initial))
        print('The result was saved at ' + str(path) + '\saved_initial_func.txt')

    def save_simplified_func(self):
        path = os.getcwd()
        with open(path + '\saved_simplified_func.txt', 'w', encoding='utf-8') as file:
            file.write(str(self.operation2_3))
        print('The result was saved at ' + str(path) + '\saved_simplified_func.txt')

    def calculate_Z(self):
        # X ∩ Y\
        self.tZ4.delete(1.0, END)
        self.operation_Z = intesection_func.intersect(self.C, self.B)
        if self.operation_Z:
            self.tZ4.insert(INSERT, self.operation_Z)
        else:
            self.operation_Z = 'set()'
            self.tZ4.insert(INSERT, self.operation_Z)

    def save_Z(self):
        path = os.getcwd()
        with open(path + '\saved_Z_func.txt', 'w', encoding='utf-8') as file:
            file.write(str(self.operation_Z))
        print('The result was saved at ' + str(path) + '\saved_Z_func.txt')

root = Tk()
root.configure(background='#024FBF')
root.resizable(width=False, height=False)
root.title('Main')
program = Main(root)
root.mainloop()