print('_' * 40)
print('|')
print('|', end='')
print(' ' * 10, end='')
print('Projeto')
print('|')
print('|', end='     ')
resp = input('deseja começar? {s/n}: ')
print('|')
while (resp not in ('s', 'n')):
    print('|', end='     ')
    resp = input('digite um valor válido {s/n}: ')
campeao = ''
maiormedia = 0
while (resp == 's'):
    print('|', end='     ')
    while True:
        nome = input("Digite o nome do atleta: ")
        valido = False
        for c in nome:
            if c.isalpha() or c.isspace():
                valido = True
            else:
                valido = False
                break
        if valido:
            break
        print("|Nome inválido! Digite novamente usando apenas letras e espaços.")
    print('|')
    while True:
        print('|', end='     ')
        salto = input("Digite o valor do 1º salto: ")
        numeric = False
        ponto = 0
        for c in salto:
            if c.isnumeric():
                numeric = True
            elif c == '.' and ponto == 0:
                ponto += 1
                numeric = True
            else:
                numeric = False
                break
        if numeric:
            p = float(salto)
            break
        print("|     Valor inválido! Digite novamente usando apenas números.")
    maior = p
    menor = p
    soma = p
    for x in range(2, 6):
        while True:
            print('|', end='     ')
            salto = input(f"Digite o valor do {x}º salto: ")
            numeric = False
            ponto = 0
            for c in salto:
                if c.isnumeric():
                    numeric = True
                elif c == '.' and ponto == 0:
                    ponto += 1
                    numeric = True
                else:
                    numeric = False
                    break
            if numeric:
                p = float(salto)
                break
            print("|Valor inválido! Digite novamente usando apenas números.")
        if p > maior:
            maior = p
        elif p < menor:
            menor = p
        soma += p
    media = (soma - maior - menor) / 3
    if (media >= maiormedia):
        maiormedia = media
        campeao = nome
    print('|')
    print('|', end='     ')
    print(
        f'Melhor salto: {maior}m\n|     Pior salto: {menor}m\n|     Média dos demais saltos: {media:.1f}m\n|     Resultado Final:\n|     {nome}: {media:.1f}m')
    print('|')
    print('|', end='     ')
    resp = input('deseja continuar? {s/n}: ')
    while (resp not in ('s', 'n')):
        print('|', end='     ')
        resp = input('digite um valor válido {s/n}: ')
if campeao:
    print('|')
    print('|', end='     ')
    print("ATLETA CAMPEÃO: ", campeao.upper())
print('|', end='')
print('_' * 40)
