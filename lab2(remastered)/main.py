from tkinter import *
import os
import networkx as nx
import matplotlib.pyplot as plt
from random import randint, sample
from Relation_S import relations_S
from Relation_R import relations_R
import logic_functions
import tkinter.messagebox
from tkintertable.Tables import TableCanvas
from tkintertable.TableModels import TableModel


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
        elements_of_menu.add_command(label="Window 2", command=self.window2)
        elements_of_menu.add_command(label="Window 3", command=self.window3)
        elements_of_menu.add_command(label="Window 4", command=self.window4)
        elements_of_menu.add_command(label="Quit", command=lambda: root.quit())
        root.config(menu=main_menu)

        # frame for information
        text_frame = Frame(root, bg='#002451')
        text_frame.pack(fill=X, pady=5)

        lab_label = Label(text_frame, text="    Лабораторна робота №2   ", fg='#F9F9F9', bg='#002451', font=("Ubuntu", 30), justify=CENTER, anchor='center')
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

    def window2(self):
        def save_A():
            path = os.getcwd()
            with open(path + "\saved_A.txt", "w") as w:
                for i in self.A:
                    w.write(str(i) + "\n")
            print('The result was saved at ' + str(path) + '\saved_A.txt')

        def save_B():
            path = os.getcwd()
            with open(path + "\saved_B.txt", "w") as w:
                for i in self.B:
                    w.write(str(i) + "\n")
            print('The result was saved at ' + str(path) + '\saved_B.txt')

        def read_A():
            self.A.clear()
            path = os.getcwd()
            with open(path + "\saved_A.txt", "r") as r:
                for line in r:
                    self.A.add(line[:-1])
            print('The file was read from ' + str(path) + '\saved_A.txt')

        def read_B():
            self.B.clear()
            path = os.getcwd()
            with open(path + "\saved_B.txt", "r") as r:
                for line in r:
                    self.B.add(line[:-1])
            print('The file was read from ' + str(path) + '\saved_B.txt')

        def clear_A():
            self.A.clear()

        def clear_B():
            self.B.clear()

        self.win2 = Toplevel(root)
        self.win2.title("Window 2")
        self.win2.configure(background='#002451')
        self.win2.resizable(width=False, height=False)
        main_menu = Menu(self.win2)
        elements_of_menu = Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="Windows", menu=elements_of_menu)
        elements_of_menu.add_command(label="Window 3", command=self.window3)
        elements_of_menu.add_command(label="Window 4", command=self.window4)
        elements_of_menu.add_command(label="Quit", command=lambda: root.quit())
        self.win2.config(menu=main_menu)

        def set_W():
            if women_select.get() == "A":
                for i in list_of_women.curselection():
                    self.A.add(self.list_of_women_names[i])

            elif women_select.get() == "B":
                for i in list_of_women.curselection():
                    self.B.add(self.list_of_women_names[i])

        def set_M():
            if men_select.get() == "A":
                for i in list_of_men.curselection():
                    self.A.add(self.list_of_men_names[i])

            elif men_select.get() == "B":
                for i in list_of_men.curselection():
                    self.B.add(self.list_of_men_names[i])

        l_w = Label(self.win2, text="List of women names ", font=("Arial", 15, "bold"), bg='#002451', fg='#FF8C00')
        l_w.grid(row=0, column=0, pady=7)
        list_of_women = Listbox(self.win2, font=("Times", 16), selectmode=EXTENDED, highlightcolor="gold", bg='#284C79', fg='#A9B7C6', selectbackground='#FF8C00',
                                relief=FLAT, yscrollcommand=set())
        self.list_of_women_names = ["Adriana", "Anna", "Elizabeth", "Camilla", "Gloria", "Helen", "Mary", "Molly", "Julia", "Selena",
                                    'Arabella', "Bella", "Carla", "Donna", "Doris", "Elly"]
        for i in self.list_of_women_names:
            list_of_women.insert(END, str(i))
        list_of_women.grid(row=1, column=0, padx=7, pady=5)
        women_select = StringVar()
        women_select.set('A')
        women_aRB = Radiobutton(self.win2, text='A', variable=women_select, value="A", relief=FLAT, activebackground='#284C79', activeforeground='#FF8C00', bg='#284C79')
        women_bRB = Radiobutton(self.win2, text='B', variable=women_select, value="B", relief=FLAT, activebackground='#284C79', activeforeground='#FF8C00', bg='#284C79')
        women_aRB.grid(row=2, column=0, sticky=E, padx=110)
        women_bRB.grid(row=2, column=0, sticky=E, padx=70)
        b_w = Button(self.win2, text="Add to", bg='#FF8C00', activebackground='#284C79', relief=FLAT, command=set_W)
        b_w.grid(row=2, column=0, sticky=W, padx=80, pady=5)

        l_m = Label(self.win2, text="List of men names  ", font=("Arial", 15, "bold"), bg='#002451', fg='#FF8C00')
        l_m.grid(row=0, column=1, pady=7)
        list_of_men = Listbox(self.win2, font=("Times", 16), selectmode=EXTENDED, highlightcolor="gold", bg='#284C79', fg='#A9B7C6', selectbackground='#FF8C00',
                              relief=FLAT, yscrollcommand=set())
        self.list_of_men_names = ["Albert", "Alexander", "Benjamin", "Bill", "Edward", "Hector", "Isaac", "Kelvin", "Mark",
                                  "Raymond", "Samuel", "Berthold", "Christian", "Donald", "Elbert "]
        for i in self.list_of_men_names:
            list_of_men.insert(END, str(i))
        list_of_men.grid(row=1, column=1, padx=7, pady=5)
        men_select = StringVar()
        men_select.set("A")
        men_a = Radiobutton(self.win2, text='A', variable=men_select, value="A", relief=FLAT, activebackground='#284C79', activeforeground='#FF8C00', bg='#284C79')
        men_b = Radiobutton(self.win2, text='B', variable=men_select, value="B", relief=FLAT, activebackground='#284C79', activeforeground='#FF8C00', bg='#284C79')
        men_a.grid(row=2, column=1, sticky=E, padx=110)
        men_b.grid(row=2, column=1, sticky=E, padx=70)
        save_to_m = Button(self.win2, text="Add to", bg='#FF8C00', activebackground='#284C79', relief=FLAT, command=set_M)
        save_to_m.grid(row=2, column=1, sticky=W, padx=80, pady=5)

        save_a_b = Button(self.win2, text="Save A to file", bg='#FF8C00', activebackground='#284C79', command=save_A)
        save_a_b.grid(row=3, column=0, pady=5, sticky=E, padx=5)
        save_b_b = Button(self.win2, text="Save B to file", bg='#FF8C00', activebackground='#284C79', command=save_B)
        save_b_b.grid(row=3, column=1, sticky=W, padx=5)

        read_a_b = Button(self.win2, text="Read A from file", bg='#FF8C00', activebackground='#284C79', command=read_A)
        read_a_b.grid(row=4, column=0, sticky=E, padx=5)
        read_b_b = Button(self.win2, text="Read B from file", bg='#FF8C00', activebackground='#284C79', command=read_B)
        read_b_b.grid(row=4, column=1, sticky=W, padx=5)

        clear_a_b = Button(self.win2, text="Delete A", bg='#FF8C00', activebackground='#284C79', command=clear_A)
        clear_a_b.grid(row=5, column=0, pady=5, sticky=E, padx=5)
        clear_b_b = Button(self.win2, text="Delete B", bg='#FF8C00', activebackground='#284C79', command=clear_B)
        clear_b_b.grid(row=5, column=1, sticky=W, padx=5)

    def window3(self):
        self.win3 = Toplevel(root)
        self.win3.title("Window 3")
        self.win3.configure(background='#002451')
        self.win3.resizable(width=False, height=False)
        main_menu = Menu(self.win3)
        elements_of_menu = Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="Windows", menu=elements_of_menu)
        elements_of_menu.add_command(label="Window 4", command=self.window4)
        elements_of_menu.add_command(label="Quit", command=lambda: root.quit())
        self.win3.config(menu=main_menu)

        def update_a():
            listbox_a.delete(0, END)
            for i in list(self.A):
                listbox_a.insert(END, str(i))

        def update_b():
            listbox_b.delete(0, END)
            for i in list(self.B):
                listbox_b.insert(END, str(i))

        l_a = Label(self.win3, text="Set А", font=("Arial", 15, "bold"), bg='#002451', fg='#FF8C00')
        l_a.grid(row=0, column=0)
        listbox_a = Listbox(self.win3, font=("Arial", 16), selectmode=EXTENDED, highlightcolor="gold", bg='#284C79', fg='#A9B7C6', selectbackground='#FF8C00',
                            relief=FLAT, yscrollcommand=set())
        update_a()
        listbox_a.grid(row=1, column=0, padx=10, pady=5)
        update_a = Button(self.win3, text="Update A", bg='#FF8C00', activebackground='#284C79', command=update_a)
        update_a.grid(row=2, column=0, pady=10)

        l_b = Label(self.win3, text="Set B", font=("Arial", 15, "bold"), bg='#002451', fg='#FF8C00')
        l_b.grid(row=0, column=2)
        listbox_b = Listbox(self.win3, font=("Arial", 16), selectmode=EXTENDED, highlightcolor="gold", bg='#284C79', fg='#A9B7C6', selectbackground='#FF8C00',
                            relief=FLAT, yscrollcommand=set())
        update_b()
        listbox_b.grid(row=1, column=2, padx=10, pady=5)
        update_b = Button(self.win3, text="Update B", bg='#FF8C00', activebackground='#284C79', command=update_b)
        update_b.grid(row=2, column=2)

        rel_s_b = Button(self.win3, text="Relation S and R", bg='#FF8C00', activebackground='#284C79', command=self.R_realtion)  # command=self.relations_S
        rel_s_b.grid(row=3, column=1, pady=3)

        # rel_r_b = Button(self.win3, text="Relation R", bg='#FF8C00', activebackground='#284C79', command=self.R_realtion)  # command=self.relations_R
        # rel_r_b.grid(row=3, column=2)

    def window4(self):
        def union():
            un_res = logic_functions.unite(self.R, self.S)
            G = nx.DiGraph()

            color_map = []
            for node1 in list(self.A):
                if node1 in self.A and node1 in self.B:
                    continue
                color_map.append('blue')
            for nod2 in list(self.B):
                if nod2 in self.A and nod2 in self.B:
                    continue
                color_map.append('green')

            G.add_nodes_from(list(self.A))
            G.add_nodes_from(list(self.B))
            G.add_edges_from(un_res)
            pos = nx.circular_layout(G)
            plt.figure().set_facecolor('#FF0000')
            try:
                nx.draw_networkx(G, pos, edges=G.edges(), edge_color="#FF8C00", node_color=color_map, arrowsize=17, font_size=13, width=1.5)
            except:
                print('An error occurred')
                nx.draw_networkx(G, pos, edges=G.edges(), edge_color="#FF8C00", arrowsize=17, font_size=13, width=1.5)
            plt.title('R ∪ S')
            plt.show()

        def inersection():
            in_res = logic_functions.intersect(self.R, self.S)
            print("Result of intersection " + str(in_res))

            color_map = []

            G_I = nx.DiGraph()
            for node1 in list(self.A):
                if node1 in self.A and node1 in self.B:
                    continue
                color_map.append('blue')
            for nod2 in list(self.B):
                if nod2 in self.A and nod2 in self.B:
                    continue
                color_map.append('green')
            G_I.add_nodes_from(list(self.A))
            G_I.add_nodes_from(list(self.B))
            G_I.add_edges_from(in_res)
            pos = nx.circular_layout(G_I)
            plt.figure().set_facecolor('#FFED00')
            try:
                nx.draw_networkx(G_I, pos, edges=G_I.edges(), edge_color="#FF8C00", node_color=color_map, arrowsize=17, cmap=plt.cm.Blues, font_size=13, width=1.5)
            except:
                print('An error occurred')
                nx.draw_networkx(G_I, pos, edges=G_I.edges(), edge_color="#FF8C00", arrowsize=17, cmap=plt.cm.Blues, font_size=13, width=1.5)
            plt.title('R ∩ S')
            plt.show()

        def difference_func():
            diff_res = logic_functions.difference_f(self.R, self.S)
            G_D = nx.DiGraph()
            color_map = []
            for node1 in list(self.A):
                if node1 in self.A and node1 in self.B:
                    continue
                color_map.append('blue')
            for node2 in list(self.B):
                if node2 in self.A and node2 in self.B:
                    continue
                color_map.append('green')
            G_D.add_nodes_from(list(self.A))
            G_D.add_nodes_from(list(self.B))
            G_D.add_edges_from(diff_res)
            pos = nx.circular_layout(G_D)
            plt.figure().set_facecolor('#CF00B5')
            try:
                nx.draw_networkx(G_D, pos, edges=G_D.edges(), edge_color="#FF8C00", node_color=color_map, arrowsize=17, cmap=plt.cm.Blues, font_size=13, width=1.5)
            except:
                print('An error occurred')
                nx.draw_networkx(G_D, pos, edges=G_D.edges(), edge_color="#FF8C00", arrowsize=17, cmap=plt.cm.Blues, font_size=13, width=1.5)
            plt.title('R \ S')
            plt.show()

        def addition():
            a_res = logic_functions.addition(self.R, self.A, self.B)
            G_A = nx.DiGraph()
            color_map = []
            for node1 in list(self.A):
                if node1 in self.A and node1 in self.B:
                    continue
                color_map.append('blue')
            for node2 in list(self.B):
                if node2 in self.A and node2 in self.B:
                    continue
                color_map.append('green')
            G_A.add_nodes_from(list(self.A))
            G_A.add_nodes_from(list(self.B))
            G_A.add_edges_from(a_res)
            pos = nx.circular_layout(G_A)
            plt.figure().set_facecolor('#1BDB00')
            try:
                nx.draw_networkx(G_A, pos, edges=G_A.edges(), edge_color="#FF8C00", node_color=color_map, arrowsize=17, cmap=plt.cm.Blues, font_size=13, width=1.5)
            except:
                print('An error occurred')
                nx.draw_networkx(G_A, pos, edges=G_A.edges(), edge_color="#FF8C00", arrowsize=17, cmap=plt.cm.Blues, font_size=13, width=1.5)
            plt.title("U \ R")
            plt.show()

        def inverse_f():
            in_res = logic_functions.inverse_f(self.S)
            G_i = nx.DiGraph()
            color_map = []
            for node1 in list(self.A):
                if node1 in self.A and node1 in self.B:
                    continue
                color_map.append('blue')
            for node2 in list(self.B):
                if node2 in self.A and node2 in self.B:
                    continue
                color_map.append('green')
            G_i.add_nodes_from(list(self.A))
            G_i.add_nodes_from(list(self.B))
            G_i.add_edges_from(in_res)
            pos = nx.circular_layout(G_i)
            plt.figure().set_facecolor('#00D2F0')
            try:
                nx.draw_networkx(G_i, pos, edges=G_i.edges(), edge_color="#FF8C00", node_color=color_map, arrowsize=17, cmap=plt.cm.Blues, font_size=13, width=1.5)
            except:
                print('An error occurred')
                nx.draw_networkx(G_i, pos, edges=G_i.edges(), edge_color="#FF8C00", arrowsize=17, cmap=plt.cm.Blues, font_size=13, width=1.5)
            plt.title("S⁻¹")
            plt.show()

        self.win4 = Toplevel(root)
        self.win4.title("Windows 4")
        self.win4.configure(background='#002451')
        self.win4.resizable(width=False, height=False)
        main_menu = Menu(self.win4)
        main_menu.add_command(label="Quit", command=lambda: root.quit())
        self.win4.config(menu=main_menu)
        frame1 = Frame(self.win4, bg='#002451')
        frame1.pack(fill=X, pady=10)
        label = Label(frame1, text='  Graphical representation of the relation  ', font=("Arial", 22, "bold"), bg='#002451', fg='#FF8C00')
        label.pack()
        frame2 = Frame(self.win4, bg='#002451')
        frame2.pack(pady=10)
        union_bnt = Button(frame2, text='R ∪ S', bg='#FF0000', activebackground='#284C79', relief=GROOVE, font=("Arial", 15, "bold"), command=union)
        intersection_btn = Button(frame2, text='R ∩ S', bg='#FFED00', activebackground='#284C79', relief=GROOVE, font=("Arial", 15, "bold"), command=inersection)
        difference_bnt = Button(frame2, text='R \ S', bg='#CF00B5', activebackground='#284C79', relief=GROOVE, font=("Arial", 15, "bold"), command=difference_func)
        addition_btn = Button(frame2, text='U \ R', bg='#1BDB00', activebackground='#284C79', relief=GROOVE, font=("Arial", 15, "bold"), command=addition)
        inverse_btn = Button(frame2, text='S⁻¹', bg='#00D2F0', activebackground='#284C79', relief=GROOVE, font=("Arial", 15, "bold"), command=inverse_f)

        union_bnt.grid(padx=10, column=0, pady=10)
        intersection_btn.grid(padx=15, column=1, row=0, pady=10)
        difference_bnt.grid(padx=15, column=2, row=0, pady=10)
        addition_btn.grid(padx=15, column=3, row=0, pady=10)
        inverse_btn.grid(padx=15, column=4, row=0, pady=10)

    def determine_the_variant(self):
        G = 91
        try:
            N = int(self.number_entry.get())
            M = "ІВ"
            print("Моя група: ", M + " -", G)
            print("Мій номер у групі:", N)
            if M == "ІО": N += 1
            var = (N + G % 60) % 30 + 1
            self.variant_label.configure(text=var)
            print("Мій варіант:", var)
        except ValueError:
            pass

    def R_realtion(self):
        plt.close()
        plt.title("Orange line - S\nRed line -  R")
        self.R = relations_R(self.A, self.B, self.list_of_women_names, self.list_of_men_names)
        self.g2 = nx.DiGraph()

        color_map = []
        for node1 in range(len(list(self.A))):
            if node1 in self.A and node1 in self.B:
                continue
            color_map.append('blue')
        for nod2 in list(self.B):
            if nod2 in self.A and nod2 in self.B:
                continue
            color_map.append('green')

        self.g2.add_nodes_from(list(self.A))
        self.g2.add_nodes_from(list(self.B))
        self.g2.add_edges_from(self.R)
        pos = nx.circular_layout(self.g2)
        # plt.figure().set_facecolor('#002451')
        labels_t = {e: "тесть" for e in self.g2.edges()}
        try:
            nx.draw_networkx(self.g2, pos, edges=self.g2.edges(), edge_color="r", node_color=color_map, arrowsize=17, cmap=plt.cm.Blues, font_size=13, width=1.5)
            nx.draw_networkx_edge_labels(self.g2, pos, edge_labels=labels_t, font_size=10, label_pos=0.3, bbox=dict(alpha=0))
        except:
            print('An error occurred')
            nx.draw_networkx(self.g2, pos, edges=self.g2.edges(), edge_color="r", arrowsize=17, cmap=plt.cm.Blues, font_size=13, width=1.5)

        self.S_relation()
        plt.show()
        print(nx.to_numpy_matrix(self.g2, nodelist=self.g2.nodes()))


    def S_relation(self):

        self.S = relations_S(self.A, self.B, self.list_of_men_names, self.R)

        self.g1 = nx.DiGraph()
        color_map = []
        for node1 in list(self.A):
            if node1 in self.A and node1 in self.B:
                continue
            color_map.append('blue')
        for nod2 in list(self.B):
            color_map.append('green')

        self.g1.add_nodes_from(list(self.A))
        self.g1.add_nodes_from(list(self.B))
        self.g1.add_edges_from(self.S)
        pos = nx.circular_layout(self.g1)

        labels_dad = {e: "батько" for e in self.g1.edges()}
        try:
            nx.draw_networkx(self.g1, pos, edges=self.g1.edges(), node_color=color_map, edge_color="#FF8C00", arrowsize=17, font_size=13, width=1.5)
            nx.draw_networkx_edge_labels(self.g1, pos, edge_labels=labels_dad, font_size=10, bbox=dict(alpha=0))
        except:
            print('An error occurred')
            nx.draw_networkx(self.g1, pos, edges=self.g1.edges(), edge_color="#FF8C00", arrowsize=17, font_size=13, width=1.5)


root = Tk()
root.configure(background='#024FBF')
root.resizable(width=False, height=False)
root.title('Main')
program = Window1(root)
root.mainloop()
