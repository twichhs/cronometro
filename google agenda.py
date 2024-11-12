# Linkar o google agenda
import schedule
import time
def tarefa():
    print("Lição de casa")

#-ESTRUTURA---------------------------------------------------------------------------------------
'''schedule.every().day.do(tarefa)'''
# Dentro do parenteses do every temos o periodo de execução
# Se voce colocar um numero>1 a palavra de tempo a seguir deve ir para o plural

# .At() definira o horário do dia em que a def tarefa() será executada. Se passarmos para horas, devemos deixar apenas os minutos, deste jeito = ":19"
'''schedule.every().day.at("17:52").do(tarefa)'''

#-PROJETO-----------------------------------------------------------------------------------------
# Vamos fazer uma estrutura que rode apenas enquanto o usuário está "trabalhando"
schedule.every().second.until("Horario que iremos parar a aplicação") #obs: Talvez eu possa colunar uma hórarios limite de 23:59. Porém isso seria um péssima idea
# O ideal seria achar um jeito em que o schedule parasse quando o usuário quebrasse a aplicação


while True:
    schedule.run_pending()
    time.sleep(2)

