idiomas = {'br': 'Português', 'eua': 'Ingês'}
#print(idiomas['c']) #Acontece um erro se for passada uma chave que não existe
print(idiomas.get('c')) # Retorna None caso não encontre a chave passad
print(idiomas.get('c', 'País não encontrado'))
print('br' in idiomas)

for pais in idiomas.keys():
  print(pais)

for idioma in idiomas.values():
  print(idioma)

for item in idiomas.items():
  print(item)