"""
List Comprehension

- Nos permite gerar listas com dados processados a partir de
um iterável;
- Simplifica operações sem a necessidade de se criar funções para tal;
- Opera sobre iteráveis sem a necessidade de loops;

# Sintaxe
[dado for dado in iterável]

"""

"""
Exemplos 
"""
numeros = [1,2,3,4,5] #Lista (um tipo de iterável)

comp = [num + 5 for num in numeros] #Comprehension criada com a lista
print(comp)

# É possível trabalhar com comprehensions em strings
nome = 'João Vítor'
nome_m = [str.upper() for str in nome]
print(nome_m)