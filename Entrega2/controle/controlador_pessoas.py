from limite.tela_pessoa import TelaPessoa
from entidade.pessoa import Pessoa
from entidade.vendedor import Vendedor
from entidade.cliente import Cliente
#TENHO QUE VER O QUE EU FAÇO AQUI

class ControladorPessoas():
    def __init__(self, controlador_sistema):
        self.__vendedores = []
        self.__clientes = []
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_sistema = controlador_sistema

    def incluir_cliente(self):
        dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
        pessoa = Cliente(dados_pessoa["nome"],
                         dados_pessoa["cpf"],
                         dados_pessoa["celular"])
        self.__clientes.append(pessoa)

    def incluir_vendedor(self):
        dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
        pessoa = Vendedor(dados_pessoa["nome"],
                          dados_pessoa["cpf"],
                          dados_pessoa["celular"], 
                          0)
        self.__vendedores.append(pessoa)

    def alterar_pessoa(self):
        self.lista_cliente()
        cpf = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.pega_pessoa_por_cpf(cpf)

        if pessoa:
            novos_dados = self.__tela_pessoa.pega_dados_pessoa()
            pessoa.nome = novos_dados["nome"]
            pessoa.cpf = novos_dados["cpf"]
            pessoa.celular = novos_dados["celular"]
        else:
            self.__tela_pessoa.mostra_mensagem("Pessoa não encontrada!")

    def lista_cliente(self):
        for cliente in self.__clientes:
            self.__tela_pessoa.mostra_cliente({"nome": cliente.nome,
                                               "cpf": cliente.cpf,
                                               "celular": cliente.celular})

    def lista_vendedores(self):
        for vendedor in self.__vendedores:
            self.__tela_pessoa.mostra_vendedor({"nome": vendedor.nome,
                                                "cpf": vendedor.cpf,
                                                "celular": vendedor.celular,
                                                "valor_vendido_total": vendedor.valor_vendido_total})

    def excluir_cliente(self):
        self.lista_cliente()
        cpf = self.__tela_pessoa.seleciona_pessoa()
        cliente = self.pega_pessoa_por_cpf(cpf)

        if(cliente is not None):
            self.__clientes.remove(cliente)
            self.lista_cliente()
        else:
            self.__tela_pessoa.mostra_mensagem("Cliente não existente")

    def excluir_vendedor(self):
        self.lista_vendedores()
        cpf = self.__tela_pessoa.seleciona_pessoa()
        vendedor = self.pega_pessoa_por_cpf(cpf)

        if(vendedor is not None):
            self.__vendedores.remove(vendedor)
            self.lista_vendedores()
        else:
            self.__tela_pessoa.mostra_mensagem("Vendedor não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cliente,
                        2: self.incluir_vendedor,
                        3: self.lista_cliente,
                        4: self.excluir_cliente,
                        5: self.lista_vendedores,
                        6: self.excluir_vendedor,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_pessoa.tela_opcoes()]()