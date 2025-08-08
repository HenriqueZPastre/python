import csv

chaves = []

with (open('nfg.csv', newline='')) as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		chaves.append(row['Chave de Acesso'].replace(" ",""))

write_file = open('chaves.json', 'w')
write_file.write('[\n')
for i, chave in enumerate(chaves):
	if i > 0:
		write_file.write(',\n')
	write_file.write(f'"{chave}"')
write_file.write('\n]')
write_file.close()