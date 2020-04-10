import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from pylab import *

N = 10000  # population totale
I = 1  # Nombre de cas infecte 1er jour
R = 0  # 0 gueris
S = N - I - R  # Susceptible (N=S+I+R)

beta = 5.5  # infection
gamma = .5  # rate de soin

temps = 20  # nb de jours


def SIR(vals, t, b, g):
    S, I, R = vals

    dS = -b * S * I / N  # dS/dt
    dI = b * S * I / N - g * I
    dR = g * I

    return [dS, dI, dR]


x = np.linspace(0, temps, 1000)
x1 = [S, I, R]  #paraminitiaux
rates = (beta, gamma) #les taux
sol = odeint(SIR, x1, x, args=rates)

# Solutions des EDO
plt.plot(x, sol[:, 0])
plt.plot(x, sol[:, 1])
plt.plot(x, sol[:, 2])

plt.xlabel('Temps')
plt.ylabel('Population')
plt.legend(['S', 'I', 'R'], shadow=True)
plt.title('COVID19')
plt.show()
#savefig("/bouret/Documents/" + "parambeta " + str(beta) + "paramgamma " + str(gamma) + ".png", dpi=400)