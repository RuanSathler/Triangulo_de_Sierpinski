import tkinter as tk
import math

def desenhaTriangulo(x1, y1, x2, y2, x3, y3, cor):
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=cor, outline="black")

def triangulo_serp(x, y, z, nivel, cor):
    if nivel == 0:
        desenhaTriangulo(x[0], x[1], y[0], y[1], z[0], z[1], cor)
        return

    base = z[0] - x[0]
    altura = (base * math.sqrt(3)) / 2

    # vértices do triângulo superior
    g = [x[0] + base / 4, x[1] - altura / 2] #vertice inferior esquerdo
    h = [x[0] + 3 * base / 4, x[1] - altura / 2] #vertice inferior direito

    #ponto que delimita os dois triangulos inferiores
    r = [x[0] + base / 2, x[1]]

    # recursão: triângulo de cima
    triangulo_serp(g, y, h, nivel - 1, "#1CC9C0")

    # triângulo inferior esquerdo
    triangulo_serp(x, g, r, nivel - 1, "#FF3232")

    # triângulo inferior direito
    triangulo_serp(r, h, z, nivel - 1, "#00FF88")

# Triângulo inicial
x = [50, 1000]
z = [1150, 1000]
altura = (1100 * math.sqrt(3)) / 2
y = [600, 1000 - altura]

''''
tela = tk.Tk()
tela.geometry("1200x1000")
canvas = tk.Canvas(tela, width=1200, height=1000, bg="white")
canvas.pack()
nivel = 0

while 1:
    
    triangulo_serp(x, y, z, nivel, "#00FFFF")
    nivel += 1

      # Exibe a janela sem bloquear
    input("Pressione Enter para fechar a janela e continuar...")
    canvas.delete("all")  # Fecha a janela antes da próxima iteração

'''''

# Inicialização da tela e canvas
tela = tk.Tk()
tela.geometry("1200x1000")
canvas = tk.Canvas(tela, width=1200, height=1000, bg="white")
canvas.pack()

nivel = 0

mensagens = {
    6: "\033[34mInsistência não é sempre uma virtude...\033[0m",
    7: "\033[34mVocê ainda tá aqui? Vai tomar uma água!\033[0m",
    8: "\033[34mSério, por que você está fazendo isso consigo mesmo?\033[0m",
    9: "\033[34mChega! O programa já sofreu demais...\033[0m",
}

while 1:

    if nivel > 5:
        if nivel > 9: 
            print("Encerrando... você foi avisado 😤")
            tela.destroy()
            break
        mensagem = mensagens.get(nivel)
        print(mensagem)
        
        

    triangulo_serp(x, y, z, nivel, "#00FFFF")
    nivel += 1

    entrada = input("Pressione Enter para fechar a janela e continuar, ou digite qualque outra coisa para encerrar o programa...")
    if entrada != "":
        break

    # Limpa o canvas para a próxima iteração
    canvas.delete("all")

    
