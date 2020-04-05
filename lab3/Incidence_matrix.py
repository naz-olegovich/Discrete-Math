from tkinter import *
def build_incidence_matrix(root,bg,G):
    win_for_in_matrix = Toplevel(root, bg=bg)
    frame_for_label = Frame(win_for_in_matrix)
    frame_for_label.pack(pady=5)
    label_inMatrix = Label(frame_for_label, bg="#00035C", fg='#A9B7C6', font=("Times", 19), text="Матриця суміжності")
    label_inMatrix.pack()
    frame_for_inMatrix = Frame(win_for_in_matrix, bg=bg)
    frame_for_inMatrix.pack()

    nodes = list(G.nodes())
    edges_list = list(G.edges())

    for i in range(len(edges_list)):
        l = Label(frame_for_inMatrix, bg=bg, fg="aqua", text="e" + str(i + 1), font=("Arial", 12))
        l.grid(row=0, column=i + 1)
    for i in range(len(nodes)):
        l = Label(frame_for_inMatrix, bg=bg, fg="aqua", text=nodes[i], font=("Arial", 12))
        l.grid(row=i + 1, column=0, sticky=E)

        #, , , width = 3, font = ("", 21), bd = 3, justify = CENTER, relief = FLAT

    for row in range(len(nodes)):
        for column in range(len(edges_list)):
            if edges_list[column][0] == nodes[row] and edges_list[column][1] == nodes[row]:
                l = Label(frame_for_inMatrix,bg = bg, fg = '#E8E8E7', text="±1", font=("Arial", 18))
                l.grid(row=row + 1, column=column + 1,padx=3,pady=3)
            elif edges_list[column][0] == nodes[row]:
                l = Label(frame_for_inMatrix, bg = bg, fg = '#E8E8E7', text="+1", font=("Arial", 18))
                l.grid(row=row + 1, column=column + 1,padx=3,pady=3)
            elif edges_list[column][1] == nodes[row]:
                l = Label(frame_for_inMatrix, bg = bg, fg = '#E8E8E7', text="-1", font=("Arial", 18))
                l.grid(row=row + 1, column=column + 1,padx=3,pady=3)
            else:
                l = Label(frame_for_inMatrix, bg = bg, fg = '#E8E8E7', text="0", font=("Arial", 18))
                l.grid(row=row + 1, column=column + 1,padx=3,pady=3)
