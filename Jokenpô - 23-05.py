print('Jogo do Pedra, Papel e Tesoura')
jogador1 = input('Jogador 1 você escolhe Pedra, Papel ou Tesoura?\n:')
jogador2 = input('Jogador 2 você escolhe Pedra, Papel ou Tesoura?\n:')
if jogador1 == 'Pedra':
    if jogador2 == 'Pedra':
        print("Empatou!")
    else:
        if jogador2 == 'Papel':
            print('Jogador 2 Venceu!')
        else:
            print("Jogador 1 Venceu")
elif jogador1 == 'Papel':
    if jogador2 == 'Pedra':
        print("Jogador 1 Venceu")
    elif jogador2 == 'Papel':
        print("Empatou!")
    else:
        print("Jogador 2 Venceu")
else:
    if jogador2 == 'Pedra':
        print("Jogador 2 Venceu")
    elif jogador2 == 'Papel':
        print("Jogador 1 Venceu!")
    else:
        print("Empatou!")