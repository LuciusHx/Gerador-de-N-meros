import random
from tkinter import * 

'''print(random.random()) //Valor 0.0 até 1.0
    print(random.uniform(0,10)) //Valor decimal no mínimo ao máximo
    print(random.randint()) //Valor inteiro min ao max

    cores = ['verde','vermelho', 'azul']
    print(random.choice(cores)) //Escolher uma opção dentro de uma fonte '''

def gerar():
    num = random.randint(1,60)
    numero["text"] = num


janela = Tk() #Gerar a Janela
janela.title("Gerador") #Inserir um título 

texto = Label(janela, text="Gerador de números aleatórios") #primeiro parâmetro: que janela? // segundo: o texto em si
texto.grid(column=0, row=0)
texto2 = Label(janela, text="Clique aqui") 
texto2.grid(column=0, row=2, padx=5, pady=5)

#BOTAO
button = Button(janela, text="GERAR", command = gerar)
button.grid(column=0, row=3, padx=10, pady=10)

#MENSAGEM RESULTADO
numero = Label(janela, text="")
numero.grid(column=0, row=4, padx=5, pady=10)

janela.mainloop() #Deixar a Janela Aberta

