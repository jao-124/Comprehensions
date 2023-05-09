"""
Set Comprehension

- Um set, ou conjunto, é um tipo de estrutura com mais restrições que as demais.
Lista = [1,2,3,4,5]
Set = {1,2,3,4,5}

- Observações:
    - Sets não possuem valores duplicados;
    - Sets não têm ordenação;
    - Elementos não são acessados via índice, ou seja, sets não são indexados;
"""
#Exemplos
numeros = {num for num in set([1,1,2,3,4,5,5,6,7])}
print(numeros)

nome = 'João Vítor'
exp = {let for let in nome}
print(exp)