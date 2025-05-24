from limite.tela_fornecedor import TelaFornecedor
from limite.tela_produto import TelaProduto
from entidade.fornecedor import Fornecedor
from entidade.produto import Produto

class ControladorFornecedores:
    
    def __init__(self, controlador_sistema):
        self.__fornecedores = [Fornecedor("Gumege Alumínios", 1111, 4899, Produto("caneca", 1, 20.00, 10), 10.00), 
                               Fornecedor("Somar", 2222, 549, Produto('camisa m', 21, 40.00, 6), 25.00)]
        self.__tela_fornecedor = TelaFornecedor()
        self.__controlador_sistema = controlador_sistema
        self.__fornecedores[0].incluir_endereco("88037200", "Av. Gov. José Boabaid", "30")
        self.__fornecedores[1].incluir_endereco("95070380", "Rua Amâncio Miguel Ferreira", "229")

    def pega_fornecedor_por_cnpj(self, cnpj: str):
        for fornecedor in self.__fornecedores:
            if fornecedor.cnpj == cnpj:
                return fornecedor
        return None

    def incluir_fornecedor(self):
        self.lista_fornecedores()
        dados_fornecedor = self.__tela_fornecedor.pega_dados_fornecedor()

        codigo_produto = int(dados_fornecedor["produto"])
        objeto_produto = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(codigo_produto)

        if objeto_produto:
            fornecedor = Fornecedor(
                dados_fornecedor["nome"],
                dados_fornecedor["cnpj"],
                dados_fornecedor["celular"],
                objeto_produto,
                float(dados_fornecedor["preco"])
                )
            if self.pega_fornecedor_por_cnpj(dados_fornecedor["cnpj"]) is None: #daria para colocar if not...
                self.__fornecedores.append(fornecedor)
                self.__tela_fornecedor.mostra_mensagem("Fornecedor incluído com sucesso!")
                self.__tela_fornecedor.mostra_fornecedor({
                                                            "nome": fornecedor.nome,
                                                            "cnpj": fornecedor.cnpj,
                                                            "celular": fornecedor.celular,
                                                            "produto": fornecedor.produto.nome,
                                                            "preco": fornecedor.preco,
                                                            "enderecos": fornecedor.enderecos
                                                        })
            else:
                self.__tela_fornecedor.mostra_mensagem("ATENÇÃO: Já existe um fornecedor com este CNPJ")
        else:
            self.__tela_fornecedor.mostra_mensagem("ATENÇÃO: Produto não encontrado.\nNão foi possível incluir o fornecedor.")

    def alterar_fornecedor(self):
        self.lista_fornecedores()
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)       

        if fornecedor:
            novos_dados_fornecedor = self.__tela_fornecedor.pega_dados_fornecedor()
            novo_codigo_produto = int(novos_dados_fornecedor["produto"])
            novo_objeto_produto = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(novo_codigo_produto)

            if novo_objeto_produto:
                fornecedor.nome = novos_dados_fornecedor["nome"]
                fornecedor.cnpj = novos_dados_fornecedor["cnpj"]
                fornecedor.celular = novos_dados_fornecedor["celular"]
                fornecedor.produto = novo_objeto_produto
                fornecedor.preco = float(novos_dados_fornecedor["preco"])
                self.__tela_fornecedor.mostra_mensagem("Fornecedor alterado com sucesso.\n")
                self.__tela_fornecedor.mostra_fornecedor({"nome": fornecedor.nome,
                                                         "codigo": fornecedor.codigo_produto,
                                                         "preco_venda": fornecedor.preco_venda,
                                                         "quant_estoque": fornecedor.quant_estoque})
            else:
                self.__tela_fornecedor.mostra_mensagem("ATENÇÃO: Produto não encontrado.\n")
        else:
            self.__tela_fornecedor.mostra_mensagem("ATENÇÃO: Fornecedor não encontrado.\n")

    def adicionar_endereco(self):
        self.lista_fornecedores()
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)

        if fornecedor:
            dados_endereco = self.__tela_fornecedor.pega_dados_endereco()
            fornecedor.incluir_endereco(
                dados_endereco["cep"],
                dados_endereco["rua"],
                dados_endereco["numero"]
            )
            self.__tela_fornecedor.mostra_mensagem("Endereço adicionado com sucesso!\n")
            fornecedor.lista_enderecos()
#            enderecos = fornecedor.lista_enderecos()
#            for endereco in enderecos:
#                self.__tela_fornecedor.mostra_endereco(endereco)
#        else:
#            self.__tela_fornecedor.mostra_mensagem("ATENCAO: Fornecedor não encontrado.")

    def lista_fornecedores(self):
        if not self.__fornecedores:
            self.__tela_fornecedor.mostra_mensagem("Não há fornecedores cadastrados.")
            return

        for fornecedor in self.__fornecedores:
            self.__tela_fornecedor.mostra_fornecedor({
                "nome": fornecedor.nome,
                "cnpj": fornecedor.cnpj,
                "celular": fornecedor.celular,
                "produto": fornecedor.produto.nome,
                "preco": fornecedor.preco,
                "enderecos": fornecedor.enderecos
            })

    def excluir_fornecedores(self):
        self.lista_fornecedores()
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)

        if fornecedor is not None:
            self.__fornecedores.remove(fornecedor)
            self.__tela_fornecedor.mostra_mensagem("Fornecedor excluído com sucesso!")
            self.lista_fornecedores()
        else:
            self.__tela_fornecedor.mostra_mensagem("ATENÇÃO: Fornecedor não encontrado.")

    def excluir_endereco(self):
        self.lista_fornecedores()
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)
        
        if fornecedor is not None:
            self.listar_enderecos_do_fornecedor()
            cep_endereco = self.__tela_fornecedor.seleciona_endereco()

            endereco_encontrado = False
            for endereco in fornecedor.enderecos:
                if endereco.cep == cep_endereco:
                    fornecedor.remover_endereco(cep_endereco)
                    endereco_encontrado = True
                    self.__tela_fornecedor.mostra_mensagem("Endereço excluído com sucesso!\nEndereços restantes:")
                    self.listar_enderecos_do_fornecedor()
                    break
            if not endereco_encontrado:
                self.__tela_fornecedor.mostra_mensagem("ATENCAO: Endereço não encontrado para este fornecedor.")
        else:
            self.__tela_fornecedor.mostra_mensagem("ATENCAO: Fornecedor não encontrado.")

    def listar_enderecos_do_fornecedor(self):
        self.lista_fornecedores()
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)
        if fornecedor:
            if fornecedor.enderecos:
                for endereco in fornecedor.lista_enderecos:
                    self.__tela_fornecedor.mostra_endereco({
                        "cep": endereco.cep,
                        "rua": endereco.rua,
                        "numero": endereco.numero
                    })
            else:
                self.__tela_fornecedor.mostra_mensagem("Fornecedor sem endereços cadastrados.")
        else:
            self.__tela_fornecedor.mostra_mensagem("ATENCAO: Fornecedor não encontrado.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_fornecedor, 2: self.alterar_fornecedor,
                        3: self.lista_fornecedores, 4: self.excluir_fornecedores,
                        5: self.adicionar_endereco, 6: self.excluir_endereco,
                        0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_fornecedor.tela_opcoes()
            if opcao_escolhida in lista_opcoes:
                lista_opcoes[opcao_escolhida]()
            else:
                self.__tela_fornecedor.mostra_mensagem("Opção inválida, digite novamente.")


            