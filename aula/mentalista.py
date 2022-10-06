from time import sleep
import random

#mostrar o título
def titulo():
    print("\n=========================")
    print('\tO MENTALISTA')
    print('=========================')
    
#gerando um número aleatório    
def numero_aleatorio():
    numeroGerado = random.randrange(1, 101)
    return numeroGerado

#função principal
def mentalista(numero, tentativa):
    oppa = 0
    while oppa < 1:
        try:
            chute = int(input('\nChute o número que estou pensando entre 1 e 100. \nResposta: '))
            if chute < 1 or chute > 100:
                sleep(1)
                print('\nApenas um número entre 1 e 100. Tente novamente')
            elif chute > numero:
                sleep(1)
                print(f'\nO número que pensei é menor que {chute}, tente novamente')
                tentativa += 1
            elif chute < numero:
                 sleep(1)
                 print(f'\nO número que pensei é maior que {chute}, tente novamente')  
                 tentativa += 1
            elif chute == numero:
                 sleep(1)
                 print(f'\nPARABÉNS, você acertou com {tentativa} tentativas!\n')
                 opcao = input('Quer jogar mais uma vez? (s/n): ')
                 if opcao.lower() == 's' or opcao.lower() == 'sim':
                     print('\nReiniciando jogo...')
                     sleep(3)
                     numero = numero_aleatorio()
                     tentativa = 0
                     titulo()
                     continue
                 elif opcao.lower() == 'n' or opcao.lower() == 'nao':
                    sleep(1)
                    print('\nOk, obrigado por jogar!')
                    break
                                                 
        except ValueError:
            print('\nDigite um número inteiro!')
            sleep(1)                      
                           
titulo()
input('Digite ENTER para iniciar o game...')
numero = numero_aleatorio()
tentativa = 0                          
mentalista(numero, tentativa)                 