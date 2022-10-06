from time import sleep
resposta = input

#Função para mostrar o titulo
def titulo():
    print('\n=======================')
    print('\tBTS QUIZ')
    print('=======================')
    
#Primeira Pergunta    
def pergunta1():
   resposta1 =  input('\nQual o nome do membro mais velho (Hyung) do BTS?\nResposta: ')
   return resposta1
    
    
#Segunda Pergunta
def pergunta2():
  resposta2 = input('\nEm que ano o grupo debutou?\nResposta: ')    
  return resposta2
  
#Terceira Pergunta
def pergunta3():
  resposta3 = input('\nPor quantos membros a Vocal Line é formada? \nResposta: ')
  return resposta3
  
#Quarta Pergunta
def pergunta4():
      resposta4 = input('\nQuem é o maknae do grupo? \nResposta: ')
      return resposta4
      
#Quinta Pergunta
def pergunta5():
      resposta5 = input('\nQue membro utiliza o nome artístico "RM"?\nResposta: ')
      return resposta5

perguntaAtual = 1
while perguntaAtual <= 5:
    if perguntaAtual == 1:
        resposta = pergunta1()
        if resposta == "Jin":
            perguntaAtual += 1

    if perguntaAtual == 2:
        resposta = pergunta2()
        if resposta == "2013":
            perguntaAtual += 1

    if perguntaAtual == 3:
        resposta = pergunta3()
        if resposta in ["4", "quatro"]:
            perguntaAtual += 1

    if perguntaAtual == 4:
        resposta = pergunta4()
        if resposta == "JK":
            perguntaAtual += 1

    if perguntaAtual == 5:
        resposta = pergunta5()
        if resposta == "Namjoon":
            perguntaAtual += 1

print("Parabéns, você acertou todas!!!")


           