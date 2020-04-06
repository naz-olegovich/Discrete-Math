from tkinter import *


def build_incidence_matrix(root, bg, G):
    win_for_in_matrix = Toplevel(root, bg=bg)
    win_for_in_matrix.title("Матриця інцидентності")
    frame_for_label = Frame(win_for_in_matrix, bg=bg)
    frame_for_label.pack(fill=X, pady=10)
    label_inMatrix = Label(frame_for_label, bg="#00035C", fg='#A9B7C6', font=("Times", 19), text="  Матриця інцидентності  ")
    label_inMatrix.pack(fill=X)
    frame_for_inMatrix = Frame(win_for_in_matrix, bg=bg)
    frame_for_inMatrix.pack()

    nodes = list(G.nodes())
    edges_list = list(G.edges())
    nodes.sort()

    for i in range(len(edges_list)):
        l = Label(frame_for_inMatrix, bg=bg, fg='#A9B7C6', text="e" + str(i + 1), font=("Arial", 17))
        l.grid(row=0, column=i + 1, pady=3)
    for i in range(len(nodes)):
        l = Label(frame_for_inMatrix, bg=bg, fg='#A9B7C6', text=nodes[i], font=("Arial", 17))
        l.grid(row=i + 1, column=0, sticky=E)

    for row in range(len(nodes)):
        for column in range(len(edges_list)):
            if edges_list[column][0] == nodes[row] and edges_list[column][1] == nodes[row]:
                l = Label(frame_for_inMatrix, bg=bg, fg='#E8E8E7', text="±1", font=("Arial", 21))
                l.grid(row=row + 1, column=column + 1, padx=3, pady=3)
            elif edges_list[column][0] == nodes[row]:
                l = Label(frame_for_inMatrix, bg=bg, fg='#E8E8E7', text="+1", font=("Arial", 21))
                l.grid(row=row + 1, column=column + 1, padx=3, pady=3)
            elif edges_list[column][1] == nodes[row]:
                l = Label(frame_for_inMatrix, bg=bg, fg='#E8E8E7', text="-1", font=("Arial", 18))
                l.grid(row=row + 1, column=column + 1, padx=3, pady=3)
            else:
                l = Label(frame_for_inMatrix, bg=bg, fg='#E8E8E7', text="0", font=("Arial", 18))
                l.grid(row=row + 1, column=column + 1, padx=3, pady=3)
