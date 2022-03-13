import os.path
import csv

arquivoExiste = os.path.exists('Test.csv')



if arquivoExiste == True:
	with open('Test.csv', 'a', newline='\n') as csvfile:
				fieldnames = ['Vitorias']
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				writer.writerow({'Vitorias': 1000})
else:
	with open('Test.csv', 'w', newline='\n') as csvfile:
				fieldnames = ['Vitorias']
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				writer.writeheader()
				writer.writerow({'Vitorias': 0})
