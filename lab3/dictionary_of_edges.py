from tkinter import *


def show_dictionary_of_edges(root, bg, G):
    win_for_edges = Toplevel(root, bg=bg)
    win_for_edges.title("Словник ребер")
    frame_for_label = Frame(win_for_edges, bg=bg)
    frame_for_label.pack(fill=X)
    label_edges = Label(frame_for_label, bg="#00035C", fg='#A9B7C6', font=("Times", 19), text="  Словник ребер  ")
    label_edges.pack(fill=X)
    frame_for_edges = Frame(win_for_edges, bg=bg)
    frame_for_edges.pack()

    listbox = Listbox(frame_for_edges, font=("Arial", 17), selectmode=EXTENDED, highlightcolor="gold", bg='#284C79', fg='#A9B7C6', selectbackground='#FF8C00',
                      relief=FLAT, justify=CENTER, yscrollcommand=set())
    listbox.pack(side=LEFT)

    scrollbar = Scrollbar(frame_for_edges, orient="vertical")
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox.config(yscrollcommand=scrollbar.set)

    listbox.delete(0, END)
    for i in list(G.edges()):
        listbox.insert(END, str(i))
