from limite.tela_fornecedor import TelaFornecedor
from limite.tela_produto import TelaProduto
from entidade.fornecedor import Fornecedor
from excessoes.EncontradoNaListaException import EncontradoNaListaException
from excessoes.NaoEncontradoNaListaException import NaoEncontradoNaListaException
class ControladorFornecedores:
    
    def __init__(self, controlador_sistema):
        self.__fornecedores = []
        self.__tela_fornecedor = TelaFornecedor()
        self.__controlador_sistema = controlador_sistema
        self.__fornecedores[0].incluir_endereco("88037200", "Av. Gov. José Boabaid", "30")
        self.__fornecedores[1].incluir_endereco("95070380", "Rua Amâncio Miguel Ferreira", "229")

    def pega_fornecedor_por_cnpj(self, cnpj: str):
        for fornecedor in self.__fornecedores:
<<<<<<< HEAD
            if int(fornecedor.cnpj) == int(cnpj):
=======
            if fornecedor.cnpj == cnpj:
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe
                return fornecedor
        return None

    def incluir_fornecedor(self):
        self.lista_fornecedores()
        dados_fornecedor = self.__tela_fornecedor.pega_dados_fornecedor()
<<<<<<< HEAD
        try:
            codigo_produto = int(dados_fornecedor["produto"])  
            objeto_produto = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(codigo_produto)
            if objeto_produto is not None:
                if self.pega_fornecedor_por_cnpj(dados_fornecedor["cnpj"]) is None:
                    fornecedor = Fornecedor(
                        str(dados_fornecedor["nome"]),
                        int(dados_fornecedor["cnpj"]),
                        int(dados_fornecedor["celular"]),
                        objeto_produto,
                        float(dados_fornecedor["preco"]) 
                    )
                    self.__fornecedores.append(fornecedor)
                    self.__tela_fornecedor.mostra_mensagem("Fornecedor incluído com sucesso!")
                else:
                    raise EncontradoNaListaException()
            else:
                raise NaoEncontradoNaListaException("produto")
        except Exception as e:
            self.__tela_fornecedor.mostra_mensagem(e)
=======

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
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe

    def alterar_fornecedor(self):
        self.lista_fornecedores
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)       
<<<<<<< HEAD
        try:
            if fornecedor is not None:
                novos_dados_fornecedor = self.__tela_fornecedor.pega_dados_fornecedor()
                fornecedor_copiado = self.pega_fornecedor_por_cnpj(novos_dados_fornecedor["cnpj"])       
                novo_codigo_produto = int(novos_dados_fornecedor["produto"])
                novo_produto = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(novo_codigo_produto)
                if fornecedor_copiado is None or (fornecedor_copiado == cnpj_fornecedor):
                    if novo_produto is not None:
                        fornecedor.nome = novos_dados_fornecedor["nome"]
                        fornecedor.cnpj = novos_dados_fornecedor["cnpj"]
                        fornecedor.celular = novos_dados_fornecedor["celular"]
                        fornecedor.produto = novo_produto
                        fornecedor.preco = float(novos_dados_fornecedor["preco"])
                        self.__tela_fornecedor.mostra_mensagem("Fornecedor alterado com sucesso.")
                    else:
                        raise NaoEncontradoNaListaException("produto")
                else:
                    raise EncontradoNaListaException()
            else:
                raise NaoEncontradoNaListaException("fornecedor")
        except Exception as e:
            self.__tela_fornecedor.mostra_mensagem(e)
=======

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
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe

    def adicionar_endereco(self):
        self.lista_fornecedores()
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)
        try:
            if fornecedor is None:
                raise NaoEncontradoNaListaException("fornecedor")
            dados_endereco = self.__tela_fornecedor.pega_dados_endereco()
            cep_novo = dados_endereco["cep"]
            cep_existente = False
            for endereco in fornecedor.enderecos:
                if int(endereco.cep) == int(cep_novo): 
                    cep_existente = True
                    break  
            if cep_existente:
                raise EncontradoNaListaException()
            fornecedor.incluir_endereco(
                int(dados_endereco["cep"]),
                str(dados_endereco["rua"]),
                int(dados_endereco["numero"])
            )
<<<<<<< HEAD
            self.__tela_fornecedor.mostra_mensagem("Endereço adicionado com sucesso!")
            
        except Exception as e:
            self.__tela_fornecedor.mostra_mensagem(e)
=======
            self.__tela_fornecedor.mostra_mensagem("Endereço adicionado com sucesso!\n")
            fornecedor.lista_enderecos()
#            enderecos = fornecedor.lista_enderecos()
#            for endereco in enderecos:
#                self.__tela_fornecedor.mostra_endereco(endereco)
#        else:
#            self.__tela_fornecedor.mostra_mensagem("ATENCAO: Fornecedor não encontrado.")
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe

    def lista_fornecedores(self):
        if not self.__fornecedores:
            self.__tela_fornecedor.mostra_mensagem("Não há fornecedores cadastrados.")
<<<<<<< HEAD
        else:
            for fornecedor in self.__fornecedores:
                enderecos = []
                for endereco in fornecedor.enderecos:
                    enderecos.append({"cep": endereco.cep,
                                      "rua": endereco.rua,
                                      "numero": endereco.numero})
=======
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
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe

                dados = {"nome": fornecedor.nome,
                         "cnpj": fornecedor.cnpj,
                         "celular": fornecedor.celular,
                         "produto": fornecedor.produto.nome,
                         "preco": fornecedor.preco,
                         "enderecos": enderecos}
                self.__tela_fornecedor.mostra_fornecedor(dados)

    def excluir_fornecedor(self):
        self.lista_fornecedores()
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)
<<<<<<< HEAD
        try:
            if fornecedor is not None:
                self.__fornecedores.remove(fornecedor)
                self.__tela_fornecedor.mostra_mensagem("Fornecedor excluído com sucesso!")
            else:
                raise NaoEncontradoNaListaException()
        except Exception as e:
            self.__tela_fornecedor.mostra_mensagem(e)
=======

        if fornecedor is not None:
            self.__fornecedores.remove(fornecedor)
            self.__tela_fornecedor.mostra_mensagem("Fornecedor excluído com sucesso!")
            self.lista_fornecedores()
        else:
            self.__tela_fornecedor.mostra_mensagem("ATENÇÃO: Fornecedor não encontrado.")
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe

    def excluir_endereco(self):
        self.lista_fornecedores()
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)
<<<<<<< HEAD
        try:
            if fornecedor is None:
                raise NaoEncontradoNaListaException("fornecedor") 
            cep_endereco = self.__tela_fornecedor.seleciona_endereco()
            endereco_remover = None
            for endereco in fornecedor.enderecos:
                if str(endereco.cep).strip() == str(cep_endereco).strip():
                    endereco_remover = endereco
                    break
            if endereco_remover:
                fornecedor.enderecos.remove(endereco_remover)
                self.__tela_fornecedor.mostra_mensagem("Endereço excluído com sucesso!")
                self.lista_fornecedores()
            else:
                raise NaoEncontradoNaListaException("endereço")
        except Exception as e:
            self.__tela_fornecedor.mostra_mensagem(e)
            
=======
        
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

>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_fornecedor,
            2: self.alterar_fornecedor,
            3: self.lista_fornecedores,
            4: self.excluir_fornecedor,
            5: self.adicionar_endereco,
            6: self.excluir_endereco,
            0: self.retornar
        }

        while True:
            opcao_escolhida = self.__tela_fornecedor.tela_opcoes()
            if opcao_escolhida in lista_opcoes:
                lista_opcoes[opcao_escolhida]()
            else:
<<<<<<< HEAD
                self.__tela_fornecedor.mostra_mensagem("Opção inválida, digite novamente.")
=======
                self.__tela_fornecedor.mostra_mensagem("Opção inválida, digite novamente.")


            
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe
