from scipy.integrate import odeint
from pylab import *
import tkinter as tk
'@author:nathan bouret'

################################################################ interface
master = tk.Tk()
master.geometry("400x200")

# set window color
master.configure(bg='blue')


def retrieve_input():
    N, I, R, beta, gamma = (e1.get(), e2.get(), e3.get(), e4.get(), e5.get())
    ####################################################################

    N = float(N)  # population totale
    I = float(I)  # Nombre de cas infecte 1er jour
    R = float(R)  # 0 gueris
    S = N - I - R
    S = float(S)  # Susceptible (N=S+I+R)
    print(N, I, R, beta, gamma)
    beta = float(beta)  # infection
    gamma = float(gamma)  # rate de soin

    temps = 20  # nb de jours

    def SIR(vals, t, b, g):
        S, I, R = vals
        dS = -b * S * I / N  # dS/dt
        dI = b * S * I / N - g * I
        dR = g * I

        return [dS, dI, dR]

    x = np.linspace(0, temps, 1000)
    x1 = [S, I, R]  # paraminitiaux
    rates = (beta, gamma)  # les taux
    sol = odeint(SIR, x1, x, args=rates)

    # Solutions des ODEs
    plt.plot(x, sol[:, 0])
    plt.plot(x, sol[:, 1])
    plt.plot(x, sol[:, 2])

    plt.xlabel('Temps')
    plt.ylabel('Population')
    plt.legend(['S', 'I', 'R'], shadow=True)
    plt.title('COVID19')
    plt.show()
    # savefig("/bouret/Documents/" + "parambeta " + str(beta) + "paramgamma " + str(gamma) + ".png", dpi=400)

    ############################################################################################################
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
          command=master.quit).grid(row=5,
                                    column=1,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Show', command=lambda: retrieve_input()).grid(row=5,
                                                              column=2,
                                                              sticky=tk.W,

                                                              pady=4)

master.mainloop()
tk.mainloop()
