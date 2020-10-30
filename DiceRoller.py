import random
from os import system
from time import sleep

jogar_denovo = 1

def tela_inicial():
    #-----| TELA INICIAL |-----
    print('----------╭═══════════════════════════╮----------')
    print('----------|     Simple Dice Roller    |----------')
    print('----------|(d4, d6, d8, d10, d12, d20)|----------')
    print('----------╰═══════════════════════════╯----------')
    print()

    print('SELECIONE QUAL DADO QUER ROLAR')
    print(' [1] d4    (Dado de 4  faces)')
    print(' [2] d6    (Dado de 6  faces)')
    print(' [3] d8    (Dado de 8  faces)')
    print(' [4] d10   (Dado de 10 faces)')
    print(' [5] d12   (Dado de 12 faces)')
    print(' [6] d20   (Dado de 20 faces)')
    dice_t = int(input('\nQual dado deseja rolar? '))                   #Definir o tipo de dado que ira jogar
    print()                                                             #
    dice_x = 1 + int(input('Quantas vezes voce quer rolar o dado? '))   #Definir o intervalo de rolagens
    system('clear')                                                     #
    sistema_rolagem(dice_t, dice_x)

def dice(v_min, v_max):                     #Funcao que realiza a rolagem do dado
    dice = random.randrange(v_min, v_max)   #Define o valor em que o dado inicia 'v_min' e o valor maximo possivel 'v_max'
    return dice                             #Retorna o valor gerado randomicamente

def sistema_rolagem(dice_t, dice_x):        #Funcao que define qual dado sera rolado e quantas vezes
    qtd = 1                                 #Contador utilizado no while
    try:
        while qtd < dice_x:                 #Loop de execucao com limite no intervalo de rolagens decidido na tela inicial
            
            if dice_t == 1:                                             #Opcao d4
                print('-------| Jogada ', qtd, '|-------')              #Contador de Jogada
                print(f'O resultado da rolagem foi {dice(1,4)}! \n')    #Rolagem
                qtd = qtd + 1                                           #Avancar loop

            elif dice_t == 2:                                           #Opcao d6
                print('-------| Jogada ', qtd, '|-------')              #Contador de Jogada
                print(f'O resultado da rolagem foi {dice(1,6)}! \n')    #Rolagem
                qtd = qtd + 1                                           #Avancar loop

            elif dice_t == 3:                                           #Opcao d8
                print('-------| Jogada ', qtd, '|-------')              #Contador de Jogada
                print(f'O resultado da rolagem foi {dice(1,8)}! \n')    #Rolagem
                qtd = qtd + 1                                           #Avancar loop

            elif dice_t == 4:                                           #Opcao d10
                print('-------| Jogada ', qtd, '|-------')              #Contador de Jogada
                print(f'O resultado da rolagem foi {dice(1,10)}! \n')   #Rolagem
                qtd = qtd + 1                                           #Avancar loop

            elif dice_t == 5:                                           #Opcao d12
                print('-------| Jogada ', qtd, '|-------')              #Contador de Jogada
                print(f'O resultado da rolagem foi {dice(1,12)}! \n')   #Rolagem
                qtd = qtd + 1                                           #Avancar loop

            elif dice_t == 6:                                           #Opcao d20
                print('-------| Jogada ', qtd, '|-------')              #Contador de Jogada
                print(f'O resultado da rolagem foi {dice(1,20)}! \n')   #Rolagem
                qtd = qtd + 1                                           #Avancar loop

            else:                                                       #Saindo do loop por selecao invalida
                print('Selecao invalida...')                            #
                system('clear')                                         #Limpa a tela
    
    except:
        print('Erro na execucao das rolagens')

    finally:
        jogar_denovo = int(input('Jogar novamente ? \n [1] SIM \n [2] NAO \n > '))
        if jogar_denovo == 1:
            tela_inicial()

        elif jogar_denovo == 2:
            print('Encerando o DiceRoller...')
            print('\nObrigado por usa-lo')

        else:
            print('Erro na selecao de tela')
            sleep(2)
            print('Encerando o DiceRoller...')
            print('\nObrigado por usa-lo')

tela_inicial()
