from limite.tela_pessoa import TelaPessoa
from entidade.vendedor import Vendedor
from entidade.cliente import Cliente
from excessoes.EncontradoNaListaException import EncontradoNaListaException
from excessoes.NaoEncontradoNaListaException import NaoEncontradoNaListaException

class ControladorPessoas():
    def __init__(self, controlador_sistema):
        self.__vendedores = []
        self.__clientes = []
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_sistema = controlador_sistema

<<<<<<< HEAD
    def pega_cliente_por_cpf(self, cpf: int):
=======
    def pega_cliente_por_cpf(self, cpf: str):
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def pega_vendedor_por_cpf(self, cpf: int):
        for vendedor in self.__vendedores:
            if vendedor.cpf == cpf:
                return vendedor
        return None

    def incluir_cliente(self):
        dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
<<<<<<< HEAD
        try:
            if self.pega_cliente_por_cpf(dados_pessoa["cpf"]) is None:
                pessoa = Cliente(dados_pessoa["nome"],
                                dados_pessoa["cpf"],
                                dados_pessoa["celular"])
                self.__clientes.append(pessoa)
                self.__tela_pessoa.mostra_mensagem("Cliente incluído com sucesso!")
            else:
                raise EncontradoNaListaException()
        except Exception as e:
            self.__tela_pessoa.mostra_mensagem(e)

    def incluir_vendedor(self):
        dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
        try:
            if self.pega_vendedor_por_cpf(dados_pessoa["cpf"]) is None:
                pessoa = Vendedor(dados_pessoa["nome"],
                                dados_pessoa["cpf"],
                                dados_pessoa["celular"], 
                                0)
                self.__vendedores.append(pessoa)
                self.__tela_pessoa.mostra_mensagem("Vendedor incluído com sucesso!")
            else:
                raise EncontradoNaListaException()
        except Exception as e:
            self.__tela_pessoa.mostra_mensagem(e)     

    def lista_cliente(self):
        if len(self.__clientes) == 0:
            self.__tela_pessoa.mostra_mensagem("Não há clientes cadastrados.")
            return None

=======
        if self.pega_cliente_por_cpf(dados_pessoa["cpf"]) is None:
            pessoa = Cliente(dados_pessoa["nome"],
                            dados_pessoa["cpf"],
                            dados_pessoa["celular"])
            self.__clientes.append(pessoa)
            self.__tela_pessoa.mostra_mensagem("Cliente incluído com sucesso!")
        else:
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: CPF já utilizado.")

    def incluir_vendedor(self):
        dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
        if self.pega_vendedor_por_cpf(dados_pessoa["cpf"]) is None:
            pessoa = Vendedor(dados_pessoa["nome"],
                            dados_pessoa["cpf"],
                            dados_pessoa["celular"], 
                            0)
            self.__vendedores.append(pessoa)
            self.__tela_pessoa.mostra_mensagem("Vendedor incluído com sucesso!")
        else:
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: CPF já utilizado.")
# Esse metodo alterar_pessoa não tá sendo usado. Mandei áudio explicando oq eu achei
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
        if not self.__clientes:
            self.__tela_pessoa.mostra_mensagem("Não há clientes cadastrados.")
            return None
        
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe
        for cliente in self.__clientes:
            self.__tela_pessoa.mostra_cliente({"nome": cliente.nome,
                                               "cpf": cliente.cpf,
                                               "celular": cliente.celular})

    def lista_vendedores(self):
<<<<<<< HEAD
        if len(self.__clientes) == 0:
=======
        if not self.__clientes:
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe
            self.__tela_pessoa.mostra_mensagem("Não há vendedores cadastrados.")
            return None

        for vendedor in self.__vendedores:
            self.__tela_pessoa.mostra_vendedor({"nome": vendedor.nome,
                                                "cpf": vendedor.cpf,
                                                "celular": vendedor.celular,
                                                "valor_vendido_total": vendedor.valor_vendido_total})

    def excluir_cliente(self):
<<<<<<< HEAD
        try:
            if len(self.__clientes) == 0:
                self.__tela_pessoa.mostra_mensagem("Não existe clientes para excluir")
            else:
                self.lista_cliente()
                cpf = self.__tela_pessoa.seleciona_pessoa()
                cliente = self.pega_cliente_por_cpf(cpf)
                if cliente is not None:
                    self.__clientes.remove(cliente)
                    self.__tela_pessoa.mostra_mensagem("Cliente excluído com sucesso!")
                    if len(self.__clientes) != 0:
                        self.__tela_pessoa.mostra_mensagem("Clientes restantes:")
                        self.lista_cliente()
                else:
                    raise NaoEncontradoNaListaException("cliente")
        except Exception as e:
            self.__tela_pessoa.mostra_mensagem(e)

    def excluir_vendedor(self):
        try:
            if len(self.__vendedores) == 0:
                self.__tela_pessoa.mostra_mensagem("Não existe vendedor para excluir")
            else:
                self.lista_vendedores()
                cpf = self.__tela_pessoa.seleciona_pessoa()
                vendedor = self.pega_vendedor_por_cpf(cpf)
                if vendedor is not None:
                    self.__vendedores.remove(vendedor)
                    self.__tela_pessoa.mostra_mensagem("Vendedor excluído com sucesso!")
                    if len(self.__vendedores) != 0:
                        self.__tela_pessoa.mostra_mensagem("Vendedores restantes:")
                        self.lista_vendedores()
                else:
                    raise NaoEncontradoNaListaException("vendedor")
        except Exception as e:
            self.__tela_pessoa.mostra_mensagem(e)
=======
        self.lista_cliente()
        cpf = self.__tela_pessoa.seleciona_pessoa()
        cliente = self.pega_pessoa_por_cpf(cpf)

        if cliente is not None:
            self.__clientes.remove(cliente)
            self.__tela_pessoa.mostra_mensagem("Cliente excluído com sucesso!\nClientes restantes:")
            self.lista_cliente()
        else:
            self.__tela_pessoa.mostra_mensagem("Cliente não existente")

    def excluir_vendedor(self):
        self.lista_vendedores()
        cpf = self.__tela_pessoa.seleciona_pessoa()
        vendedor = self.pega_pessoa_por_cpf(cpf)

        if vendedor is not None:
            self.__vendedores.remove(vendedor)
            self.__tela_pessoa.mostra_mensagem("Vendedor excluído com sucesso!\nVendedores restantes:")
            self.lista_vendedores()
        else:
            self.__tela_pessoa.mostra_mensagem("Vendedor não existente")
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe

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

        while True:
            opcao_escolhida = self.__tela_pessoa.tela_opcoes()
            if opcao_escolhida in lista_opcoes:
                lista_opcoes[opcao_escolhida]()
            else:
<<<<<<< HEAD
                self.__tela_pessoa.mostra_mensagem("Opção inválida, digite novamente.")
=======
                self.__tela_pedido.mostra_mensagem("Opção inválida, digite novamente.")
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe
