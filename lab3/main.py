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
    bg = '#002451'
    fr_bg = '#024FBF'
    fg = '#A9B7C6'
    def __init__(self, main):
        self.main = root

        # menu
        main_menu = Menu(root)
        elements_of_menu = Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="Windows", menu=elements_of_menu)
        elements_of_menu.add_command(label="Window 2", command=self.window2)
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
        number_in_list_label = Label(frame_for_variant, fg='#A9B7C6', font=("Ubuntu", 15), text="Номер у списку: 28\nНомер залікової книжки: 9130", bg='#002451')
        number_in_list_label.grid(row=0, column=0)


        # separated frame for button 'Variant' and label
        frame_for_variant2 = Frame(text_frame, bg='#002451')
        frame_for_variant2.pack()
        variant_button = Button(frame_for_variant2, bg='#002451', fg='#A9B7C6', text='Variant', relief=GROOVE, padx=8, pady=2, activebackground='#284C79',
                                command=self.determine_the_variant)
        variant_button.grid(row=0, column=0)
        self.variant_label = Label(frame_for_variant2, font=30, bg='#002451', fg='#A9B7C6')
        self.variant_label.grid(row=0, column=1)


    def window2(self):
        def switch(event):
            if event.widget.get() == "0":
                event.widget.delete(0, END)
                event.widget.insert(END, "1")
            else:
                event.widget.delete(0, END)
                event.widget.insert(END, "0")

        def build_graph():
            plt.close()
            plt.title("Матриця суміжності")
            edges = list()
            node_list1 = list()
            node_list2 = list()
            for i in list_of_entries:
                for j in i:
                    if j.get() == "1":
                        index1 = list_of_entries.index(i)+1
                        index2 = i.index(j) + 1
                        edges.append([index1, index2])
                        node_list1.append(index1)
                        node_list2.append(index2)
            G = nx.DiGraph()
            pos = nx.spring_layout(G)
            G.add_edges_from(edges)
            # nx.draw_networkx_nodes(G, pos, nodelist=node_list1,node_color='r')
            # nx.draw_networkx_nodes(G, pos, nodelist=node_list2,node_color='b')
            color_map = []
            for i in G.nodes():
                if i in node_list1:
                    color_map.append("blue")
                else:
                    color_map.append("red")

            print(edges)


            nx.draw_networkx(G, node_color=color_map,arrowsize=13, font_size=13, width=1.3)
            plt.show()



        win2 = Toplevel(root, bg=self.bg)
        win2.title("Матриця суміжності")
        frame1 = Frame(win2, bg="#000059")
        frame1.pack(fill=X, pady=5)
        header5 = Label(frame1, bg="#00035C", fg='#A9B7C6', font=("Times", 19), text="Матриця суміжності")
        header5.pack(fill=X)

        frame2 = Frame(win2, bg=self.bg)
        frame2.pack()




        for i in range(10):
            l = Label(frame2, bg=self.bg, fg=self.fg, text=i + 1, font=("Arial", 21))
            l.grid(row=0, column=i + 1)
        for i in range(10):
            l = Label(frame2, bg=self.bg, fg=self.fg, text=i + 1, font=("Arial", 21))
            l.grid(row=i + 1, column=0, sticky=E)

        list_of_entries = list()
        for row in range(10):
            list_of_entries.append([])
            for column in range(10):
                entry = Entry(frame2,  bg="#00387F", fg='#E8E8E7', width=3, font=("", 21), bd=3, justify=CENTER, relief=FLAT)
                entry.grid(row=row+1, column=column+1)
                entry.insert(END, "0")
                entry.bind('<Button-1>', switch)
                list_of_entries[row].append(entry)
        frame3 = Frame(win2, bg=self.bg)
        frame3.pack()

        b_build_graph = Button(win2, width=17, text="Build Graph", font=("Arial", 12), bg='#FF8C00', activebackground='#284C79', relief=GROOVE, command=build_graph)
        b_build_graph.pack(pady=10)










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
