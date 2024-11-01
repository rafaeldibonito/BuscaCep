from PyQt5 import uic, QtWidgets
import requests
from PyQt5.QtWidgets import QMessageBox, QLineEdit

# Cria uma aplicação PyQt5
app = QtWidgets.QApplication([])

# Carrega a interface gráfica a partir do arquivo 'interface.ui'
self = uic.loadUi('interface.ui')


# Define a função que busca as informações do site ViaCEP e preenche os campos do formulário
def buscarCep():
    # Pega o valor do campo de texto do CEP
    cep = self.cep.text()

    # Verifica se o campo de texto está vazio
    if cep:
        # Constrói a URL para a API do ViaCEP
        url = f'https://viacep.com.br/ws/{cep}/json/'

        # Faz uma solicitação GET para a API
        response = requests.get(url)

        # Verifica se a solicitação foi bem-sucedida
        if response.status_code == 200:
            # Converte a resposta para um formato JSON
            resposta = response.json()

            # Verifica se o CEP foi encontrado
            if 'erro' not in resposta:
                # Preenche os campos do formulário com os resultados da busca
                self.logradouro.setText(resposta["logradouro"])
                self.bairro.setText(resposta["bairro"])
                self.localidade.setText(resposta["localidade"])
                self.uf.setText(resposta["uf"])
                self.ibge.setText(resposta["ibge"])
                self.ddd.setText(resposta["ddd"])
            else:
                # Exibe uma mensagem se o CEP não foi encontrado
                msg = QMessageBox()
                msg.setWindowTitle('Erro!')
                msg.setText('Cep não encontrado!!')
                msg.exec()
                limparCamposFormulario()
        else:
            # Exibe uma mensagem se houver um erro
            msg = QMessageBox()
            msg.setWindowTitle('Erro!')
            msg.setText('CEP inválido!')
            msg.exec()
            limparCamposFormulario()
    else:
        # Exibe uma mensagem se o campo de texto estiver vazio
        msg = QMessageBox()
        msg.setWindowTitle('Atenção!!')
        msg.setText('Digite o CEP!')
        msg.exec()
        limparCamposFormulario()


# Conecta a função buscarCep ao botão de busca
self.buscarCep.clicked.connect(buscarCep)


# Define a função que limpa os campos do formulário
def limparCamposFormulario():
    # Limpa os campos do formulário
    self.cep.setText("")
    self.logradouro.setText("")
    self.bairro.setText("")
    self.localidade.setText("")
    self.uf.setText("")
    self.ibge.setText("")
    self.ddd.setText("")


# Conecta a função limparCamposFormulario ao botão de limpar
self.limparCampos.clicked.connect(limparCamposFormulario)

# Define o título da janela
self.setWindowTitle('BuscaCep')

# Mostra a janela
self.show()

# Inicia a aplicação
app.exec()