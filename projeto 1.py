from random import choice
from sys import exit
from time import sleep
print('{:=^60}'.format('JOKENPÔ'))
print('\n')
print('{:=^60}'.format('BEM VINDO'))
c = 50
loja = ['prata',' ouro', 'diamante']
inv = []
while True:
    j = str(input('Você deseja jogar? [\033[1;32mS\033[m/\033[1;31mN\033[m]\n')).upper().strip()[0]
    if j == 'S':
     print('Prepare-se!!\n')
     sleep(1)
     print('Você irá ter uma carteira com um valor de \033[1;36m50 pontos\033[m!')
     sleep(1)
     print('O objetivo do jogo consiste em comprar todos os itens da loja!')
     sleep(1)
     print('Perde o jogo se ficar com \033[1;31mpontos negativos\033[m na carteira!')
     sleep(1)
     print('Uma vitoria dá \033[1;32m20 pontos\033[m, um empate dá \033[1;33m5 pontos\033[m e uma derrota retira \033[1;31m10 pontos\033[m!')
     while True:
         n = ('pedra', 'papel', 'tesoura')
         while True:
            n1 = str(input('\nFaça a sua jogada! '
                           '\n1. Pedra\n'
                           '2. Papel\n'
                           '3. Tesoura\n')).lower().strip()
            if n1 == 'pedra' or n1 == 'papel' or n1 == 'tesoura':
                break
         pc = choice(n)
         print('JO')
         sleep(0.3)
         print('KEN')
         sleep(0.3)
         print('PÔ')
         if n1 == 'pedra' and pc == 'pedra':
             print('\n\033[1;33mEMPATE\033[m')
             print(f'Você escolheu \033[1;33m{n1}\033[m e o computador escolheu \033[1;33m{pc}\033[m ')
             c = c + 5
             print(f'Ganhou \033[1;33m5 pontos\033[m para a sua carteira, tendo agora \033[1;36m{c} pontos\033[m')
             sleep(1)
             print('\n')
             while True:
                 print('MENU')
                 print('1. Continuar\n'
                       '2. Loja\n'
                       '3. Sair do jogo\n'
                       '4. Mostrar Inventário')
                 m = int(input('Qual das opções deseja?'))
                 if m == 1:
                     break
                 elif m == 2 and loja[0] == 'diamante':
                     sleep(0.3)
                     print('\n')
                     print('{:=^60}'.format('LOJA'))
                     print('Prata == 100 pontos\n'
                           'Ouro == 200 pontos\n'
                           'Diamante == 300 pontos')
                     print('{:=^60}'.format('LOJA'))
                     print('\n')
                     print('O que deseja fazer?')
                     print('1. Comprar\n'
                           '2. Sair da loja\n')
                     s = int(input())
                     if s == 1:
                         print('{:=^60}'.format('LOJA'))
                         print('1. Upgrade Final?\n')
                         print('{:=^60}'.format('LOJA'))
                         s1 = int(input())
                         if s1 == 1:
                             print('COMPRANDO . . .')
                             if c >= 300:
                                 sleep(0.3)
                                 c = c - 300
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou o Diamante e ficou com {c} pontos na carteira')
                                 sleep(0.3)
                                 if  inv[2] == 'diamante':
                                    print('VOCÊ COMPLETOU O JOGO\nParabéns!!')
                                    exit('FIM')
                             else:
                                 print('Você não tem pontos suficientes!!')

                 elif m == 2:
                     sleep(0.3)
                     print('\n')
                     print('{:=^60}'.format('LOJA'))
                     print('Prata == 100 pontos\n'
                           'Ouro == 200 pontos\n'
                           'Diamante == 300 pontos')
                     print('{:=^60}'.format('LOJA'))
                     print('\n')
                     print('O que deseja fazer?')
                     print('1. Comprar\n'
                           '2. Sair da loja\n')
                     s = int(input())
                     if s == 1:
                         print('{:=^60}'.format('LOJA'))
                         print('1. Upgrade?\n')
                         print('{:=^60}'.format('LOJA'))
                         s1 = int(input())
                         if s1 == 1 and inv == []:
                             print('COMPRANDO . . .')
                             if c >= 100:
                                 sleep(0.3)
                                 c = c - 100
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou a Prata e ficou com {c} pontos na carteira')
                             else:
                                 print('Você não tem pontos suficientes!!')
                         elif s1 == 1 and inv[0] == 'prata':
                             print('COMPRANDO . . .')
                             if c >= 200:
                                 sleep(0.3)
                                 c = c - 200
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou o Ouro e ficou com {c} pontos na carteira')
                             else:
                                 print('Você não tem pontos suficientes!!')

                 elif m == 3:
                     exit('FIM')
                 elif m == 4:
                     print(f'{inv}\n')
                 else:
                     print('Tente novamente')

         elif n1 == 'tesoura' and pc == 'tesoura':
             print('\n\033[1;33mEMPATE\033[m')
             print(f'Você escolheu \033[1;33m{n1}\033[m e o computador escolheu \033[1;33m{pc}\033[m')
             c = c + 5
             print(f'Ganhou \033[1;33m5 pontos\033[m para a sua carteira, tendo agora \033[1;36m{c} pontos\033[m')
             sleep(1)
             print('\n')
             while True:
                 print('MENU')
                 print('1. Continuar\n'
                       '2. Loja\n'
                       '3. Sair do jogo\n'
                       '4. Mostrar Inventário')
                 m = int(input('Qual das opções deseja?'))
                 if m == 1:
                     break
                 elif m == 2 and loja[0] == 'diamante':
                     sleep(0.3)
                     print('\n')
                     print('{:=^60}'.format('LOJA'))
                     print('Prata == 100 pontos\n'
                           'Ouro == 200 pontos\n'
                           'Diamante == 300 pontos')
                     print('{:=^60}'.format('LOJA'))
                     print('\n')
                     print('O que deseja fazer?')
                     print('1. Comprar\n'
                           '2. Sair da loja\n')
                     s = int(input())
                     if s == 1:
                         print('{:=^60}'.format('LOJA'))
                         print('1. Upgrade Final?\n')
                         print('{:=^60}'.format('LOJA'))
                         s1 = int(input())
                         if s1 == 1:
                             print('COMPRANDO . . .')
                             if c >= 300:
                                 sleep(0.3)
                                 c = c - 300
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou o Diamante e ficou com {c} pontos na carteira')
                                 sleep(0.3)
                                 if inv[2] == 'diamante':
                                     print('VOCÊ COMPLETOU O JOGO\nParabéns!!')
                                     exit('FIM')
                             else:
                                 print('Você não tem pontos suficientes!!')

                 elif m == 2:
                     sleep(0.3)
                     print('\n')
                     print('{:=^60}'.format('LOJA'))
                     print('Prata == 100 pontos\n'
                           'Ouro == 200 pontos\n'
                           'Diamante == 300 pontos')
                     print('{:=^60}'.format('LOJA'))
                     print('\n')
                     print('O que deseja fazer?')
                     print('1. Comprar\n'
                           '2. Sair da loja\n')
                     s = int(input())
                     if s == 1:
                         print('{:=^60}'.format('LOJA'))
                         print('1. Upgrade?\n')
                         print('{:=^60}'.format('LOJA'))
                         s1 = int(input())
                         if s1 == 1 and inv == []:
                             print('COMPRANDO . . .')
                             if c >= 100:
                                 sleep(0.3)
                                 c = c - 100
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou a Prata e ficou com {c} pontos na carteira')
                             else:
                                 print('Você não tem pontos suficientes!!')
                         elif s1 == 1 and inv[0] == 'prata':
                             print('COMPRANDO . . .')
                             if c >= 200:
                                 sleep(0.3)
                                 c = c - 200
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou o Ouro e ficou com {c} pontos na carteira')
                             else:
                                 print('Você não tem pontos suficientes!!')

                 elif m == 3:
                     exit('FIM')
                 elif m == 4:
                     print(f'{inv}\n')
                 else:
                     print('Tente novamente')

         elif n1 == 'papel' and pc == 'papel':
             print('\n\033[1;33mEMPATE\033[m')
             print(f'Você escolheu \033[1;33m{n1}\033[m e o computador escolheu \033[1;33m{pc}\033[m')
             c = c + 5
             print(f'Ganhou \033[1;33m5 pontos\033[m para a sua carteira, tendo agora \033[1;36m{c} pontos\033[m')
             sleep(1)
             print('\n')
             while True:
                 print('MENU')
                 print('1. Continuar\n'
                       '2. Loja\n'
                       '3. Sair do jogo\n'
                       '4. Mostrar Inventário')
                 m = int(input('Qual das opções deseja?'))
                 if m == 1:
                     break
                 elif m == 2 and loja[0] == 'diamante':
                     sleep(0.3)
                     print('\n')
                     print('{:=^60}'.format('LOJA'))
                     print('Prata == 100 pontos\n'
                           'Ouro == 200 pontos\n'
                           'Diamante == 300 pontos')
                     print('{:=^60}'.format('LOJA'))
                     print('\n')
                     print('O que deseja fazer?')
                     print('1. Comprar\n'
                           '2. Sair da loja\n')
                     s = int(input())
                     if s == 1:
                         print('{:=^60}'.format('LOJA'))
                         print('1. Upgrade Final?\n')
                         print('{:=^60}'.format('LOJA'))
                         s1 = int(input())
                         if s1 == 1:
                             print('COMPRANDO . . .')
                             if c >= 300:
                                 sleep(0.3)
                                 c = c - 300
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou o Diamante e ficou com {c} pontos na carteira')
                                 sleep(0.3)
                                 if inv[2] == 'diamante':
                                     print('VOCÊ COMPLETOU O JOGO\nParabéns!!')
                                     exit('FIM')
                             else:
                                 print('Você não tem pontos suficientes!!')

                 elif m == 2:
                     sleep(0.3)
                     print('\n')
                     print('{:=^60}'.format('LOJA'))
                     print('Prata == 100 pontos\n'
                           'Ouro == 200 pontos\n'
                           'Diamante == 300 pontos')
                     print('{:=^60}'.format('LOJA'))
                     print('\n')
                     print('O que deseja fazer?')
                     print('1. Comprar\n'
                           '2. Sair da loja\n')
                     s = int(input())
                     if s == 1:
                         print('{:=^60}'.format('LOJA'))
                         print('1. Upgrade?\n')
                         print('{:=^60}'.format('LOJA'))
                         s1 = int(input())
                         if s1 == 1 and inv == []:
                             print('COMPRANDO . . .')
                             if c >= 100:
                                 sleep(0.3)
                                 c = c - 100
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou a Prata e ficou com {c} pontos na carteira')
                             else:
                                 print('Você não tem pontos suficientes!!')
                         elif s1 == 1 and inv[0] == 'prata':
                             print('COMPRANDO . . .')
                             if c >= 200:
                                 sleep(0.3)
                                 c = c - 200
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou o Ouro e ficou com {c} pontos na carteira')
                             else:
                                 print('Você não tem pontos suficientes!!')

                 elif m == 3:
                     exit('FIM')
                 elif m == 4:
                     print(f'{inv}\n')
                 else:
                     print('Tente novamente')

         elif n1 == 'papel' and pc == 'pedra':
             print('\n\033[1;32mVOCÊ GANHOU!\033[m')
             print(f'Você escolheu \033[1;32m{n1}\033[m e o computador escolheu \033[1;31m{pc}\033[m')
             c = c + 20
             print(f'Ganhou \033[1;32m20 pontos\033[m para a sua carteira, tendo agora \033[1;36m{c} pontos\033[m')
             sleep(1)
             while True:
                 print('MENU')
                 print('1. Continuar\n'
                       '2. Loja\n'
                       '3. Sair do jogo\n'
                       '4. Mostrar Inventário')
                 m = int(input('Qual das opções deseja?'))
                 if m == 1:
                     break
                 elif m == 2 and loja[0] == 'diamante':
                     sleep(0.3)
                     print('\n')
                     print('{:=^60}'.format('LOJA'))
                     print('Prata == 100 pontos\n'
                           'Ouro == 200 pontos\n'
                           'Diamante == 300 pontos')
                     print('{:=^60}'.format('LOJA'))
                     print('\n')
                     print('O que deseja fazer?')
                     print('1. Comprar\n'
                           '2. Sair da loja\n')
                     s = int(input())
                     if s == 1:
                         print('{:=^60}'.format('LOJA'))
                         print('1. Upgrade Final?\n')
                         print('{:=^60}'.format('LOJA'))
                         s1 = int(input())
                         if s1 == 1:
                             print('COMPRANDO . . .')
                             if c >= 300:
                                 sleep(0.3)
                                 c = c - 300
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou o Diamante e ficou com {c} pontos na carteira')
                                 sleep(0.3)
                                 if inv[2] == 'diamante':
                                     print('VOCÊ COMPLETOU O JOGO\nParabéns!!')
                                     exit('FIM')
                             else:
                                 print('Você não tem pontos suficientes!!')

                 elif m == 2:
                     sleep(0.3)
                     print('\n')
                     print('{:=^60}'.format('LOJA'))
                     print('Prata == 100 pontos\n'
                           'Ouro == 200 pontos\n'
                           'Diamante == 300 pontos')
                     print('{:=^60}'.format('LOJA'))
                     print('\n')
                     print('O que deseja fazer?')
                     print('1. Comprar\n'
                           '2. Sair da loja\n')
                     s = int(input())
                     if s == 1:
                         print('{:=^60}'.format('LOJA'))
                         print('1. Upgrade?\n')
                         print('{:=^60}'.format('LOJA'))
                         s1 = int(input())
                         if s1 == 1 and inv == []:
                             print('COMPRANDO . . .')
                             if c >= 100:
                                 sleep(0.3)
                                 c = c - 100
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou a Prata e ficou com {c} pontos na carteira')
                             else:
                                 print('Você não tem pontos suficientes!!')
                         elif s1 == 1 and inv[0] == 'prata':
                             print('COMPRANDO . . .')
                             if c >= 200:
                                 sleep(0.3)
                                 c = c - 200
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou o Ouro e ficou com {c} pontos na carteira')
                             else:
                                 print('Você não tem pontos suficientes!!')

                 elif m == 3:
                     exit('FIM')
                 elif m == 4:
                     print(f'{inv}\n')
                 else:
                     print('Tente novamente')

         elif n1 == 'pedra' and pc == 'tesoura':
             print('\n\033[1;32mVOCÊ GANHOU!\033[m')
             print(f'Você escolheu \033[1;32m{n1}\033[m e o computador escolheu \033[1;31m{pc}\033[m')
             c = c + 20
             print(f'Ganhou \033[1;32m20 pontos\033[m para a sua carteira, tendo agora \033[1;36m{c} pontos\033[m')
             sleep(1)
             print('\n')
             while True:
                 print('MENU')
                 print('1. Continuar\n'
                       '2. Loja\n'
                       '3. Sair do jogo\n'
                       '4. Mostrar Inventário')
                 m = int(input('Qual das opções deseja?'))
                 if m == 1:
                     break
                 elif m == 2 and loja[0] == 'diamante':
                     sleep(0.3)
                     print('\n')
                     print('{:=^60}'.format('LOJA'))
                     print('Prata == 100 pontos\n'
                           'Ouro == 200 pontos\n'
                           'Diamante == 300 pontos')
                     print('{:=^60}'.format('LOJA'))
                     print('\n')
                     print('O que deseja fazer?')
                     print('1. Comprar\n'
                           '2. Sair da loja\n')
                     s = int(input())
                     if s == 1:
                         print('{:=^60}'.format('LOJA'))
                         print('1. Upgrade Final?\n')
                         print('{:=^60}'.format('LOJA'))
                         s1 = int(input())
                         if s1 == 1:
                             print('COMPRANDO . . .')
                             if c >= 300:
                                 sleep(0.3)
                                 c = c - 300
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou o Diamante e ficou com {c} pontos na carteira')
                                 sleep(0.3)
                                 if inv[2] == 'diamante':
                                     print('VOCÊ COMPLETOU O JOGO\nParabéns!!')
                                     exit('FIM')
                             else:
                                 print('Você não tem pontos suficientes!!')

                 elif m == 2:
                     sleep(0.3)
                     print('\n')
                     print('{:=^60}'.format('LOJA'))
                     print('Prata == 100 pontos\n'
                           'Ouro == 200 pontos\n'
                           'Diamante == 300 pontos')
                     print('{:=^60}'.format('LOJA'))
                     print('\n')
                     print('O que deseja fazer?')
                     print('1. Comprar\n'
                           '2. Sair da loja\n')
                     s = int(input())
                     if s == 1:
                         print('{:=^60}'.format('LOJA'))
                         print('1. Upgrade?\n')
                         print('{:=^60}'.format('LOJA'))
                         s1 = int(input())
                         if s1 == 1 and inv == []:
                             print('COMPRANDO . . .')
                             if c >= 100:
                                 sleep(0.3)
                                 c = c - 100
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou a Prata e ficou com {c} pontos na carteira')
                             else:
                                 print('Você não tem pontos suficientes!!')
                         elif s1 == 1 and inv[0] == 'prata':
                             print('COMPRANDO . . .')
                             if c >= 200:
                                 sleep(0.3)
                                 c = c - 200
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou o Ouro e ficou com {c} pontos na carteira')
                             else:
                                 print('Você não tem pontos suficientes!!')

                 elif m == 3:
                     exit('FIM')
                 elif m == 4:
                     print(f'{inv}\n')
                 else:
                     print('Tente novamente')

         elif n1 == 'tesoura' and pc == 'papel':
             print('\n\033[1;32mVOCÊ GANHOU!\033[m')
             print(f'Você escolheu \033[1;32m{n1}\033[m e o computador escolheu \033[1;31m{pc}\033[m')
             c = c + 20
             print(f'Ganhou \033[1;32m20 pontos\033[m para a sua carteira, tendo agora \033[1;36m{c} pontos\033[m')
             sleep(1)
             print('\n')
             while True:
                 print('MENU')
                 print('1. Continuar\n'
                       '2. Loja\n'
                       '3. Sair do jogo\n'
                       '4. Mostrar Inventário')
                 m = int(input('Qual das opções deseja?'))
                 if m == 1:
                     break
                 elif m == 2 and loja[0] == 'diamante':
                     sleep(0.3)
                     print('\n')
                     print('{:=^60}'.format('LOJA'))
                     print('Prata == 100 pontos\n'
                           'Ouro == 200 pontos\n'
                           'Diamante == 300 pontos')
                     print('{:=^60}'.format('LOJA'))
                     print('\n')
                     print('O que deseja fazer?')
                     print('1. Comprar\n'
                           '2. Sair da loja\n')
                     s = int(input())
                     if s == 1:
                         print('{:=^60}'.format('LOJA'))
                         print('1. Upgrade Final?\n')
                         print('{:=^60}'.format('LOJA'))
                         s1 = int(input())
                         if s1 == 1:
                             print('COMPRANDO . . .')
                             if c >= 300:
                                 sleep(0.3)
                                 c = c - 300
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou o Diamante e ficou com {c} pontos na carteira')
                                 sleep(0.3)
                                 if inv[2] == 'diamante':
                                     print('VOCÊ COMPLETOU O JOGO\nParabéns!!')
                                     exit('FIM')
                             else:
                                 print('Você não tem pontos suficientes!!')

                 elif m == 2:
                     sleep(0.3)
                     print('\n')
                     print('{:=^60}'.format('LOJA'))
                     print('Prata == 100 pontos\n'
                           'Ouro == 200 pontos\n'
                           'Diamante == 300 pontos')
                     print('{:=^60}'.format('LOJA'))
                     print('\n')
                     print('O que deseja fazer?')
                     print('1. Comprar\n'
                           '2. Sair da loja\n')
                     s = int(input())
                     if s == 1:
                         print('{:=^60}'.format('LOJA'))
                         print('1. Upgrade?\n')
                         print('{:=^60}'.format('LOJA'))
                         s1 = int(input())
                         if s1 == 1 and inv == []:
                             print('COMPRANDO . . .')
                             if c >= 100:
                                 sleep(0.3)
                                 c = c - 100
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou a Prata e ficou com {c} pontos na carteira')
                             else:
                                 print('Você não tem pontos suficientes!!')
                         elif s1 == 1 and inv[0] == 'prata':
                             print('COMPRANDO . . .')
                             if c >= 200:
                                 sleep(0.3)
                                 c = c - 200
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou o Ouro e ficou com {c} pontos na carteira')
                             else:
                                 print('Você não tem pontos suficientes!!')

                 elif m == 3:
                     exit('FIM')
                 elif m == 4:
                     print(f'{inv}\n')
                 else:
                     print('Tente novamente')

         elif n1 == 'pedra' and pc == 'papel':
             print('\n\033[1;31mVOCÊ PERDEU!\033[m')
             print(f'Você escolheu \033[1;31m{n1}\033[m e o computador escolheu \033[1;32m{pc}\033[m ')
             c = c - 10
             print(f'Perdeu \033[1;31m10 pontos\033[m da sua carteira, tendo agora \033[1;36m{c} pontos\033[m')
             if c < 0:
                 print('Perdeu o jogo!\n')
                 exit('FIM')
             sleep(1)
             print('\n')
             while True:
                 print('MENU')
                 print('1. Continuar\n'
                       '2. Loja\n'
                       '3. Sair do jogo\n'
                       '4. Mostrar Inventário')
                 m = int(input('Qual das opções deseja?'))
                 if m == 1:
                     break
                 elif m == 2 and loja[0] == 'diamante':
                     sleep(0.3)
                     print('\n')
                     print('{:=^60}'.format('LOJA'))
                     print('Prata == 100 pontos\n'
                           'Ouro == 200 pontos\n'
                           'Diamante == 300 pontos')
                     print('{:=^60}'.format('LOJA'))
                     print('\n')
                     print('O que deseja fazer?')
                     print('1. Comprar\n'
                           '2. Sair da loja\n')
                     s = int(input())
                     if s == 1:
                         print('{:=^60}'.format('LOJA'))
                         print('1. Upgrade Final?\n')
                         print('{:=^60}'.format('LOJA'))
                         s1 = int(input())
                         if s1 == 1:
                             print('COMPRANDO . . .')
                             if c >= 300:
                                 sleep(0.3)
                                 c = c - 300
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou o Diamante e ficou com {c} pontos na carteira')
                                 sleep(0.3)
                                 if inv[2] == 'diamante':
                                     print('VOCÊ COMPLETOU O JOGO\nParabéns!!')
                                     exit('FIM')
                             else:
                                 print('Você não tem pontos suficientes!!')

                 elif m == 2:
                     sleep(0.3)
                     print('\n')
                     print('{:=^60}'.format('LOJA'))
                     print('Prata == 100 pontos\n'
                           'Ouro == 200 pontos\n'
                           'Diamante == 300 pontos')
                     print('{:=^60}'.format('LOJA'))
                     print('\n')
                     print('O que deseja fazer?')
                     print('1. Comprar\n'
                           '2. Sair da loja\n')
                     s = int(input())
                     if s == 1:
                         print('{:=^60}'.format('LOJA'))
                         print('1. Upgrade?\n')
                         print('{:=^60}'.format('LOJA'))
                         s1 = int(input())
                         if s1 == 1 and inv == []:
                             print('COMPRANDO . . .')
                             if c >= 100:
                                 sleep(0.3)
                                 c = c - 100
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou a Prata e ficou com {c} pontos na carteira')
                             else:
                                 print('Você não tem pontos suficientes!!')
                         elif s1 == 1 and inv[0] == 'prata':
                             print('COMPRANDO . . .')
                             if c >= 200:
                                 sleep(0.3)
                                 c = c - 200
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou o Ouro e ficou com {c} pontos na carteira')
                             else:
                                 print('Você não tem pontos suficientes!!')

                 elif m == 3:
                     exit('FIM')
                 elif m == 4:
                     print(f'{inv}\n')
                 else:
                     print('Tente novamente')

         elif n1 == 'papel' and pc == 'tesoura':
             print('\n\033[1;31mVOCÊ PERDEU!\033[m')
             print(f'Você escolheu \033[1;31m{n1}\033[m e o computador escolheu \033[1;32m{pc}\033[m ')
             c = c - 10
             print(f'Perdeu \033[1;31m10 pontos\033[m da sua carteira, tendo agora \033[1;36m{c} pontos\033[m')
             if c < 0:
                 print('Perdeu o jogo!')
                 exit('FIM')
             sleep(1)
             print('\n')
             while True:
                 print('MENU')
                 print('1. Continuar\n'
                       '2. Loja\n'
                       '3. Sair do jogo\n'
                       '4. Mostrar Inventário')
                 m = int(input('Qual das opções deseja?'))
                 if m == 1:
                     break
                 elif m == 2 and loja[0] == 'diamante':
                     sleep(0.3)
                     print('\n')
                     print('{:=^60}'.format('LOJA'))
                     print('Prata == 100 pontos\n'
                           'Ouro == 200 pontos\n'
                           'Diamante == 300 pontos')
                     print('{:=^60}'.format('LOJA'))
                     print('\n')
                     print('O que deseja fazer?')
                     print('1. Comprar\n'
                           '2. Sair da loja\n')
                     s = int(input())
                     if s == 1:
                         print('{:=^60}'.format('LOJA'))
                         print('1. Upgrade Final?\n')
                         print('{:=^60}'.format('LOJA'))
                         s1 = int(input())
                         if s1 == 1:
                             print('COMPRANDO . . .')
                             if c >= 300:
                                 sleep(0.3)
                                 c = c - 300
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou o Diamante e ficou com {c} pontos na carteira')
                                 sleep(0.3)
                                 if inv[2] == 'diamante':
                                     print('VOCÊ COMPLETOU O JOGO\nParabéns!!')
                                     exit('FIM')
                             else:
                                 print('Você não tem pontos suficientes!!')

                 elif m == 2:
                     sleep(0.3)
                     print('\n')
                     print('{:=^60}'.format('LOJA'))
                     print('Prata == 100 pontos\n'
                           'Ouro == 200 pontos\n'
                           'Diamante == 300 pontos')
                     print('{:=^60}'.format('LOJA'))
                     print('\n')
                     print('O que deseja fazer?')
                     print('1. Comprar\n'
                           '2. Sair da loja\n')
                     s = int(input())
                     if s == 1:
                         print('{:=^60}'.format('LOJA'))
                         print('1. Upgrade?\n')
                         print('{:=^60}'.format('LOJA'))
                         s1 = int(input())
                         if s1 == 1 and inv == []:
                             print('COMPRANDO . . .')
                             if c >= 100:
                                 sleep(0.3)
                                 c = c - 100
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou a Prata e ficou com {c} pontos na carteira')
                             else:
                                 print('Você não tem pontos suficientes!!')
                         elif s1 == 1 and inv[0] == 'prata':
                             print('COMPRANDO . . .')
                             if c >= 200:
                                 sleep(0.3)
                                 c = c - 200
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou o Ouro e ficou com {c} pontos na carteira')
                             else:
                                 print('Você não tem pontos suficientes!!')

                 elif m == 3:
                     exit('FIM')
                 elif m == 4:
                     print(f'{inv}\n')
                 else:
                     print('Tente novamente')

         elif n1 == 'tesoura' and pc == 'pedra':
             print('\n\033[1;31mVOCÊ PERDEU!\033[m')
             print(f'Você escolheu \033[1;31m{n1}\033[m e o computador escolheu \033[1;32m{pc}\033[m ')
             c = c - 10
             print(f'Perdeu \033[1;31m10 pontos\033[m da sua carteira, tendo agora \033[1;36m{c} pontos\033[m')
             if c < 0:
                 print('Perdeu o jogo!')
                 exit('FIM')
             sleep(1)
             print('\n')
             while True:
                 print('MENU')
                 print('1. Continuar\n'
                       '2. Loja\n'
                       '3. Sair do jogo\n'
                       '4. Mostrar Inventário')
                 m = int(input('Qual das opções deseja?'))
                 if m == 1:
                     break
                 elif m == 2 and loja[0] == 'diamante':
                     sleep(0.3)
                     print('\n')
                     print('{:=^60}'.format('LOJA'))
                     print('Prata == 100 pontos\n'
                           'Ouro == 200 pontos\n'
                           'Diamante == 300 pontos')
                     print('{:=^60}'.format('LOJA'))
                     print('\n')
                     print('O que deseja fazer?')
                     print('1. Comprar\n'
                           '2. Sair da loja\n')
                     s = int(input())
                     if s == 1:
                         print('{:=^60}'.format('LOJA'))
                         print('1. Upgrade Final?\n')
                         print('{:=^60}'.format('LOJA'))
                         s1 = int(input())
                         if s1 == 1:
                             print('COMPRANDO . . .')
                             if c >= 300:
                                 sleep(0.3)
                                 c = c - 300
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou o Diamante e ficou com {c} pontos na carteira')
                                 sleep(0.3)
                                 if inv[2] == 'diamante':
                                     print('VOCÊ COMPLETOU O JOGO\nParabéns!!')
                                     exit('FIM')
                             else:
                                 print('Você não tem pontos suficientes!!')

                 elif m == 2:
                     sleep(0.3)
                     print('\n')
                     print('{:=^60}'.format('LOJA'))
                     print('Prata == 100 pontos\n'
                           'Ouro == 200 pontos\n'
                           'Diamante == 300 pontos')
                     print('{:=^60}'.format('LOJA'))
                     print('\n')
                     print('O que deseja fazer?')
                     print('1. Comprar\n'
                           '2. Sair da loja\n')
                     s = int(input())
                     if s == 1:
                         print('{:=^60}'.format('LOJA'))
                         print('1. Upgrade?\n')
                         print('{:=^60}'.format('LOJA'))
                         s1 = int(input())
                         if s1 == 1 and inv == []:
                             print('COMPRANDO . . .')
                             if c >= 100:
                                 sleep(0.3)
                                 c = c - 100
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou a Prata e ficou com {c} pontos na carteira')
                             else:
                                 print('Você não tem pontos suficientes!!')
                         elif s1 == 1 and inv[0] == 'prata':
                             print('COMPRANDO . . .')
                             if c >= 200:
                                 sleep(0.3)
                                 c = c - 200
                                 inv.append(loja[0])
                                 del loja[0]
                                 print('COMPRA FEITA COM SUCESSO!')
                                 print(f'Você comprou o Ouro e ficou com {c} pontos na carteira')
                             else:
                                 print('Você não tem pontos suficientes!!')

                 elif m == 3:
                     exit('FIM')
                 elif m == 4:
                     print(f'{inv}\n')
                 else:
                     print('Tente novamente')
    elif j == 'N':
        print('{:=^60}'.format('FIM'))
        break
    else:
        print('Digitou errado! Tente novamente')
