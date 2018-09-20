import sys

print('=' * 120)
print('=' * 120)
print('=' * 120)
print('  Bem-vindo ao jogo da velha em Python  '.center(120, '='))
print('=' * 120)
print('=' * 120)
print('=' * 120)
print('')

jogar_novamente = False
contador = 0
vitoria_player1 = 0
vitoria_player2 = 0
deu_velha = 0
verifica_jogada = False


def cria_reseta_tab():
    global tab
    tab = [[' ' * 0, ' ' * 1, ' ' * 2], [' ' * 3, ' ' * 4, ' ' * 5], [' ' * 6, ' ' * 7, ' ' * 8]]
    return tab


def aplicar_jogada(x, y):
    global player
    global verifica_jogada
    
    if tab[x][y] != 'X' and tab[x][y] != 'O':
        verifica_jogada = True
        tab[x][y] = player


def monta_primeira():
    c = 0
    for i in tab:
        print('')
        for j in i:
            c += 1
            auxDivisao = ''
            auxObjeto = ''
            confereNumero = c != 3 and c != 6 and c != 9
            confereJogada = str(j).replace(' ', '') == ''
            if confereJogada:
                auxObjeto = c
            else:
                auxObjeto = j

            if confereNumero:
                auxDivisao = '| '
            print(auxObjeto, auxDivisao, end='')


def jogada(move):
    posicoes = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2]
    }

    aplicar_jogada(posicoes[move][0], posicoes[move][1])

    c = 0
    for i in tab:
        print('')
        for j in i:
            c += 1
            auxDivisao = ''
            auxObjeto = ''
            confereNumero = c != 3 and c != 6 and c != 9
            confereJogada = str(j).replace(' ', '') == ''
            if confereJogada:
                auxObjeto = c
            else:
                auxObjeto = j

            if confereNumero:
                auxDivisao = '| '
            print(auxObjeto, auxDivisao, end='')


def letra(let):
    global player1, player2

    player1 = let
    verifica = player1 == 'X'

    if verifica:
        player2 = 'O'
    elif not verifica:
        player1 = 'O'
        player2 = 'X'
    return player1, player2


def check():
    global vitoria
    global velha
    vitoria = False
    velha = False

    condHor1 = tab[0][0] == tab[0][1] == tab[0][2]
    condHor2 = tab[1][0] == tab[1][1] == tab[1][2]
    condHor3 = tab[2][0] == tab[2][1] == tab[2][2]

    condVert1 = tab[0][0] == tab[1][0] == tab[2][0]
    condVert2 = tab[0][1] == tab[1][1] == tab[2][1]
    condVert3 = tab[0][2] == tab[1][2] == tab[2][2]

    condDiag1 = tab[0][0] == tab[1][1] == tab[2][2]
    condDiag2 = tab[0][2] == tab[1][1] == tab[2][0]

    condHorizontal = condHor1 or condHor2 or condHor3
    condVertical = condVert1 or condVert2 or condVert3
    condDiagonal = condDiag1 or condDiag2

    vitoria = condHorizontal or condVertical or condDiagonal

    conta_campo_vazio = 0
    if contador_jogada != 0:
        for i in tab:
            for j in i:
                if not j.replace(' ', '') == '':
                    conta_campo_vazio += 1
    
        if conta_campo_vazio == 9:
            velha = True


def mostra_placar():
    print('')
    print('=' * 50)
    print('  Placar  '.center(50, '='))
    print('=' * 50)
    print('')

    print(vitoria_player1 + vitoria_player2 + deu_velha, ' vez(es) jogadas.')
    print('Empates: ' ,deu_velha)
    print('Player 1: ' ,vitoria_player1)
    print('Player 2: ' ,vitoria_player2)

    if vitoria_player1 > vitoria_player2:
        print('Player 1 na frente!')
    elif vitoria_player2 > vitoria_player2:
        print('Player 2 na frente!')
    elif vitoria_player1 == vitoria_player2:
        print('Empatados!')

    print('')
    print('=' * 50)
    print('')


while not jogar_novamente:
    pergunta_jogar = 'Você deseja jogar? (S/N) '
    if contador > 0:
        pergunta_placar = input('Deseja ver o placar? (S/N) ').upper().replace(' ', '')
        if pergunta_placar == 'S':
            mostra_placar()
        else:
            pass
        pergunta_jogar = 'Você deseja jogar novamente? (S/N) '

    resposta_jogar = input(pergunta_jogar).upper().replace(' ', '')
    
    if resposta_jogar == 'S':
        jogar_novamente = True
        contador += 1
        pass
    elif contador > 0 and not jogar_novamente:
        mostra_placar()
        sys.exit('Adeus, amiguinho <3')
    else:
        continue

    cria_reseta_tab()

    escolha = ''
    while escolha != 'X' and escolha != 'O':
        verificaLetra = escolha != 'X' and escolha != 'O' and escolha != ''

        if verificaLetra:
            print('Letra inválida!\nSelecione X ou O.\n')
        escolha = input('\nQual letra o Player 1 deseja? (X/O)\n').upper().replace(' ', '')
        letra(escolha)

    contador_jogada = 0
    check()
    monta_primeira()
    while not vitoria and not velha:
        vez_jogada = contador_jogada % 2 == 0
        if vez_jogada and not verifica_jogada:
            player = player1
            while not verifica_jogada:
                i = int(input('\n\nVez do Player 1!\nEm que posição deseja jogar? '))
                jogada(i)
                if verifica_jogada:
                    contador_jogada += 1
                else:
                    print('\nNão é possível executar uma jogada neste campo, tente jogar num campo livre.')
                check()
                break
            
            verifica_jogada = False
        else:
            player = player2
            while not verifica_jogada:
                i = int(input('\n\nVez do Player 2!\nEm que posição deseja jogar? '))
                jogada(i)
                if verifica_jogada:
                    contador_jogada += 1
                else:
                    print('\nNão é possível executar uma jogada neste campo, tente jogar num campo livre.')
                check()
                break

            verifica_jogada = False

    if velha:
        deu_velha += 1
        print('\nDeu velha! Pela ', deu_velha, 'ª vez!')
    elif contador_jogada % 2 == 0:
        vitoria_player2 += 1
        print('\nPlayer 2 ganhou ' ,vitoria_player2, ' vez(es).')
    elif contador_jogada % 2 == 1:
        vitoria_player1 += 1
        print('\nPlayer 1 ganhou ' ,vitoria_player1, ' vez(es).')

    jogar_novamente = False
