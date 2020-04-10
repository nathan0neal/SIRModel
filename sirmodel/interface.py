import tkinter as tk
from tkinter import END

master = tk.Tk()
master.geometry("400x200")

# set window color
master.configure(bg='blue')


def retrieve_input():
    N, I, R, beta, gamma = (e1.get(), e2.get(), e3.get(), e4.get(), e5.get())
    print(N, I, R, beta, gamma)


def only_numbers(char):
    if char.isdigit() or char == ".":
        return True
    else:
        return False


tk.Label(master,
         text="Population totale", bg='#54FA9B').grid(row=0)
tk.Label(master,
         text="Infecté", bg='#54FA9B').grid(row=1)
tk.Label(master,
         text="Guéri(s)", bg='#54FA9B').grid(row=2)
tk.Label(master,
         text="Taux de propagation", bg='#54FA9B').grid(row=3)
tk.Label(master,
         text="Taux de guérison", bg='#54FA9B').grid(row=4)

validation = master.register(only_numbers)
e1 = tk.Entry(master, validate="key", validatecommand=(validation, '%S'))
e2 = tk.Entry(master, validate="key", validatecommand=(validation, '%S'))
e3 = tk.Entry(master, validate="key", validatecommand=(validation, '%S'))
e4 = tk.Entry(master, validate="key", validatecommand=(validation, '%S'))
e5 = tk.Entry(master, validate="key", validatecommand=(validation, '%S'))

e1.insert(10, "10000")
e2.insert(10, "1")
e3.insert(10, "0")
e4.insert(10, "2")
e5.insert(10, "1")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)

tk.Button(master,
          text='Quit',
          command=master.quit, highlightbackground='green', fg="white").grid(row=5,
                                                                             column=1,
                                                                             sticky=tk.W,
                                                                             pady=4)
tk.Button(master,
          text='Show', command=lambda: retrieve_input(), bg='green', highlightbackground='green').grid(row=5,
                                                                                                       column=2,
                                                                                                       sticky=tk.W,

                                                                                                       pady=4)

master.mainloop()
tk.mainloop()
#####faire un reset
