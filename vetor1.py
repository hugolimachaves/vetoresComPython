import matplotlib.pyplot as plt
import numpy as np 


vetor_1 = np.array([0.1,0.2])
vetor_2 = np.array([0.5,0.1])

vetor_soma = vetor_1 + vetor_2


print(vetor_soma)



ax = plt.axes()
ax.arrow(0, 0, vetor_1[0],\
 			vetor_1[1], head_width=0.02, head_length=0.01, fc='b', ec='k')
ax.arrow(vetor_1[0], vetor_1[1], vetor_2[0], vetor_2[1], head_width=0.02, head_length=0.01, fc='r', ec='g')
ax.arrow(0, 0, vetor_soma[0], vetor_soma[1], head_width=0.02, head_length=0.01, fc='c', ec='m')


#ax.arrow(posição inicial em x,)

plt.show()

