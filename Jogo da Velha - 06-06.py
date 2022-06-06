
# --------------------------------------------------------------- [ Variáveis ]

contador = 1
linha1 = [1, 2, 3]
linha2 = [4, 5, 6]
linha3 = [7, 8, 9]
vez = "X"

# --------------------------------------------------------------- [ While ]

while contador < 10:
    contador = contador + 1
    print(linha1)
    print(linha2)
    print(linha3)
    print("Jogador da vez: ", vez)
    posicao = int(input("Qual posição você deseja jogar?: "))
    print("")

    # --------------------------------------------------------------- [ Condições ]

    if posicao < 1 or posicao > 9:
        posicao = int(input("Qual posição você deseja jogar?: "))
        print("")
    if posicao == 1 or posicao == 2 or posicao == 3:
        linha1[posicao - 1] = vez
    elif posicao == 4 or posicao == 5 or posicao == 6:
        linha2[posicao - 4] = vez
    else:
        linha3[posicao - 7] = vez

    # --------------------------------------------------------------- [ Altera "Naipe" ]

    if vez == "X":
        vez = "O"
    else:
        vez = "X"

    # ------------------------------------------------------ [ Horizontal ]

    if linha1[0] == linha1[1] == linha1[2]:
        contador = 10
        print("O vencedor é:",linha1[0])

    elif linha2[0] == linha2[1] == linha2[2]:
        contador = 10
        print("O vencedor é:", linha2[0])

    elif linha3[0] == linha3[1] == linha3[2]:
        contador = 10
        print("O vencedor é:", linha3[0])

    # ------------------------------------------------------ [ Diagonal ]

    elif linha1[0] == linha2[1] == linha3[2]:
        contador = 10
        print("O vencedor é:", linha1[0])

    elif linha1[2] == linha2[1] == linha3[0]:
        contador = 10
        print("O vencedor é:", linha1[2])

    # ------------------------------------------------------  [ Vertical ]

    elif linha1[0] == linha2[0] == linha3[0]:
        contador = 10
        print("O vencedor é:", linha1[0])

    elif linha1[1] == linha2[1] == linha3[1]:
        contador = 10
        print("O vencedor é:", linha1[1])

    elif linha1[2] == linha2[2] == linha3[2]:
        contador = 10
        print("O vencedor é:", linha1[2])

    print(linha1)
    print(linha2)
    print(linha3)

    # ------------------------------------------------------------------------------------------------------------------
