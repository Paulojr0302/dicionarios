import os

os.system('cls')
lista_de_compra = []
total_da_compra = 0
print('Para parar a entrada de dados, digite "fim" no lugar do nome do produto')

nome = str(input('Informe qual o item desejado: '))
while nome.lower() != "fim":
    produto = {
        'nome': nome,
        'preco': 0.0,
        'quantidade': 0,
        'total': 0
    }

    produto['preco'] = float(input('Informe o preço do produto informado: '))
    produto['quantidade'] = int(input('Informe a quantidade adquirida: '))
    produto['total'] = produto['preco'] * produto['quantidade']
    total_da_compra += produto['total']

    if produto['preco'] > 0:
        lista_de_compra.append(produto)

    os.system('cls')
    nome = str(input('Informe o nome do produto desejado: '))

os.system('cls')
for produto in lista_de_compra:
    print(f"Produto: {produto['nome']} / Valor unitário: {produto['preco']} / Quantidade: {produto['quantidade']} / Total: {produto['total']}")

print(f"\nTotal da compra: {total_da_compra}")
input('Fim do programa')