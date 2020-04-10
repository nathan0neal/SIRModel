import numpy as np
import matplotlib.pyplot as plt
'@author:nathan bouret'

CH = np.genfromtxt("germanyrawdata.csv", delimiter=";", skip_header=1)
for i in range(CH.__len__() - 1, -1, -1):
    CH[i, 0] = CH.__len__() - (i + 1)
# print(CH)
A = CH[:50, 0]
B = CH[:50, 1]  # nb de malade
C = CH[:50, 2]  # nb de mort
Soin = CH[:50, 4]
D = CH[:, 3]
plt.plot(A, B)
plt.show()

plt.plot(A, C)
plt.xlabel("jour depuis 1er cas")
plt.show()

plt.plot(A, B, color="green")
plt.plot(A, C, color="purple")
plt.show()

NBMalCUM = np.flip(np.flip(B).cumsum())
# on defini un exposed theo en choisissant Ro autour de 2
Expo = 2*NBMalCUM
plt.plot(A, NBMalCUM, color="red")
plt.show()

NBMort = np.flip(np.flip(C).cumsum())
plt.plot(A, NBMort, color="green")
plt.ylabel('Mort Sa Mere')
plt.show()

plt.plot(A, B, color="green")
plt.plot(A, NBMort, color="purple")
plt.show()

plt.plot(A, NBMort, color="green")
plt.plot(A, Expo, color="yellow")
plt.plot(A, Soin, color="black")
plt.plot(A, NBMalCUM, color="blue")
plt.xlabel('Time /days')
plt.ylabel('Population')
legend = plt.legend()
legend.get_frame().set_alpha(0.5)
plt.show()

# mort cumulé
# plt.plot(CH,[0,1])
# plt.show()
