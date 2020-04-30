import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt



    # Partie modifiable, données à adapter


# Population totale (à adapter)
N = 1000

# Nombre initial d'individus rétablis (en général 0)
R0 = 0

# Nombre initial d'individus infectés
I0 = 1

# Nombre d'individus susceptibles d'êtres atteints : tous les autres
S0 = N - I0 - R0

# beta = Taux de transmission à chaque contact (ne pas confondre avec R0)
beta = 0.3


# dret = Durée de rétablissement : avant de plus être contaminant (jours)
dret = 17

# gamma = Inverse de la durée de rétablissement (jour^(-1)) (temps moyen contaminant)
gamma = 1/dret

# t = Un échantillon de temps sur lequel on réalise la simulation (jours)
t = np.linspace(0, 160, 160)



    # Partie non modifiable, équations du modèle


# Conditions initiales sous forme d'un vecteur
y0 = S0, I0, R0

# Equations différentielles du modèle SIR
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -(beta/N)*S*I
    dIdt = (beta/N)*S*I/ - gamma*I
    dRdt = gamma*I
    return dSdt, dIdt, dRdt

# On intègre les équations différentielles sur une échelle de temps t avec
# conditions initiales yo. Les équa diff doivent être données comme des
# fonctions que l'on peut appeler, args sont les autres arguments pris par deriv
ret = odeint(deriv, y0, t, args=(N, beta, gamma))

# ret est une matrice de taille (len(t), len(yo)) donc on a S, I, R qui sont
# les trois colonnes de T : on les récupère en prenant la transposé de ret
S, I, R = ret.T



    # Affichage graphique du résultat obtenu


fig = plt.figure(facecolor='w')
#plt.subplot(211)
#ax = fig.add_subplot(111, axis_bgcolor='#dddddd', axisbelow=True)
plt.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
plt.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
plt.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
plt.xlabel('Time /days')
plt.ylabel('Number')
#plt.ylim(0,1.2)
plt.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = plt.legend()
legend.get_frame().set_alpha(0.5)
#for spine in ('top', 'right', 'bottom', 'left'):
#plt.spines[spine].set_visible(False)
plt.show()