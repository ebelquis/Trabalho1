from excessoes.OpcaoErroException import OpcaoErroException

class TelaPessoa():
    def tela_opcoes(self):
        print("-------- PESSOAS ----------")
        print("Escolha a opção")
        print("1 - Incluir Pessoa")
        print("2 - Alterar Pessoa")
        print("3 - Listar Clientes")
        print("4 - Listar Vendedores")
        print("5 - Excluir Pessoa")
        print("0 - Retornar")

        try:
            opcao = int(input("Escolha a opcao: "))
            if opcao not in [0, 1, 2, 3, 4, 5]:
                raise OpcaoErroException()
            return opcao
        except OpcaoErroException as e:
            self.mostra_mensagem(e)

    def pega_dados_pessoa(self):
        print("-------- DADOS PESSOA ---------")
        print("Escolha uma opção")
        print("0 - Vendedor")
        print("1 - Cliente")
        try:
            selecionador = input("Escolha a opção: ")
            if selecionador not in [0, 1]:
                raise OpcaoErroException()
            return selecionador
        except OpcaoErroException as e:
           self. mostra_mensagem(e)

        while True:
            try:
                nome = str(input("Nome:"))
                break
            except ValueError:
                print("nome inválido. Insira um nome valido.")

        while True:
            try:
                cpf = int(input("CPF:"))
                break
            except ValueError:
                print("cpf inválido. Insira um valor valido.")
    
        while True:
            try:
                celular = int(input("celular:"))
                break
            except ValueError:
                print("celular inválido. Insira um celular valido.")

        return {"selecionador": selecionador,
                "nome": nome,
                "cpf": cpf,
                "celular": celular}

    def mostra_cliente(self, dados_cliente):
        print("------CLIENTE------")
        print("NOME DO CLIENTE: ", dados_cliente["nome"])
        print("CPF DO CLIENTE: ", dados_cliente["cpf"])
        print("TELEFONE DO CLEINTE: ", dados_cliente["telefone"])
        print("\n")

    def mostra_vendedor(self, dados_vendedor):
        print("------VENDEDOR------")
        print("NOME DO VENDEDOR: ", dados_vendedor["nome"])
        print("CPF DO VENDEDOR: ", dados_vendedor["cpf"])
        print("TELEFONE DO VENDEDOR: ", dados_vendedor["telefone"])
        print("VALOR VENDIDO TOTAL DO VENDEDOR: ", dados_vendedor["valor_vendido_total"])
        print("\n")
    
    def seleciona_pessoa(self):
        print("Escolha uma opção")
        print("0 - Vendedor")
        print("1 - Cliente")

        try:
            selecionador = input("Escolha a opção: ")
            if selecionador not in [0, 1]:
                raise OpcaoErroException()
            return selecionador
        except OpcaoErroException as e:
            self.mostra_mensagem(e)

        while True:
            try:
                cpf = input("CPF da pessoa que deseja selecionar: ")
            except ValueError:
                print("Cpf invalido. Digite novamente.")
        
        return selecionador, cpf

    def mostra_mensagem(self, msg):
        print(msg)