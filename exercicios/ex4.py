total = 0.0
media = 0.0

for i in range(1, 5):
    valor = input(f'Digite o valor da {i}° nota.: ')

    if isinstance(float(valor), float):
        total += float(valor)
    else:
        print('Apenas valores numericos são permitidos!')
        break
    
media = total/4
print(f' A média é: {"{:.2f}".format(media)}')