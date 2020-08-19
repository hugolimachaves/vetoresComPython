#Como fazer um gráfico (plot) em python de soma de vetores!

#segue o passo-a-passo:

import matplotlib.pyplot as plt  #matplotlib  --> bibliteca para fazer gráficos
import numpy as np 				 #numpy       --> bibliteca para fazer calculos com vetores

vetor_1 = np.array([0.1,0.2])     #declaração de vetores (x1,y1)
vetor_2 = np.array([0.5,0.1])     #declaração de vetores (x2,y2)
vetor_soma = vetor_1 + vetor_2    #soma do vetores
print("O vetor_1 é: ", vetor_1)	  #impressão do vetor_1
print("O vetor_2 é: ", vetor_2)   #impressão do vetor_2
print("A soma dos vetores é: ", vetor_soma) #impressão do vetor resultante

ax = plt.axes()
ax.arrow(0			, 0			, vetor_1[0]	, vetor_1[1]	, head_width=0.02, head_length=0.01, fc='b', ec='olive') # linha para desenhar a 'seta' do vetor 1
ax.arrow(vetor_1[0] , vetor_1[1], vetor_2[0]	, vetor_2[1]	, head_width=0.02, head_length=0.01, fc='r', ec='aqua') # linha para desenhar a 'seta' do vetor 2
ax.arrow(0			, 0			, vetor_soma[0]	, vetor_soma[1]	, head_width=0.02, head_length=0.01, fc='c', ec='tomato') # linha para desenhar a 'seta' do vetor soma

#ax.arrow(	posição inicial em x,        \
# 			posição inicial em y,        \
# 			posicao final em x,          \
# 			posicao final em y           \
# 			espessura da ponda da seta   \
# 			comprimento da ponta da seta \
# 			cor	da ponta da seta         \
# 			cor da seta                  \
# )

plt.axis([-1, 1, -1, 1])  #definindo os limites do gráfico a ser desenhado (plotado)
plt.grid( linestyle='-', linewidth=1)  #definir o grid (tela)
plt.show() # comando final para desenhar na tela (plotar)
C:\Users\Hugo\Documents\ifFast\vetor1.py
#propostas

# 1) Trocar os vetores (coordenadas)
# 2) Trocas as cores dos vetores
# desafio: Multiplicar UM vetor qualquer por 2
	# a) Como multiplicar um vetor por 2? Matemática
	# b) Como multiplicar um vetor por 2 com python? Resultado 
	# c) Como que eu plot esse vetor multiplicado?  Gráfico

#Como fazer um gráfico (plot) em python de soma de vetores!

#segue o passo-a-passo:

import matplotlib.pyplot as plt  #matplotlib  --> bibliteca para fazer gráficos
import numpy as np 				 #numpy       --> bibliteca para fazer calculos com vetores

vetor_1 = np.array([0.1,0.2])     #declaração de vetores (x1,y1)
vetor_2 = np.array([0.5,0.1])     #declaração de vetores (x2,y2)
vetor_soma = vetor_1 + vetor_2    #soma do vetores
print("O vetor_1 é: ", vetor_1)	  #impressão do vetor_1
print("O vetor_2 é: ", vetor_2)   #impressão do vetor_2
print("A soma dos vetores é: ", vetor_soma) #impressão do vetor resultante

ax = plt.axes()
ax.arrow(0			, 0			, vetor_1[0]	, vetor_1[1]	, head_width=0.02, head_length=0.01, fc='b', ec='olive') # linha para desenhar a 'seta' do vetor 1
ax.arrow(vetor_1[0] , vetor_1[1], vetor_2[0]	, vetor_2[1]	, head_width=0.02, head_length=0.01, fc='r', ec='aqua') # linha para desenhar a 'seta' do vetor 2
ax.arrow(0			, 0			, vetor_soma[0]	, vetor_soma[1]	, head_width=0.02, head_length=0.01, fc='c', ec='tomato') # linha para desenhar a 'seta' do vetor soma

#ax.arrow(	posição inicial em x,        \
# 			posição inicial em y,        \
# 			posicao final em x,          \
# 			posicao final em y           \
# 			espessura da ponda da seta   \
# 			comprimento da ponta da seta \
# 			cor	da ponta da seta         \
# 			cor da seta                  \
# )

plt.axis([-1, 1, -1, 1])  #definindo os limites do gráfico a ser desenhado (plotado)
plt.grid( linestyle='-', linewidth=1)  #definir o grid (tela)
plt.show() # comando final para desenhar na tela (plotar)
C:\Users\Hugo\Documents\ifFast\vetor1.py
#propostas

# 1) Trocar os vetores (coordenadas)
# 2) Trocas as cores dos vetores
# desafio: Multiplicar UM vetor qualquer por 2
	# a) Como multiplicar um vetor por 2? Matemática
	# b) Como multiplicar um vetor por 2 com python? Resultado 
	# c) Como que eu plot esse vetor multiplicado?  Gráfico

