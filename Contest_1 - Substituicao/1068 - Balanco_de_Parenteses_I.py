feira = {}

def produtos_disponiveis(qtd_produto):
    global feira
    for item in range(qtd_produto):
        produto, preco = input().split(" ")
        feira[produto] = float(preco)
    return feira

def compra(qtd_lista):
    valor_compra = 0
    for i in range(qtd_lista):
        produto, quantidade = input().split(" ")
        if produto in feira:
            valor_compra += feira[produto] *int(quantidade)
    return valor_compra

qtd_ida_feira = int(input())
for i in range(qtd_ida_feira):
    qtd_produto_disponivel = int(input())
    produtos_disponiveis(qtd_produto_disponivel)
    itens_a_comprar = int(input())
    print("R$ %.2f" %compra(itens_a_comprar))

