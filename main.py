import os

game = [[['     '], ['     '], ['     ']],
        [['     '], ['     '], ['     ']],
        [['     '], ['     '], ['     ']]]

xis = ['\033[34m  X  \033[m']
ball = ['\033[35m  O  \033[m']

def mostrar_jogo():
    os.system('clear')
    print('-' * 50)
    print(f'{"JOGO DA VELHA!": ^50}')
    print('-' * 50)
    print()
    cont = 0
    for n in game:
        cont += 1
        print(f'                 {n[0][0]}|{n[1][0]}|{n[2][0]}')
        if cont < 3: 
            print(f'                 -----------------')

    print()    
    print('-' * 50)

def deu_velha():
    for linha in game:
        for casa in linha:
            if casa[0] == '     ':
                return False
    return True

def jogada_valida(linha, coluna):
    if game[linha][coluna] == ['     ']:
        return True

def ganhou(simbolo):
    if game[0][0] == game[0][1] == game[0][2] == simbolo or game[1][0] == game[1][1] == game[1][2] == simbolo or game[2][0] == game[2][1] == game[2][2] == simbolo or game[0][0] == game[1][0] == game[2][0] == simbolo or game[0][1] == game[1][1] == game[2][1] == simbolo or game[0][2] == game[1][2] == game[2][2] == simbolo or game[0][0] == game[1][1] == game[2][2] == simbolo or game[0][2] == game[1][1] == game[2][0] == simbolo:
        return True
    return False

while True:
    game = [[['     '], ['     '], ['     ']],
            [['     '], ['     '], ['     ']],
            [['     '], ['     '], ['     ']]]
    mostrar_jogo()
    while True:
        escolhax = input('Player\033[34m[ X ]\033[m faça a sua jogada: ')
        while True:
            if escolhax == '7' and jogada_valida(0, 0):
                game[0][0] = xis
                break
            elif escolhax == '8' and jogada_valida(0, 1):
                game[0][1] = xis
                break
            elif escolhax == '9' and jogada_valida(0, 2):
                game[0][2] = xis
                break
            elif escolhax == '4' and jogada_valida(1, 0):
                game[1][0] = xis
                break
            elif escolhax == '5' and jogada_valida(1, 1):
                game[1][1] = xis
                break
            elif escolhax == '6' and jogada_valida(1, 2):
                game[1][2] = xis
                break
            elif escolhax == '1' and jogada_valida(2, 0):
                game[2][0] = xis
                break
            elif escolhax == '2' and jogada_valida(2, 1):
                game[2][1] = xis
                break
            elif escolhax == '3' and jogada_valida(2, 2):
                game[2][2] = xis
                break
            elif escolhax not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                mostrar_jogo()
                print('\033[31mComando inválido, Tente novamente!\033[m')
                escolhax = input('Player\033[34m[ X ]\033[m faça a sua jogada: ')
            else:
                mostrar_jogo()
                print('\033[31mJogada inválida, tente novamente!\033[m')
            
        mostrar_jogo()

        if ganhou(xis):
            print('\033[32mJogador X ganhou, PARABÉS!\033[m')
            break
        elif deu_velha():
            print('\033[31mDEU VELHA!\033[m')
            break
        
        escolhao = input('Player\033[35m[ O ]\033[m faça a sua jogada: ')
        while True:
            if escolhao == '7' and jogada_valida(0, 0):
                game[0][0] = ball
                break
            elif escolhao == '8' and jogada_valida(0, 1):
                game[0][1] = ball
                break
            elif escolhao == '9' and jogada_valida(0, 2):
                game[0][2] = ball
                break
            elif escolhao == '4' and jogada_valida(1, 0):
                game[1][0] = ball 
                break
            elif escolhao == '5' and jogada_valida(1, 1):
                game[1][1] = ball
                break
            elif escolhao == '6' and jogada_valida(1, 2):
                game[1][2] = ball
                break
            elif escolhao == '1' and jogada_valida(2, 0):
                game[2][0] = ball
                break
            elif escolhao == '2' and jogada_valida(2, 1):
                game[2][1] = ball
                break
            elif escolhao == '3' and jogada_valida(2, 2):
                game[2][2] = ball
                break
            elif escolhao not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                mostrar_jogo()
                print('\033[31mComando inválido, Tente novamente!\033[m')
                escolhao = input('Player\033[35m[ O ]\033[m faça a sua jogada: ')
            else:
                mostrar_jogo()
                print('\033[31mJogada inválida, tente novamente!\033[m')

        mostrar_jogo()

        if ganhou(ball):
            print('\033[32mJogador O ganhou, PARABÉS!\033[m')
            break
        elif deu_velha():
            print('\033[31mDEU VELHA!\033[m')
            break
        
    while True:
        again = input('Quer jogar novamente? ')
        if again[0] in 'Ss':
            break
        elif again[0] not in 'SsNn':
            print('Digite Sim ou Não seu burro!')
            again = input('Quer jogar novamente? ')
        else:
            print('Obrigado por utilizar o programa!')
            break    
        break