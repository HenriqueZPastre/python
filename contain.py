lista = [10,15,20]
conatin = (12 in lista) or (123 in lista) or (10 in lista)
print('contain',conatin)

for i in lista:
    if i == 134:
        print('10 esta na lista')
        break
else:
	print('10 nao esta na lista')	
 
# Range com salto
for t in range(3,34,3):
	print(t, end=" ")
print()

l = list(range(0,100,10))
print(l)

for x, i in enumerate(l):
	print(x, i, end=",")
 
max= max(l)
print(f'\nO maior valor da lista é: {max}')