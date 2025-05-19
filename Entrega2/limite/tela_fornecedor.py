class TelaFornecedor():
    def tela_opcoes(self):
        print("-------- AMIGOS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Fornecedor")
        print("2 - Alterar Fornecedor")
        print("3 - Listar Fornecedores")
        print("4 - Excluir Fornecedor")
        print("5 - Incluir Endereco do Fornecedor")
        print("6 - Excluir Endereco do Forcedor")
        print("7 - Listar Enderecos do Forcedor")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_fornecedor(self):
        print("-------- DADOS FORNECEDORES ----------")
        nome = input("Nome: ")
        cnpj = input("cnpj: ")
        telefone = input("telefone: ")
        produto = input("produto: ")
        preco = input("preco: ")

        return {"nome": nome, "cnpj": cnpj, "telefone": telefone, "produto": produto, "preco": preco,}

    def mostra_fornecedor(self, dados_fornecedor):
        print("NOME DO FORNECEDOR: ", dados_fornecedor["nome"])
        print("CNPJ DO FORNECEDOR: ", dados_fornecedor["cnpj"])
        print("TELEFONE DO FORNECEDOR: ", dados_fornecedor["telefone"])
        print("PRODUTO DO FORNECEDOR: ", dados_fornecedor["produto"])
        print("PRECO DO FORNECEDOR: ", dados_fornecedor["preco"])
        print("\n")

    def pega_dados_endereco(self):
        print("-------- DADOS DO ENDERECO ----------")
        cep = input("cep: ")
        rua = input("rua: ")
        numero = input("numero: ")

        return {"cep": cep, "rua": rua, "numero": numero}

    def mostra_endereco(self, dados_endereco):
        print("CEP DO FORNECEDOR: ", dados_endereco["cep"])
        print("RUA DO FORNECEDOR: ", dados_endereco["rua"])
        print("NUMERO DA EMPRESA DO FORNECEDOR: ", dados_endereco["numero"])
        print("\n")

    def seleciona_fornecedor(self):
        cnpj = input("Cnpj do fornecedor que deseja selecionar: ")
        return cnpj

    def seleciona_endereco(self):
        cep = input("Cep do fornecedor que deseja selecionar: ")
        return cep

    def mostra_mensagem(self, msg):
        print(msg)