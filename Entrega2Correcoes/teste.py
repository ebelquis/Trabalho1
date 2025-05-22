from entidade.fornecedor import *
from entidade.vendedor import *
from entidade.cliente import *


    #Produtos
    caneca = Produto("caneca", 1, 20.00, 10)
    camisa = Produto('camisa m', 21, 40.00, 6)
    print(f'{camisa.nome}, {caneca.nome}')
    ControladorProdutos.lista_produtos.append(caneca)
    ControladorProdutos.lista_produtos.append(camisa)

    #fornecedores
    gumege = Fornecedor("Gumege Alumínios", 1111, 4899, caneca, 10.00)
    ControladorFornecedores.fornecedores.append(gumege)
    somar = Fornecedor("Somar", 2222, 549, camisa, 25.00)
    ControladorFornecedores.fornecedores.append(somar)
    print(f'{gumege.nome}, {somar.nome}')

    #vendedores
    djonys = Vendedor('Djonys', 123, 4444, 100)
    ControladorPessoas.lista_vendedores.append(djonys)
    #quando o vendedor vende, precisa aumentar o último atributo

    #clientes
    ravi = Cliente('Ravi', 222, 4433)
    print(f'{djonys.nome}, {ravi.nome}')
    ControladorPessoas.lista_cliente.append(ravi)

    #endereço
    end_gumege = gumege.incluir_endereco('8888', 'rua a', '229')
    print(f'{gumege.lista_enderecos}')
