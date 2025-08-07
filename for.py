""" lista = [10,5,8]
soma = 0
for i in lista:
    soma += i
print(f'Média: {(soma / len(lista)):.2f}')
print ('Média %.2f' %(soma / len(lista)))
print(soma)  """

def funcao():
    for i in range(11):
        print(i)
        if i == 55:
            return 'Encerrou o loop'
        
a = funcao()
print(a)
print(a == True)

