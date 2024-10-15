import os

os.system('cls')
atletas = []
print('Para encerrar a entrada de atletas aperte "enter" no lugar do nome do atleta')

atleta = {'nome': 'inicial'}
while atleta['nome'] != "":
    atleta['nome'] = input("Digite o nome do atleta: ")
    if atleta['nome'] == "":
        break

    atleta['saltos'] = []

    for i in range(5):
        distancia = float(input(f"{atleta['nome']}, informe o seu {i + 1}º salto: "))
        atleta['saltos'].append(distancia)

    atleta['saltos'].sort()
    melhor_salto = atleta['saltos'].pop()
    pior_salto = atleta['saltos'].pop(0)
    atleta['media'] = sum(atleta['saltos']) / len(atleta['saltos'])

    print(f"\nAtleta: {atleta['nome']}")
    print(f"Primeiro Salto: {atleta['saltos'][0]} m")
    print(f"Segundo Salto: {atleta['saltos'][1]} m")
    print(f"Terceiro Salto: {atleta['saltos'][2]} m")
    print(f"Melhor salto: {melhor_salto} m")
    print(f"Pior salto: {pior_salto} m")
    print(f"Média dos demais saltos: {atleta['media']:.1f} m")

    atletas.append(atleta.copy())

print("\nResumo dos atletas e seus saltos considerados:")
for atleta in atletas:
    print(f"\nAtleta: {atleta['nome']}")
    print(f"Saltos considerados: {atleta['saltos']}")
    print(f"Média dos saltos: {atleta['media']:.1f} m")