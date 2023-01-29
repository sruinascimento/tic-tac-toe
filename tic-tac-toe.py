tabuleiro = ['-', '-', '-',
    '-', '-', '-',
    '-', '-', '-']

jogador_vencedor = None
jogo_finalizado = False

def mostrar_tabuleiro(tabuleiro):
    print(f'{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}')
    print('---------')
    print(f'{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}')
    print('---------')
    print(f'{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}')
    print()


def realizar_jogada(tabuleiro, jogador):
    print(f'Turno do jogador {jogador}')
    indice = int(input('Digite um valor de 0-9 para realizar sua jogada '))
    if tabuleiro[indice] == '-':
        tabuleiro[indice] = jogador
    else:
        print('Jogada inválida')

def checar_vitoria_horizontal(tabuleiro:list) -> bool:
    global jogador_vencedor
    if tabuleiro[0] == tabuleiro[1] == tabuleiro[2] and tabuleiro[0] != '-':
        jogador_vencedor = tabuleiro[0]
        return True

    if tabuleiro[3] == tabuleiro[4] == tabuleiro[5] and tabuleiro[4] != '-':
        jogador_vencedor = tabuleiro[3]
        return True
    
    if tabuleiro[6] == tabuleiro[7] == tabuleiro[8] and tabuleiro[8] != '-':
        jogador_vencedor = tabuleiro[6]
        return True

    return False

def checar_vitoria_vertical(tabuleiro:list) -> bool: 
    global jogador_vencedor
    if tabuleiro[0] == tabuleiro[3] == tabuleiro[6] and tabuleiro[0] != '-':
        jogador_vencedor = tabuleiro[0]
        return True

    if tabuleiro[1] == tabuleiro[4] == tabuleiro[7] and tabuleiro[1] != '-':
        jogador_vencedor = tabuleiro[1]
        return True

    if tabuleiro[2] == tabuleiro[5] == tabuleiro[8] and tabuleiro[2] != '-':
        jogador_vencedor = tabuleiro[2]
        return True

    return False

def checar_vitoria_diagonal(tabuleiro:list) -> bool:
    global jogador_vencedor
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] and tabuleiro[0] != '-':
        jogador_vencedor = tabuleiro[0]
        return True
    
    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] and tabuleiro[2] != '-':
        jogador_vencedor = tabuleiro[0]
        return True

    return False

def checar_vencedor(tabuleiro) -> bool:
    global jogo_finalizado
    if checar_vitoria_horizontal(tabuleiro) or checar_vitoria_vertical(tabuleiro) or checar_vitoria_diagonal(tabuleiro):
        jogo_finalizado = True
        print(f'Jogador {jogador_vencedor} é o vencedor XD')
    return jogo_finalizado

def checar_empate(tabuleiro:list) -> bool:
    global jogo_finalizado 
    if '-' not in tabuleiro:
        print('Jogo empate!')
        jogo_finalizado = True
        return True
    return False
    
while not jogo_finalizado:
    mostrar_tabuleiro(tabuleiro)
    realizar_jogada(tabuleiro, 'X')
    mostrar_tabuleiro(tabuleiro)
    if checar_vencedor(tabuleiro) or checar_empate(tabuleiro):
        continue

    realizar_jogada(tabuleiro, 'O')
    mostrar_tabuleiro(tabuleiro)
    if checar_vencedor(tabuleiro) or checar_empate(tabuleiro):
        continue


# Desafio controlar jogadas inválidas e fazer um robô.