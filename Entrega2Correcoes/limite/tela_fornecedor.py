from excessoes.TesteNumeroOpcoesException import TesteNumeroOpcoes
import math

class TelaFornecedor(TesteNumeroOpcoes):

    def __init__(self):
        pass

    def teste_do_cnpj(self, mensagem=" "):
        while True:
            valor_recebido = input(mensagem)
            try:
                valor_recebido_tipo = int(valor_recebido)
                if len(valor_recebido) == 14:
                    return valor_recebido_tipo
                else:
                    raise ValueError
            except ValueError:
                print("Por favor, escreva somente com numeros inteiros e coloque 14 digitos. Exemplo 1234 (erro na digitação)")

    def teste_do_cep(self, mensagem=" "):
        while True:
            valor_recebido = input(mensagem)
            try:
                valor_recebido_tipo = int(valor_recebido)
                if len(valor_recebido) == 8:
                    return valor_recebido_tipo
                else:
                    raise ValueError
            except ValueError:
                print("Por favor, escreva somente com numeros inteiros. Exemplo 1234 (erro na digitação)")
            
    def teste_do_float(self, mensagem=" "):
        while True:
            valor_recebido = input(mensagem)
            try:
                valor_recebido_tipo = float(valor_recebido)
                return valor_recebido_tipo
            except ValueError:
                print("Por favor, escreva somente com numeros inteiros. Exemplo 1234 (erro na digitação)")

    def teste_do_inteiro(self, mensagem=" "):
        while True:
            valor_recebido = input(mensagem)
            try:
                valor_recebido_tipo = int(valor_recebido)
                return valor_recebido_tipo
            except ValueError:
                print("Por favor, escreva somente com numeros inteiros. Exemplo 1234 (erro na digitação)")

    def tela_opcoes(self):
        print("-------- FORNECEDOR ----------")
<<<<<<< HEAD
=======
        print()
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe
        print("1 - Incluir Fornecedor")
        print("2 - Alterar Fornecedor")
        print("3 - Listar Fornecedores")
        print("4 - Excluir Fornecedor")
<<<<<<< HEAD
        print("5 - Incluir Endereço")
        print("6 - Excluir Endereço")
        print("0 - Retornar")
    
        opcao = self.teste_numero_opcoes("Escolha a opção: ", [0,1,2,3,4,5,6])
        print("\n")
        return opcao

    def pega_dados_fornecedor(self):
        print("-------- DADOS FORNECEDOR ----------")
        nome = input("Nome/Razão Social: ")
        cnpj = self.teste_do_cnpj("CNPJ (sem pontos e coisas a mais): ")
        celular = self.teste_do_inteiro("Celular: ")
        produto = self.teste_do_inteiro("Código do produto: ")
        preco = self.teste_do_float("Preço: ")
        return {
            "nome": nome,
            "cnpj": cnpj,
            "celular": celular,
            "produto": produto,
            "preco": preco
        }
=======
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
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe

    def mostra_fornecedor(self, dados_fornecedor):
        print("-------- DADOS DO FORNECEDOR ----------")
        print(f"Nome/Razão Social: {dados_fornecedor['nome']}")
        print(f"CNPJ: {dados_fornecedor['cnpj']}")
        print(f"Celular: {dados_fornecedor['celular']}")
        print(f"Produto: {dados_fornecedor['produto']}")
        print(f"Preço: R${float(dados_fornecedor['preco']):.2f}")
        
        if dados_fornecedor['enderecos']:
            print("Endereços:")
            for endereco in dados_fornecedor['enderecos']:
                print("- Rua: {}, Numero: {}, CEP:{}".format(endereco['rua'], endereco['numero'], endereco['cep']))
        else:
<<<<<<< HEAD
            print("\nFornecedor sem endereços cadastrados.")
        print("\n")

    def pega_dados_endereco(self):
        print("-------- DADOS DO ENDEREÇO ----------")
        cep = self.teste_do_cep("CEP: ")
        rua = input("Rua: ")
        numero = self.teste_do_inteiro("Número: ")
        print("\n")
        return {"cep": cep, "rua": rua, "numero": numero}

    def seleciona_fornecedor(self):
        print("\n")
        return input("Digite o CNPJ do fornecedor: ")

    def seleciona_endereco(self):
        print("\n")
        return input("Digite o CEP do endereço: ")

    def mostra_mensagem(self, msg):
        print(msg)
=======
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
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe
