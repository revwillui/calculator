import tkinter as tk

window= tk.Tk()
window.title("Calculator")

window.rowconfigure([0,1,2,3,4,5], minsize=50, weight=1)
window.columnconfigure([0,1,2,3], minsize=50, weight=1)

Entry1 = tk.Entry(master = window, width = 10, font = ('Arial 16'))
Entry1.insert(0,"25 + 5")
Entry1.grid(row= 0, columnspan= 3 ,sticky = "nsew")

Entry12 = tk.Entry(master = window, width = 10, font = ('Arial 16'))
Entry12.insert(0,"5")
Entry12.grid(row= 1, columnspan= 3 ,sticky = "nsew")

b1 = tk.Button(master = window, text = "7",font = ('Arial 16'))
b1.grid(row = 2, column = 0,sticky = "nsew")

b2 = tk.Button(master = window, text = "8",font = ('Arial 16'))
b2.grid(row = 2, column = 1,sticky = "nsew")

b3 = tk.Button(master = window, text = "9",font = ('Arial 16'))
b3.grid(row = 2, column = 2,sticky = "nsew")

b4 = tk.Button(master = window, text = "*",font = ('Arial 16'))
b4.grid(row = 2, column = 3,sticky = "nsew")

b5 = tk.Button(master = window, text = "4",font = ('Arial 16'))
b5.grid(row = 3, column = 0,sticky = "nsew")

b6 = tk.Button(master = window, text = "5",font = ('Arial 16'))
b6.grid(row = 3, column = 1,sticky = "nsew")

b7 = tk.Button(master = window, text = "6",font = ('Arial 16'))
b7.grid(row = 3, column = 2,sticky = "nsew")

b8 = tk.Button(master = window, text = "/",font = ('Arial 16'))
b8.grid(row = 3, column = 3,sticky = "nsew")

b9 = tk.Button(master = window, text = "1",font = ('Arial 16'))
b9.grid(row = 4, column = 0,sticky = "nsew")

b10 = tk.Button(master = window, text = "2",font = ('Arial 16'))
b10.grid(row = 4, column = 1,sticky = "nsew")

b11 = tk.Button(master = window, text = "3",font = ('Arial 16'))
b11.grid(row = 4, column = 2,sticky = "nsew")

b12 = tk.Button(master = window, text = "-",font = ('Arial 16'))
b12.grid(row = 4, column = 3,sticky = "nsew")

b13 = tk.Button(master = window, text = "c",font = ('Arial 16'))
b13.grid(row = 5, column = 0,sticky = "nsew")

b14 = tk.Button(master = window, text = "0",font = ('Arial 16'))
b14.grid(row = 5, column = 1,sticky = "nsew")

b15 = tk.Button(master = window, text = "=",font = ('Arial 16'))
b15.grid(row = 5, column = 2,sticky = "nsew")

b16 = tk.Button(master = window, text = "+",font = ('Arial 16'))
b16.grid(row = 5, column = 3,sticky = "nsew")
window.mainloop()
