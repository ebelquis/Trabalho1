class TelaFornecedor():
    def tela_opcoes(self):
        print("-------- FORNECEDOR ----------")
        print()
        print("1 - Incluir Fornecedor")
        print("2 - Alterar Fornecedor")
        print("3 - Listar Fornecedores")
        print("4 - Excluir Fornecedor")
        print("5 - Incluir Endereco do Fornecedor")
        print("6 - Excluir Endereco do Forcedor")
        print("0 - Retornar")
        print()
        opcao = int(input("Escolha a opção: "))
        print()
        return opcao

    def pega_dados_fornecedor(self):
        print("-------- DADOS FORNECEDORES ----------")
        print()
        nome = input("Nome/Razão Social: ")
        cnpj = input("CNPJ: ")
        celular = input("Celular: ")
        produto = input("Código do produto: ")
        preco = input("Preço: ")
        print()

        return {"nome": nome, "cnpj": cnpj, "celular": celular, "produto": produto, "preco": preco,}

    def mostra_fornecedor(self, dados_fornecedor):
        print("NOME/RAZÃO SOCIAL: ", dados_fornecedor["nome"])
        print("CNPJ: ", dados_fornecedor["cnpj"])
        print("TELEFONE/CELULAR: ", dados_fornecedor["celular"])
        print("PRODUTO VENDIDO: ", dados_fornecedor["produto"])
        print("PREÇO DO PRODUTO: ", dados_fornecedor["preco"])
        if dados_fornecedor["enderecos"]:
            print("ENDEREÇOS DO FORNECEDOR:")
            count = 1
            for endereco in dados_fornecedor["enderecos"]:
                print(f'Endereço {count}: {endereco.rua}, {endereco.numero} - CEP: {endereco.cep}')
                count += 1
        else:
            print("Fornecedor sem endereço")
        print()

    def pega_dados_endereco(self):
        print("-------- DADOS DO ENDERECO ----------")
        print()
        cep = input("CEP: ")
        rua = input("Rua: ")
        numero = input("Número: ")
        print()
        return {"cep": cep, "rua": rua, "numero": numero}

    def mostra_endereco(self, dados_endereco):
        print('-------- ENDERECO ----------')
        print("CEP: ", dados_endereco["cep"])
        print("RUA: ", dados_endereco["rua"])
        print("NÚMERO: ", dados_endereco["numero"])
        print()

    def seleciona_fornecedor(self):
        cnpj = input("CNPJ do fornecedor que deseja selecionar: ")
        print()
        return cnpj

    def seleciona_endereco(self):
        cep = input("CEP do endereço que deseja selecionar: ")
        print()
        return cep

    def mostra_mensagem(self, msg):
        print(msg)
        print()
