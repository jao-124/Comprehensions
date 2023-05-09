"""
Continuação - List Comprehension

- É possível associar estruturas condicionais às comprehensions;  
"""
# Exemplos
numeros = [1,2,3,4,5]

n_imp = [num for num in numeros if num % 2 != 0] #Lista com os elementos ímpares do iterável
print(n_imp)
