from limite.tela_fornecedor import TelaFornecedor
from entidade.fornecedor import Fornecedor
from excessoes.EncontradoNaListaException import EncontradoNaListaException
from excessoes.NaoEncontradoNaListaException import NaoEncontradoNaListaException


class ControladorFornecedores: 
    def __init__(self, controlador_sistema):
        self.__fornecedores = []
        self.__tela_fornecedor = TelaFornecedor()
        self.__controlador_sistema = controlador_sistema

    def pega_fornecedor_por_cnpj(self, cnpj: int):
        for fornecedor in self.__fornecedores:
            if fornecedor.cnpj == cnpj:
                return fornecedor
        return None

    def incluir_fornecedor(self):
        dados_fornecedor = self.__tela_fornecedor.pega_dados_fornecedor()
        #TEM QUE VER COMO FAZER COM ISSO AQUI
        codigo = (dados_fornecedor["produto"]).codigo
        produto = codigo_produto.pega_produto_por_codigo()
        try:
            fornecedor = Fornecedor(dados_fornecedor["nome"],
                                    int(dados_fornecedor["cnpj"]),
                                    int(dados_fornecedor["celular"]),
                                    str(dados_fornecedor["produto"]),
                                    float(dados_fornecedor["preco"])
                                    )
            self.__fornecedores.append(fornecedor)

    def alterar_fornecedor(self):
        self.lista_fornecedores()
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)
        try:
            if fornecedor is not None:
                novos_dados_fornecedor = self.__tela_fornecedor.pega_dados_fornecedor()
                fornecedor.nome = novos_dados_fornecedor["nome"]
                fornecedor.cnpj = int(novos_dados_fornecedor["cnpj"])
                fornecedor.celular = novos_dados_fornecedor["celular"]
                fornecedor.produto = novos_dados_fornecedor["produto"]
                fornecedor.preco = float(novos_dados_fornecedor["preco"])
                self.lista_fornecedores()
            else:
                raise NaoEncontradoNaListaException()
        except NaoEncontradoNaListaException as e:
            self.__tela_produto.mostra_mensagem(e)
    
    def adicionar_endereco(self):
        self.lista_fornecedores()
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)
        try:
            if fornecedor is not None:
                dados_endereco = self.__tela_fornecedor.pega_dados_endereco()
                fornecedor.incluir_endereco(
                    dados_endereco["cep"],
                    dados_endereco["rua"],
                    dados_endereco["numero"]
                     )
                fornecedor.lista_enderecos()
            else:
                raise NaoEncontradoNaListaException()
        except NaoEncontradoNaListaException as e:
            self.__tela_produto.mostra_mensagem(e)

    def lista_fornecedores(self):
        for fornecedor in self.__fornecedores:
            self.__tela_fornecedor.mostra_fornecedor({
                "nome": fornecedor.nome,
                "cnpj": fornecedor.cnpj,
                "celular": fornecedor.celular,
                "produto": fornecedor.produto,
                "preco": fornecedor.preco
            })

    def excluir_fornecedores(self):
        self.lista_fornecedores()
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)
        try:
            if fornecedor is not None:
                self.__fornecedores.remove(fornecedor)
                self.lista_fornecedores()
            else:
                raise EncontradoNaListaException()
        except EncontradoNaListaException as e:
            self.__tela_produto.mostra_mensagem(e)            

    def excluir_endereco(self):
        self.lista_fornecedores()
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)
        try:
            if fornecedor is not None:
                cep_fornecedor = self.__tela_fornecedor.seleciona_endereco()
                try:
                    if cep_fornecedor is not None:
                        fornecedor.remover_endereco(cep_fornecedor)
                        self.lista_enderecos()
                    else:
                        raise EncontradoNaListaException()
                except EncontradoNaListaException as e:
                    self.__tela_fornecedor.mostra_mensagem(e)
            else:
                raise EncontradoNaListaException()
        except EncontradoNaListaException as e:
            self.__tela_fornecedor.mostra_mensagem(e)

    def listar_enderecos(self):
        self.lista_fornecedores()
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)
        if fornecedor:
            for endereco in fornecedor.lista_enderecos:
                self.__tela_fornecedor.mostra_endereco({
                    "cep": endereco.cep,
                    "rua": endereco.rua,
                    "numero": endereco.numero
                })
        else:
            self.__tela_fornecedor.mostra_mensagem("ATENCAO: Fornecedor não encontrado.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_fornecedor, 2: self.alterar_fornecedor,
                        3: self.lista_fornecedores, 4: self.excluir_fornecedores,
                        5: self.adicionar_endereco, 6: self.excluir_endereco,
                        7: self.listar_enderecos,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_fornecedor.tela_opcoes()]()