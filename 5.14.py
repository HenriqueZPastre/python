soma = 0
numeros = []
while True:
    valor = int(input("Digite um valor (0 para sair): "))
    if valor == 0:
        break
    numeros.append(valor)
    soma += valor
if numeros:
    print(f'A media é {soma/len(numeros):.2f}')
    print("A quantidade de valores digitados é: ", len(numeros))
else:
    print('Nenhum valor foi digitado.')
    
    