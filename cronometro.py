from tkinter import *
import time

# configurações iniciais-----
window = Tk()
window.title('Myt Applin')

# BACKEND---------------------------------------------------------------------------------

# definindo globais-------------
global tempo
global rodar
global contador
tempo = "00:00:00"
rodar = False
contador = 0  # essa parte define o intervalo de tempo que vai ser contado

# funções----------------
def iniciar():
    global tempo
    global contador
    if rodar:
        # antes do cronometro começar
        if contador >= 0:  # Ajustei aqui para que o contador comece corretamente
            mins, secs = divmod(contador, 60)  # Calcula minutos e segundos
            horas = mins // 60
            tempo = f"{horas:02}:{mins%60:02}:{secs:02}"  # Formata o tempo
            label_tempo['text'] = tempo  # Atualiza o cronômetro no display
            label_tempo['font'] = 'Arial 55'

        else:
            label_tempo['text'] = f"Começando em {abs(contador)}"
            label_tempo['font'] = 'Arial 25'

        contador += 1  # Incrementa o contador para simular o cronômetro
        window.after(1000, iniciar)  # Chama novamente após 1 segundo (1000 ms)

# função para dar início-----
def start():
    global rodar
    rodar = True
    iniciar()

# função para pausar-------------
def pause():
    global rodar
    rodar = False
    iniciar()

# função para reiniciar----------
def reset():
    global contador
    contador = 0
    iniciar()
    pause()

# FRONTEND------------------------------------------------------------------------------

# ajustando background------
window.configure(background="#2d7059")

# definindo tamanho---------
window.geometry("550x301")
window.minsize(500, 300)
window.maxsize(600, 370)

# criando titulos-----------
label_titulo = Label(window, text="Cronometro", background="#2d7059", font=('arial', 25))
label_titulo.place(x=190, y=10, width=170, height=26)

label_tempo = Label(window, text=tempo, background="#2d7059", font=('arial', 55))
label_tempo.place(x=128, y=90, width=290, height=70)

# botão de start-----------
Button(window, text="Iniciar", command=start, background="#5f766e", font=('arial', 14)).place(x=124, y=198, width=85, height=40)

# botão de pause-----------
Button(window, text="Pausar", command=pause ,background="#5f766e", font=('arial', 14)).place(x=230, y=198, width=85, height=40)

# botão de restart----------
Button(window, text="Reiniciar", command=reset ,background="#5f766e", font=('arial', 14)).place(x=335, y=198, width=85, height=40)

# deixando no mainloop------
window.mainloop()            

#QA NOTE: Perfeito, apenas um problema: se clicar no botao de start n/ 
#Mais de 5x a aplicaçao quebra