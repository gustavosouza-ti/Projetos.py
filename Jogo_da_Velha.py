#Jogo da Velha

m = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]   # tabuleiro inicial numerado
jogadas = 0   # conta quantas casas já foram preenchidas (usado para detectar empate)

def jogo_da_velha():
    print("Jogo da Velha:")
    for l in range(3):
        for c in range(3):
            print(f"[{m[l][c]}]", end=" ")
        print()


while True:
    jogo_da_velha()
# VEZ DO JOGADOR 1
    j1 = int(input(f"Jogador 1, escolha uma posição para colocar X (1-9): "))
    pos1 = int(j1)-1 
    l = (pos1) // 3   # converte a posição (1-9) em linha...
    c = (pos1) % 3     # ...e coluna da matriz


    if m[l][c] != "X" and m[l][c] != "O":
                m[l][c] = "X"
    else :
         print("Posição já ocupada, escolha outra posição.")
         continue
    jogo_da_velha()
    jogadas += 1
    if (
# linhas
    (m[0][0] == m[0][1] == m[0][2]) or
    (m[1][0] == m[1][1] == m[1][2]) or
    (m[2][0] == m[2][1] == m[2][2]) or
#colunas
    (m[0][0] == m[1][0] == m[2][0]) or
    (m[0][1] == m[1][1] == m[2][1]) or
    (m[0][2] == m[1][2] == m[2][2]) or
#diagonal
    (m[0][2] == m[1][1] == m[2][0]) or
    (m[0][0] == m[1][1] == m[2][2])
    
    ):
        print("Jogador 1 venceu!")
        break

    if jogadas == 9:
        print("Deu velha! Ninguém ganhou.")
        break

# VEZ DO JOGADOR 2
    j2 = input(f"Jogador 2, escolha uma posição para colocar O (1-9): ")
    pos2 = int(j2)-1
    l = (pos2) // 3
    c = (pos2) % 3 


    if m[l][c] != "X" and m[l][c] != "O":
        m[l][c] = "O"
    else:
        print("Posição já ocupada, escolha outra posição.")
        continue
    jogo_da_velha()
    jogadas += 1
    if (
# linhas
    (m[0][0] == m[0][1] == m[0][2]) or
    (m[1][0] == m[1][1] == m[1][2]) or
    (m[2][0] == m[2][1] == m[2][2]) or
#colunas
    (m[0][0] == m[1][0] == m[2][0]) or
    (m[0][1] == m[1][1] == m[2][1]) or
    (m[0][2] == m[1][2] == m[2][2]) or
#diagonal
    (m[0][2] == m[1][1] == m[2][0]) or
    (m[0][0] == m[1][1] == m[2][2])
    
    ):
        print("Jogador 2 venceu!")
        break

    if jogadas == 9:
        print("Deu velha! Ninguém ganhou.")
        break



print ("Fim de jogo!")