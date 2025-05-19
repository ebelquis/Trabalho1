from excessoes.OpcaoErroException import OpcaoErroException

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

        try:
            opcao = int(input("Escolha a opcao: "))
            if opcao not in [0, 1, 2, 3, 4, 5, 6, 7]:
                raise OpcaoErroException()
            return opcao
        except OpcaoErroException as e:
            self.__tela_venda.mostra_mensagem(e)

    def pega_dados_fornecedor(self):
        print("-------- DADOS FORNECEDORES ----------")
        
        while True:
            try:
                nome = str(input("Nome: "))
                break
            except ValueError:
                print("nome inválido. Insira algo válido (erro de digitacao).")

        while True:
            try:
                cnpj = int(input("Cnpj: "))
                break
            except ValueError:
                print("cnpj inválido. Insira um valor valido (erro de digitacao).")

        while True:
            try:
                telefone = int(input("telefone: "))
                break
            except ValueError:
                print("telefone inválido. Insira valor válido (erro de digitacao).")

        while True:
            try:
                produto = str(input("produto: "))
                break
            except ValueError:
                print("produto inválido. Insira algo válido (erro de digitacao).")

        while True:
            try:
                preco = float(input("preco: "))
                break
            except ValueError:
                print("preco inválido. Insira valor válido (erro de digitacao).")

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
        while True:
            try:
                cep = int(input("cep: "))
                break
            except ValueError:
                print("cep inválido. Insira valor válido (erro de digitacao).")

        while True:
            try:
                rua = str(input("rua: "))
                break
            except ValueError:
                print("rua inválida. Insira algo válido (erro de digitacao).")

        while True:
            try:
                numero = int(input("numero: "))
                break
            except ValueError:
                print("numero inválido. Insira valor válido (erro de digitacao).")

        return {"cep": cep, "rua": rua, "numero": numero}

    def mostra_endereco(self, dados_endereco):
        print("CEP DO FORNECEDOR: ", dados_endereco["cep"])
        print("RUA DO FORNECEDOR: ", dados_endereco["rua"])
        print("NUMERO DA EMPRESA DO FORNECEDOR: ", dados_endereco["numero"])
        print("\n")

    def seleciona_fornecedor(self):
        while True:
            try:
                cnpj = int(input("Cnpj do fornecedor que deseja selecionar: "))
                break
            except ValueError:
                print("Esse valor é invalido (erro de digitacao)!") 
            return cnpj


    def seleciona_endereco(self):
        while True:
            try:
                cep = int(input("Cep do fornecedor que deseja selecionar: "))
                break
            except ValueError:
                print("Esse valor é invalido (erro de digitacao)!") 
            return cep

    def mostra_mensagem(self, msg):
        print(msg)