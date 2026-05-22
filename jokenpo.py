print(f'Digitem suas jogadas (pedra, papel, tesoura)')
print(f'Jogador 1: ')
player1 = str(input().upper())
print(f'Jogador 2: ')
player2 = str(input().upper())

#A linha 18 existe dessa forma para tratar quando player1 == player2, mas ambas são respostas inválidas para o jogo.
#Isso não seria tratado como estava antes em: 
#if (player1 == player2):
#   print('Empate!')
#elif ((player1 == 'PEDRA' and player2 == 'PAPEL') or (player1 == 'PAPEL' and player2 == 'TESOURA') or (player1 == 'TESOURA' and player2 == 'PEDRA')):
#   print ('Jogador 2 venceu!')
#elif ((player1 == 'PEDRA' and player2 == 'TESOURA') or (player1 == 'PAPEL' and player2 == 'PEDRA') or (player1 == 'TESOURA' and player2 == 'PAPEL')):
#   print ('Jogador 1 venceu!') 
#else:
#   print ('Entrada nao reconhecida.')

if ((player1 != 'PEDRA' and player1 != 'PAPEL' and player1 != 'TESOURA') or (player2 != 'PEDRA' and player2 != 'PAPEL' and player2 != 'TESOURA')):
    print ('Entrada nao reconhecida.') 
else:
    if (player1 == player2):
      print('Empate!')
    elif ((player1 == 'PEDRA' and player2 == 'PAPEL') or (player1 == 'PAPEL' and player2 == 'TESOURA') or (player1 == 'TESOURA' and player2 == 'PEDRA')):
        print ('Jogador 2 venceu!')
    elif ((player1 == 'PEDRA' and player2 == 'TESOURA') or (player1 == 'PAPEL' and player2 == 'PEDRA') or (player1 == 'TESOURA' and player2 == 'PAPEL')):
        print ('Jogador 1 venceu!') 
