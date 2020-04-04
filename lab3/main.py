from tkinter import *
import os
import networkx as nx
import matplotlib.pyplot as plt
import tkinter.messagebox
import webbrowser


class Window1:
    A = set()
    B = set()
    R = list()
    S = list()

    def __init__(self, main):
        self.main = root

        # menu
        main_menu = Menu(root)
        elements_of_menu = Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="Windows", menu=elements_of_menu)
        # elements_of_menu.add_command(label="Window 2", command=self.window2)
        # elements_of_menu.add_command(label="Window 3", command=self.window3)
        # elements_of_menu.add_command(label="Window 4", command=self.window4)
        elements_of_menu.add_command(label="GitHub", command=lambda: webbrowser.open("https://github.com/naz-olegovich/Discrete-Math/tree/master/lab3"))

        elements_of_menu.add_command(label="Quit", command=lambda: root.quit())
        root.config(menu=main_menu)

        # frame for information
        text_frame = Frame(root, bg='#002451')
        text_frame.pack(fill=X, pady=5)

        lab_label = Label(text_frame, text="    Лабораторна робота №3   ", fg='#F9F9F9', bg='#002451', font=("Ubuntu", 30), justify=CENTER, anchor='center')
        lab_label.pack(side=TOP, fill=X, pady=20, ipady=5)
        name_label = Label(text_frame, font=('Ubuntu', 15), text="Виконав: Чопик Назар Олегович", bg='#002451', fg='#A9B7C6')
        group_label = Label(text_frame, font=("Ubuntu", 15), text="Група: ІВ-91", anchor='w', bg='#002451', fg='#A9B7C6')
        name_label.pack(pady=5)
        group_label.pack(pady=5)

        # separated frame for entry and label
        frame_for_variant = Frame(text_frame, bg='#002451')
        frame_for_variant.pack()
        number_in_list_label = Label(frame_for_variant, fg='#A9B7C6', font=("Ubuntu", 15), text="Номер у списку: 28", bg='#002451')
        number_in_list_label.grid(row=0, column=0)


        # separated frame for button 'Variant' and label
        frame_for_variant2 = Frame(text_frame, bg='#002451')
        frame_for_variant2.pack()
        variant_button = Button(frame_for_variant2, bg='#002451', fg='#A9B7C6', text='Variant', relief=GROOVE, padx=8, pady=2, activebackground='#284C79',
                                command=self.determine_the_variant)
        variant_button.grid(row=0, column=0)
        self.variant_label = Label(frame_for_variant2, font=30, bg='#002451', fg='#A9B7C6')
        self.variant_label.grid(row=0, column=1)

    def determine_the_variant(self):
        G = 91

        N = 28
        M = "ІВ"
        print("Моя група: ", M + " -", G)
        print("Мій номер у групі:", N)
        if M == "ІО": N += 1
        var = 9130 % 10 + 1
        self.variant_label.configure(text=var)
        print("Мій варіант:", var)




root = Tk()
root.configure(background='#024FBF')
root.resizable(width=False, height=False)
root.title('Main')
program = Window1(root)
root.mainloop()
