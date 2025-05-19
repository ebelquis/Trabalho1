from cliente import Cliente
from fornecedor import Fornecedor
from pedido import Pedido
from produto import Produto
from transacao import Transacao
from venda import Venda
from vendedor import Vendedor
from datetime import datetime

produto1 = Produto("Caneca", "Caneca 600mL", 35.00, 10)
produto2 = Produto("Camisa", "Camisa código", 60.00, 20)

fornecedor = Fornecedor("Farol", 123456789, 999888777, produto1, 12.00)

vendedor1 = Vendedor("João", 999111222, 0.00)

cliente1 = Cliente("Maria", 988776655)

pedido = Pedido(10, produto1, datetime.now(), 14.00, fornecedor, 10.00, 14)

venda1 = Venda(1, produto2, datetime.now(), 60.0, cliente1, vendedor1)

#Atualizar valor vendido
vendedor1.valor_vendido_total += venda1.valor

# Exibindo informações
print(f"Cliente: {venda1.cliente.nome}")
print(f"Vendedor: {vendedor1.nome}")
#print(f"Total do pedido: R${pedido.calcular_total():.2f}")
print(f"Total vendido pelo vendedor: R${vendedor1.valor_vendido_total:.2f}")