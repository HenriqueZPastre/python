import csv

def read_csv(filename):
	chaves = []
	with (open(filename, newline='')) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			chaves.append(row['Chave de Acesso'].replace(" ",""))
	return chaves

def write_json(filename, chavesArray):
	write_file = open(filename, 'w')
	write_file.write('[\n')
	for i, chavesArray in enumerate(chavesArray):
		if i > 0:
			write_file.write(',\n')
		write_file.write(f'"{chavesArray}"')
	write_file.write('\n]')
	write_file.close()

chaves = read_csv('PyNFE/nfg.csv')
write_json('pyNFE/chaves.json', chaves)