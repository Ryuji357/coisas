import csv, os

from os import listdir
from os.path import isfile, join
from dotenv import load_dotenv

load_dotenv()

caminho = os.getenv('CAMINHO')

type0_arq = open(join(caminho, 'final_type0.txt'), 'w+', newline='')
type1_arq = open(join(caminho, 'final_type1.txt'), 'w+', newline='')

type0 = csv.writer(
    type0_arq,
    delimiter=';'
)

type1 = csv.writer(
    type1_arq,
    delimiter=';'
)

for f in listdir(caminho):
    if isfile(join(caminho, f)):
        with open(
            join(caminho, f),
            encoding="latin-1"
        ) as csvfile:
            spamreader = csv.reader(csvfile, delimiter='|')
            for x in spamreader:
                if x[1] == 'C100':
                    if x[2] == '0':
                        type0.writerow([x[9]])
                    elif x[2] == '1':
                        type1.writerow([x[9]])
                # Detecta a ultima linnha antes da assinatura.
                if x[1] == '9999':
                    break

type0_arq.close()
type1_arq.close()

'''
arquivo = csv.writer(
    open(join(caminho, 'final.txt')),
    delimiter='',
    quotechar='',
    quoting=csv.QUOTE_MINIMAL
)

for f in listdir(caminho):
    if isfile(join(caminho, f)):
        with open(join(caminho, f), newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter='|', quotechar='')
            for x in spamreader:
                prin(x)
'''
