import json

with open('response.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)
# Lê o arquivo JSON (substitua pelo caminho do seu arquivo)
#print(dados['data']['data'])

# Acessa os itens na lista
itens = dados['data']['data']

# Usa um set para guardar descrições únicas
descricoes_unicas = set()

for item in itens:
    descricao = item.get('descricao')
    if descricao:  # Ignora valores nulos ou vazios
        descricoes_unicas.add(descricao)


print(descricoes_unicas.s)

# Exibe as descrições únicas
for desc in sorted(descricoes_unicas):
    print(desc)
