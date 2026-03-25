from tkinter import *
window = Tk()
for i in range(4):
    for j in range(4):
        frame = Frame(master = window, relief = "raised", borderwidth=5)
        frame.grid(row=i,column=j,padx = 5, pady = 5)
        label = Label(master = frame, text = f"Row {i}\n Column {j}")
        label.pack()

window.mainloop()