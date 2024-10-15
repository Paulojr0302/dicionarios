import os

os.system('cls')
folha_pagamento = []
total_folha_pagamento = 0
print('Para parar a entrada de dados, digite "fim" no lugar do nome do funcionário')

nome = str(input('Informe o nome do funcionário: '))
while nome.lower() != "fim":
    funcionario = {
        'registro': input('Informe o número de registro do funcionário: '),
        'nome': nome,
        'horas_trabalhadas': float(input('Informe a quantidade de horas trabalhadas: ')),
        'valor_hora': float(input('Informe o valor da hora: ')),
        'horas_faltantes': float(input('Informe a quantidade de horas faltantes: ')),
        'valor_a_receber': 0.0
    }

    funcionario['valor_a_receber'] = (funcionario['valor_hora'] * funcionario['horas_trabalhadas']) - (funcionario['valor_hora'] * funcionario['horas_faltantes'])
    total_folha_pagamento += funcionario['valor_a_receber']

    folha_pagamento.append(funcionario)

    os.system('cls')
    nome = str(input('Informe o nome do funcionário: '))

os.system('cls')
print("Dados dos funcionários:")
for funcionario in folha_pagamento:
    print(f"Registro: {funcionario['registro']} / Nome: {funcionario['nome']} / Horas Trabalhadas: {funcionario['horas_trabalhadas']} / Valor Hora: {funcionario['valor_hora']} / Horas Faltantes: {funcionario['horas_faltantes']} / Valor a Receber: {funcionario['valor_a_receber']}")

print(f"\nValor total da folha de pagamento: {total_folha_pagamento}")


print("\nhask:")
tabela_hash = {funcionario['registro']: funcionario for funcionario in folha_pagamento}
for registro, dados in tabela_hash.items():
    print(f"Registro: {registro} -> Dados: {dados}")

input('Fim do programa')