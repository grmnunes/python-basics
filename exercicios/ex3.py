from matematica.operacoes import soma

num1 = input('Digite o 1° número.: ')
num2 = input('Digite o 2° número.: ')

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    print(soma(num1, num2))
else:
    print('Apenas valores numericos são aceitos.')