import xml.etree.ElementTree as ET
from dotenv import load_dotenv

caminho = os.getenv('CAMINHO')

arquivo = ET.parse(caminho)

class nota:
    versao = '' # Versão do XML da nota
    suporte = False # Mostra se a versão da nota foi testada
    xmlns = ''

    # Função para adicionar o namespace na tag
    item = lambda self, x: '{}{}'.format(self.xmlns, x)

    def __init__(self, caminho):
        # self.arquivo = ET.parse(caminho)
        self.arvore = ET.parse(caminho).getroot()
        self.versao = self.arvore.attrib['versao']
        self.xmlns = self.arvore.tag[:-7]

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

    def produtos(self):
        result = dict()
        itens = self.cam_find(['NFe', 'infNFe']).findall(self.item('det'))
        for x in itens:
            produto = x.find(self.item('prod'))
            result = {
                'codigo': produto.find(self.item('cProd')).text,
                'descricao': produto.find(self.item('xProd')).text,
                'ncm': produto.find(self.item('NCM')).text,
                'cest': produto.find(self.item('NCM')).text,
                'cfop': produto.find(self.item('CFOP')).text,
            }
            yield result

k = nota(caminho)


