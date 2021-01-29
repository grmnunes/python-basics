
#LISTAS

lista = [1, 2, 3]
print(lista)

lista = list(range(10))
print(lista)

lista = list(range(20, 0, -5))
print(lista)

full_name = 'Germano Nunes da Silva'
full_name = full_name.split() #É possivel explicitar o caracter separador .split('-')

print(full_name)

full_name = ' '.join(full_name)
print(full_name)

#TUPLAS
#São parecidas com as listas, mas são definidas com () e são imutávies.

tupla = (4, 6, 8)
print(tupla)

tupla = (4,) # tupla com apenas um caracter devem conter uma virgula no final.

# desempacotar uma tupla
tupla = ('Germano', 29)

nome, idade = tupla
print(f'Olá, meu nome é {nome} e eu tenho {idade} anos.')


# Essas operações servem para todas as sequencias strings, listas e tuplas
nome = 'Germano'
print(nome[2])
print(nome[len(nome) -1])
print(nome[-1])
print(nome[0:3])
print(nome[2:])
print(nome[::-1])