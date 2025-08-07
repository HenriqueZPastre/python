produtos = ["Banana"]

""" while True:
    produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")
    if produto.lower() == 'sair':
        break
    produtos.append(produto)
print(produtos) """

for p in produtos:
	for i in p:
		print(i, end=",")