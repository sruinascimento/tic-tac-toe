tabuleiro = ['-', '-', '-',
             '-', '-', '-',
             '-', '-', '-']

jogador_x = "X"
jogador_o = "O"


def mostrar_tabuleiro(tabuleiro):
    primeira_linha = f'{tabuleiro[0]}  {tabuleiro[1]}  {tabuleiro[2]}'
    segunda_linha = f'{tabuleiro[3]}  {tabuleiro[4]}  {tabuleiro[5]}'
    terceira_linha = f'{tabuleiro[6]}  {tabuleiro[7]}  {tabuleiro[8]}'

    print(primeira_linha)
    print(segunda_linha)
    print(terceira_linha)
    print()

def realizar_jogada(tabuleiro, jogador):
    print(f'Turno do jogador {jogador}')
    indice = int(input('Realize sua jogada, escolha um índice de 0-8 '))
    if tabuleiro[indice] == "-":
        tabuleiro[indice] = jogador
    else:
        print('Jogada inválida!')

def checar_vitoria(tabuleiro, jogador):
    if tabuleiro[0] == jogador and tabuleiro[1] == jogador and tabuleiro[2] == jogador or \
        tabuleiro[3] == jogador and tabuleiro[4] == jogador and tabuleiro[5] == jogador or \
        tabuleiro[6] == jogador and tabuleiro[7] == jogador and tabuleiro[8] == jogador or \
        tabuleiro[0] == jogador and tabuleiro[3] == jogador and tabuleiro[6] == jogador or \
        tabuleiro[1] == jogador and tabuleiro[4] == jogador and tabuleiro[7] == jogador or \
        tabuleiro[2] == jogador and tabuleiro[5] == jogador and tabuleiro[8] == jogador:
        print(f'O jogador {jogador} ganhou o jogo! :)')
        return True
    else:
        return False

def checar_empate(tabuleiro):
    if '-' in tabuleiro:
        return False 
    else:
        print('Jogo empatado! XD')
        return True

mostrar_tabuleiro(tabuleiro)
while True:
    realizar_jogada(tabuleiro, jogador_x)
    mostrar_tabuleiro(tabuleiro)
    if checar_vitoria(tabuleiro, jogador_x) or checar_empate(tabuleiro):
        break
    realizar_jogada(tabuleiro, jogador_o)
    mostrar_tabuleiro(tabuleiro)
    if checar_vitoria(tabuleiro, jogador_o) or checar_empate(tabuleiro):
        break