import json

def readJson(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def printarChaves(chaves):
	for chave in chaves:
		print(f"Consultando chave: {chave}")
	
#consultarChaves(chaves)