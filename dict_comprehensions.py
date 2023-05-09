"""
Dictionary Comprehensions

Sintaxe:
{chave: valor for valor in iterável}

Obs: 
    - não é possível iterar sobre o dicionário diretamente, é preciso extrair
    um iterável de seus itens (no caso, uma tupla) por meio do método .items();
    - as chaves do comprehension serão as mesmas que as do dicionário.

"""
#Exemplos

dict = {'a':1,'b':2,'c':3,'d':4}
dict_comp = {chave:valor + 5 for chave,valor in dict.items()}
print(dict_comp)

#Criando dicionário a partir de lista
num = [1,2,3,4,5]
dict_comp_2 = {val:pow(val,2) for val in num}
print(dict_comp_2)

#Utilizando chaves de string
chave = 'abcde'
dict_comp_3 = {chave[i]:num[i] for i in range(0,len(chave))}
print(dict_comp_3)

#Utilizando condicionais
dict_comp_4 = {val:('par' if val % 2 == 0 else 'ímpar') for val in num}
print(dict_comp_4)