 # O * diz que há um numero indeterminado de parametros *args
def soma(*values):
  total = 0
  for valor in values:
    total += valor
  return total

print(soma(1, 4, 10, 16))

# O ** diz que há um numero indeterminado de parametros nomeados **kwargs
