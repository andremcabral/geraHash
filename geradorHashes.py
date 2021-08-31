import hashlib, json
string = input('Informe o texto: ')
menu = 1
while menu > 0:
    menu = int(input('''
             ### MENU ###
        ESCOLHA O FORMATO DA HASH:
        1) MD5
        2) SHA1
        3) SHA256
        4) SHA512
        0) Sair do programa
        Digite o número correspondente:'''))

    if menu == 0:
        print("Programa encerrado")
        exit()
    if menu > 4:
        print("O valor não é válido")
    else:
        # para que o resultado seja exibido temos que usar o hexdigest
        tipoHash = {
            1: {"Resultado":(hashlib.md5(string.encode('utf-8'))).hexdigest(),
                "Tipo":"MD5"
                },
            2: {"Resultado": (hashlib.sha1(string.encode('utf-8'))).hexdigest(),
                "Tipo": "SHA1"
                },
            3: {"Resultado": (hashlib.sha256(string.encode('utf-8'))).hexdigest(),
                "Tipo": "SHA256"
                },
            4: {"Resultado": (hashlib.sha512(string.encode('utf-8'))).hexdigest(),
                "Tipo": "SHA512"
                },
        }
        print(f'\n O hash para o texto: {string},\n no formato: {tipoHash[menu]["Tipo"]},\n é: {tipoHash[menu]["Resultado"]}')