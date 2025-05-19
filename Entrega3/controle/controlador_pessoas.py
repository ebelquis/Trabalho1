from limite.tela_pessoa import TelaPessoa
from entidade.vendedor import Vendedor
from entidade.cliente import Cliente
from excessoes.EncontradoNaListaException import EncontradoNaListaException
from excessoes.NaoEncontradoNaListaException import NaoEncontradoNaListaException

#TENHO QUE VER O QUE EU FAÇO AQUI

class ControladorPessoas():
    def __init__(self, controlador_sistema):
        self.__vendedores = []
        self.__clientes = []
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_sistema = controlador_sistema
    
    def pega_vendedor_por_cpf(self, cpf: int):
        for vendedor in self.__vendedores:
            if(vendedor.cpf == cpf):
                return vendedor
        return None

    def pega_cliente_por_cpf(self, cpf: int):
        for cliente in self.__clientes:
            if(cliente.cpf == cpf):
                return cliente
        return None

    def incluir_pessoa(self):
        dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
        if dados_pessoa["selecionador"] == 0:
            cpf = self.pega_vendedor_por_cpf(dados_pessoa["cpf"])
            try:
                if cpf is None:
                    pessoa = Cliente(dados_pessoa["nome"],
                                     dados_pessoa["cpf"],
                                     dados_pessoa["celular"])
                    self.__clientes.append(pessoa)
                else:
                    raise EncontradoNaListaException()
            except EncontradoNaListaException as e:
                self.__tela_pessoa.mostra_mensagem(e)

        elif dados_pessoa["selecionador"] == 1:
            cpf = self.pega_cliente_por_cpf(dados_pessoa["cpf"])
            try:
                if cpf is None:
                    pessoa = Vendedor(dados_pessoa["nome"],
                                    dados_pessoa["cpf"],
                                    dados_pessoa["celular"], 
                                    0)
                    self.__vendedores.append(pessoa)
                else:
                    raise EncontradoNaListaException()
            except EncontradoNaListaException as e:
                self.__tela_pessoa.mostra_mensagem(e)
        
    def alterar_pessoa(self):
        self.lista_cliente()
        self.lista_vendedores()
        selecionador, cpf = self.__tela_pessoa.seleciona_pessoa()
        if selecionador == 0:
            cpf = self.pega_vendedor_por_cpf(cpf)
            try:
                if cpf is not None:
                    vendedor = self.pega_pessoa_por_cpf(cpf)
                    novos_dados = self.__tela_pessoa.pega_dados_pessoa()
                    vendedor.nome = novos_dados["nome"],
                    vendedor.cpf = novos_dados["cpf"],
                    vendedor.celular = novos_dados["celular"],
                    vendedor.valor_vendido_total = 0
                else:
                    raise NaoEncontradoNaListaException()
            except NaoEncontradoNaListaException as e:
                self.__tela_pessoa.mostra_mensagem(e)

        elif selecionador == 1:
            cpf = self.pega_cliente_por_cpf(cpf)
            try:
                if cpf is not None:
                    novos_dados = self.__tela_pessoa.pega_dados_pessoa()
                    cliente = self.pega_pessoa_por_cpf(cpf)
                    cliente.nome = novos_dados["nome"],
                    cliente.cpf = novos_dados["cpf"],
                    cliente.celular = novos_dados["celular"]
                else:
                    raise NaoEncontradoNaListaException()
            except NaoEncontradoNaListaException as e:
                self.__tela_pessoa.mostra_mensagem(e)
            
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

    def excluir_pessoa(self):
        self.lista_cliente()
        self.lista_vendedores()
        selecionador, cpf = self.__tela_pessoa.seleciona_pessoa()

        if selecionador == 1:
            cliente = self.pega_cliente_por_cpf(cpf)
            try: 
                if cliente is not None:
                    self.__clientes.remove(cliente)
                    self.lista_cliente()
                else:
                    raise NaoEncontradoNaListaException()
            except NaoEncontradoNaListaException as e:
                self.__tela_pessoa.mostra_mensagem(e)

        elif selecionador == 0:
            vendedor = self.pega_vendedor_por_cpf(cpf)
            try:
                if vendedor is not None:
                    self.__vendedores.remove(vendedor)
                    self.lista_vendedores()
                else:
                    raise NaoEncontradoNaListaException()
            except NaoEncontradoNaListaException as e:
                self.__tela_pessoa.mostra_mensagem(e)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_pessoa,
                        2: self.alterar_pessoa,
                        3: self.lista_cliente,
                        4: self.lista_vendedores,
                        5: self.excluir_pessoa,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_pessoa.tela_opcoes()]()