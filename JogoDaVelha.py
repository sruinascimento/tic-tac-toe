tabuleiro = ['-', '-', '-',
             '-', '-', '-',
             '-', '-', '-']


def mostrar_tabuleiro(tabuleiro):
    print(f'{tabuleiro[0]}  {tabuleiro[1]}  {tabuleiro[2]}')
    print(f'{tabuleiro[3]}  {tabuleiro[4]}  {tabuleiro[5]}')
    print(f'{tabuleiro[6]}  {tabuleiro[7]}  {tabuleiro[8]}')
    print()

jogador_x = 'X'
jogador_o = 'O'

def realizar_jogada(tabuleiro, jogador):
    print(f'Turno do jogador = {jogador}')
    indice = int(input('Realize sua jogada, escolha um índice de 0-8: '))
    if tabuleiro[indice] == '-':
        tabuleiro[indice] = jogador
    else:
        print('Jogada inválida')
    mostrar_tabuleiro(tabuleiro)


def checar_vitoria(tabuleiro, jogador):
    if (tabuleiro[0] == jogador and tabuleiro[1] == jogador and tabuleiro[2] == jogador) or \
        (tabuleiro[3] == jogador and tabuleiro[4] == jogador and tabuleiro[5] == jogador) or \
        (tabuleiro[6] == jogador and tabuleiro[7] == jogador and tabuleiro[7] == jogador) or \
        (tabuleiro[0] == jogador and tabuleiro[3] == jogador and tabuleiro[6] == jogador) or \
        (tabuleiro[1] == jogador and tabuleiro[4] == jogador and tabuleiro[7] == jogador) or \
        (tabuleiro[2] == jogador and tabuleiro[5] == jogador and tabuleiro[8] == jogador) or \
        (tabuleiro[0] == jogador and tabuleiro[4] == jogador and tabuleiro[8] == jogador) or \
            (tabuleiro[2] == jogador and tabuleiro[4] == jogador and tabuleiro[6] == jogador):
        print(f'Vencedor = {jogador}')
        return True
    else:
        return False


def checar_empate(tabuleiro):
    if "-" in tabuleiro:
        return False
    else:
        print('Jogo empatado!')
        return True


mostrar_tabuleiro(tabuleiro)
while True:
    realizar_jogada(tabuleiro, jogador_x)
    if checar_vitoria(tabuleiro, jogador_x) or checar_empate(tabuleiro):
        break

    realizar_jogada(tabuleiro, jogador_o)
    if checar_vitoria(tabuleiro, jogador_o) or checar_empate(tabuleiro):
        break
