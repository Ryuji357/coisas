import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import csv, os
from os import listdir
from os.path import isfile, join

class nota:
    versao = '' # Versão do XML da nota
    suporte = False # Mostra se a versão da nota foi testada
    xmlns = ''

    # Função para adicionar o namespace na tag
    item = lambda self, x: '{}{}'.format(self.xmlns, x)

    ind = {
        'nome': 'xNome',
    }

    def __init__(self, caminho):
        # self.arquivo = ET.parse(caminho)
        self.arvore = ET.parse(caminho).getroot()
        self.versao = self.arvore.attrib['versao']
        self.xmlns = self.arvore.tag[:-7]
        self.arquivo = caminho

        # Verifica a versão do XML, não impede de rodar o modulo
        if self.versao in ['4.00']:
            self.suporte = True
        else:
            self.suporte = False
            print('AVISO: A versão "{}" não é suportada.'.format(self.versao))

    def cam_find(self, lista):
        result = self.arvore
        for x in lista:
            result = result.find(self.item(x))
        return result

    def dest(self, campo = 'nome'):
        return self.cam_find(['NFe', 'infNFe', 'dest', self.ind[campo]]).text

    def emit(self, campo = 'nome'):
        return self.cam_find(['NFe', 'infNFe', 'emit', self.ind[campo]]).text

    def produtos(self):
        result = dict()
        itens = self.cam_find(['NFe', 'infNFe']).findall(self.item('det'))
        for x in itens:
            produto = x.find(self.item('prod'))
            imposto = x.find(self.item('imposto'))
            result = {
                'codigo': produto.find(self.item('cProd')).text,
                'descricao': produto.find(self.item('xProd')).text,
                'ncm': produto.find(self.item('NCM')).text,
                'cest': produto.find(self.item('NCM')).text,
                'cfop': produto.find(self.item('CFOP')).text,
                'quantidade': produto.find(self.item('qCom')).text,
                'valor': produto.find(self.item('vProd')).text,
                'imposto':{
                    'icms': self.get_icms(imposto),
                    'ipi': self.get_ipi(imposto),
                    'pis': self.get_pis(imposto),
                    'cofins': self.get_cofins(imposto),
                }
            }
            yield result

    def get_icms(self, obj):
        try:
            result = obj.find(self.item('ICMS'))[0].find(self.item('vICMS')).text
        except:
            result = '0.00'
        return result

    def get_ipi(self, obj):
        return '0.00'

    def get_pis(self, obj):
        try:
            result = obj.find(self.item('PIS'))[0].find(self.item('vPIS')).text
        except:
            result = '0.00'
        return result

    def get_cofins(self, obj):
        try:
            result = obj.find(self.item('COFINS'))[0].find(self.item('vCOFINS')).text
        except:
            result = '0.00'
        return result

load_dotenv()
caminho = os.getenv('CAMINHO')

#arquivo = ET.parse(caminho)

if __name__ == '__main__':
    arquivo = open(join(caminho, 'compilado.csv'), 'w+', newline='')
    arq = csv.writer(arquivo, delimiter=';')
    arq.writerow([
        'arquivo',
        'nota',
        'emit',
        'dest',
        'codigo',
        'descricao',
        'ncm',
        'cfop',
        'quantidade',
        'valor',
        'ipi',
        'pis',
        'cofins',
        'icms'
    ])
    for f in listdir(caminho):
        if isfile(join(caminho, f)) and f[-3:] == 'xml':
            k = nota(join(caminho, f))
            #print(k.arquivo)
            #print(k.versao)
            #print(k.suporte)
            for x in k.produtos():
                #print(x)
                arq.writerow([
                    k.arquivo,
                    '',
                    k.emit(),
                    k.dest(),
                    x['codigo'],
                    x['descricao'],
                    x['ncm'],
                    x['cfop'],
                    x['quantidade'].replace('.', ','),
                    x['valor'].replace('.', ','),
                    x['imposto']['ipi'].replace('.', ','),
                    x['imposto']['pis'].replace('.', ','),
                    x['imposto']['cofins'].replace('.', ','),
                    x['imposto']['icms'].replace('.', ','),
                ])
            del k


