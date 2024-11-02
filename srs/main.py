import tkinter as tk
from App import App  # Importando a classe App do seu arquivo App.py

def main():
    root = tk.Tk()  # Criação da janela principal
    app = App(root)  # Inicializa a classe App com a janela principal
    root.mainloop()  # Inicia o loop do Tkinter

if __name__ == "__main__":
    main()  # Executa a função main
