import numpy as np

# Listas comuns do Python (matrizes 2x2)
lista_a = [[1, 2], [3, 4]]
lista_b = [[5, 6], [7, 8]]

# Convertendo e multiplicando com o operador @
matriz_a = np.array(lista_a)
matriz_b = np.array(lista_b)
resultado = matriz_a @ matriz_b

print(resultado)
# Saída: [[19, 22], [43, 50]]