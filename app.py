from random import randint


def gerador() -> tuple:
    cpf = ''
    digito1, digito2 = 0, 0

    # Gerando os 9 primeiros digitos
    for i in range(9):
        cpf += str(randint(0, 9))

    # Gerando o primeiro digito final
    for i, r in enumerate(range(10, 1, -1)):
        digito1 += (int(cpf[i]) * r)

    digito1 = 11 - (digito1 % 11)

    if digito1 > 9:
        digito1 = 0

    cpf += str(digito1)

    # Gerando o segundo digito final
    for i, r in enumerate(range(11, 1, -1)):
        digito2 += (int(cpf[i]) * r)

    digito2 = 11 - (digito2 % 11)

    if digito2 > 9:
        digito2 = 0

    cpf += str(digito2)
    cpf_formatado = ''

    for n in range(len(cpf)):
        cpf_formatado += cpf[n]
        if (n + 1) % 3 == 0 and n < 8:
            cpf_formatado += '.'
        elif n == 8:
            cpf_formatado += '-'

    return cpf, cpf_formatado


cpf = gerador()
print(f'''O CPF gerado foi: {cpf[0]}
Com pontuação: {cpf[1]}''')
