"""
Listas aninhadas

- Arrays são estruturas apresentadas por algumas linguagens de programação.
Não é o caso do Python.

- No Python, esse tipo de estrutura é emulado pelas listas.
 
- Ao contrário dos arrays, as listas podem apresentar dados de tipos diferente.
Podemos ter, em uma mesma lista, dados do tipo char e inteiros.

- Listas aninhadas são estruturas multidimensionais em Python, semelhantes aos
vetores em C, por exemplo. Nada mais são que listas dentro de listas.
"""

#Exemplo

list_an = [[1,2,3],[4,5,6],[7,8,9]]
"""
print(list_an)
print(list_an[1][2])
"""

#Utilizando list comprehension
[[print(num) for num in lista] for lista in list_an]

#Gerando uma matriz 3x3
table = [[col for col in range(1,4)] for lin in range(1,4)]

#Tabuleiro jogo da velha
velha = [['X' if col % 2 == 0 else'O' for col in range(1,4)] for lin in range(1,4)]
print(velha)