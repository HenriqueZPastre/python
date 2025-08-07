nome = "Henrique"
idade = 25
array = [1, 2, 3, 4, 5]
print('Nome: %s, Idade: %d' % (nome, idade))
print('Nome: {}, Idade: {}'.format(nome.upper(), idade))
print(f'Nome: {nome}, Idade: {idade}')
print(f'Nome: {nome[:-1].lower() + nome[-1].upper()}, Idade: {idade}')

print('%-05d' %idade)
print('%05d' %idade)
print('%5d' %idade)

print('R$%f' % 1234.5678)
print('R$%.2f' % 1234.5678)

print('%-12s' % nome)


print(nome[1:4])
print('remove primeiro: ',nome[1:])
print('remove o ultimo: ',nome[:-1])
print('somente o primeiro: ',nome[0])
print('pega somene o que esta abaixo: ',nome[:3])
print('pega o ultimo: ',nome[-1])
print('pega os ultimo: ',nome[-2:])
#print("ri" in nome)
array.clear()
print(array)
