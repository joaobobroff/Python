
def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        if n % (m + 1) > 0:
            return n % (m + 1)
        return m


def usuario_escolhe_jogada(n, m):
    tira = int(input('Quantas peças deseja retirar? '))
    while tira > m or tira > n or tira < 1:
        print('\nJogada inválida. Tente novamente.')
        tira = int(input('Quantas peças deseja retirar? '))
    return tira


def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    while n <= 1 or n <= m:
        print('A quantidade de peças não pode ser menor ou igual que o número de jogadas, nem menor que 1. Tente novamente.')
        n = int(input('Quantas peças? '))
    while m >= n or m < 1:
        print('O limite de peças por jogada não pode ser superior ou igual que o número de peças, nem menor que 1. Tente novamente.')
        m = int(input('Limite de peças por jogada? '))
    tira = 0
    jogador = 0
    if n % (m + 1) == 0:
        print('\nVoce começa!')
        jogador = 1
        while n > 0:
            if jogador == 1:
                tira = usuario_escolhe_jogada(n, m)
                if tira > 1:
                    print('\nVocê removeu', tira, 'peças.')
                    n = n - tira
                    print("Agora restam", n, "peças no tabuleiro.\n")
                    jogador = 2
                else:
                    print('\nVocê removeu uma peça.')
                    n = n - tira
                    print("Agora restam", n, "peças no tabuleiro.\n")
                    jogador = 2
            else:
                tira = computador_escolhe_jogada(n, m)
                if tira > 1:
                    print('O computador removeu', tira, 'peças.')
                    n = n - tira
                    print("Agora restam", n, "peças no tabuleiro.\n")
                    jogador = 1
                else:
                    print('O computador removeu uma peça.')
                    n = n - tira
                    print("Agora restam", n, "peças no tabuleiro.\n")
                    jogador = 1
        if jogador == 1:
            print('Fim de jogo! O computador venceu!')
            return 2
        else:
            print('Fim de jogo! Você venceu!')
            return 1

    else:
        print('\nComputador começa!')
        jogador = 2
        while n > 0:
            if jogador == 2:
                tira = computador_escolhe_jogada(n, m)
                if tira > 1:
                    print('O computador removeu', tira, 'peças.')
                    n = n - tira
                    print("Agora restam", n, "peças no tabuleiro.\n")
                    jogador = 1
                else:
                    print('O computador removeu uma peça.')
                    n = n - tira
                    print("Agora restam", n, "peças no tabuleiro.\n")
                    jogador = 1
            else:
                tira = usuario_escolhe_jogada(n, m)
                if tira > 1:
                    print('\nVocê removeu', tira, 'peças.')
                    n = n - tira
                    print("Agora restam", n, "peças no tabuleiro.\n")
                    jogador = 2
                else:
                    print('\nVocê removeu uma peça.')
                    n = n - tira
                    print("Agora restam", n, "peças no tabuleiro.\n")
                    jogador = 2
        if jogador == 1:
            print('Fim de jogo! O computador venceu!')
            return 2
        else:
            print('Fim de jogo! Você venceu!')
            return 1


def campeonato():
    rodada = 1
    placar_computador = placar_usuario = 0
    while rodada < 4:
        print('\n**** Rodada', rodada,'****\n')
        if partida() == 1:
            placar_usuario = placar_usuario + 1
        else:
            placar_computador = placar_computador + 1
        rodada = rodada + 1
    print('**** Fim de campeonato! ****\n')
    print('Placar: Você', placar_usuario,'X', placar_computador,'Computador')


def start():
    print('Bem-vindo ao jogo do NIM! Escolha:\n')
    x = 0
    while x != 1 and x != 2:
        print('1 - para jogar uma partida isolada')
        x = int(input('2 - para jogar um campeonato '))
        if x > 2 or x < 1:
            print("\nOpção inválida, tente novamente:")
    if x == 1:
        print("\nVocê escolheu partida isolada!\n")
        partida()
    else:
        if x == 2:
            print("\nVocê escolheu um campeonato!")
            campeonato()
start()
