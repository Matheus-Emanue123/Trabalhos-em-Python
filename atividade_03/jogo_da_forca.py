import tkinter as tk
from tkinter import messagebox
import random

palavras = [
    'python', 'programacao', 'computador', 'teclado', 'mouse', 'monitor', 'internet', 'desenvolvimento',
    'jogo', 'forca', 'codigo', 'algoritmo', 'software', 'hardware', 'dados', 'variavel', 'funcao',
    'sintaxe', 'debug', 'compilador', 'interpretador', 'sistema', 'rede', 'servidor', 'cliente',
    'script', 'biblioteca', 'modulo', 'pacote', 'objeto', 'classe', 'metodo', 'heranca', 'polimorfismo',
    'encapsulamento', 'abstracao', 'estrutura', 'array', 'lista', 'dicionario', 'conjunto', 'pilha',
    'fila', 'grafo', 'arvore', 'no', 'raiz', 'folha', 'recursao', 'iteracao', 'busca', 'ordenacao',
    'insercao', 'exclusao', 'atualizacao', 'string', 'inteiro', 'float', 'booleano', 'arquivo',
    'diretorio', 'sistema_operacional', 'windows', 'linux', 'mac', 'processo', 'thread', 'concorrencia',
    'paralelismo', 'assincrono', 'sincrono', 'api', 'rest', 'json', 'xml', 'html', 'css', 'javascript',
    'framework', 'django', 'flask', 'sqlite', 'postgresql', 'mysql', 'oracle', 'mongodb', 'redis',
    'memcached', 'docker', 'kubernetes', 'virtualizacao', 'cloud', 'aws', 'azure', 'gcp', 'serverless',
    'evento'
]

class JogoForca:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Forca")
        self.master.geometry("500x400")
        self.master.configure(bg="#f0f0f0")
       
        self.iniciar_jogo()

        frame_top = tk.Frame(self.master, bg="#f0f0f0")
        frame_top.pack(pady=10)

        frame_middle = tk.Frame(self.master, bg="#f0f0f0")
        frame_middle.pack(pady=10)

        frame_bottom = tk.Frame(self.master, bg="#f0f0f0")
        frame_bottom.pack(pady=10)

        self.label_titulo = tk.Label(frame_top, text="Bem-vindo ao Jogo da Forca!", 
                                     font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        self.label_titulo.pack()

        self.label_palavra = tk.Label(frame_middle, text="", font=("Helvetica", 20), bg="#f0f0f0")
        self.label_palavra.pack(pady=10)

        self.label_tentativas = tk.Label(frame_middle, text="", font=("Helvetica", 12), bg="#f0f0f0")
        self.label_tentativas.pack(pady=5)

        self.label_letras_erradas = tk.Label(frame_middle, text="", font=("Helvetica", 12), fg="red", bg="#f0f0f0")
        self.label_letras_erradas.pack(pady=5)

        self.entry_letra = tk.Entry(frame_bottom, font=("Helvetica", 14))
        self.entry_letra.pack(side=tk.LEFT, padx=5)

        self.btn_enviar = tk.Button(frame_bottom, text="Enviar", command=self.verificar_letra, 
                                    font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.btn_enviar.pack(side=tk.LEFT, padx=5)

        self.btn_reiniciar = tk.Button(frame_bottom, text="Reiniciar", command=self.reiniciar_jogo,
                                       font=("Helvetica", 12), bg="#2196F3", fg="white")
        self.btn_reiniciar.pack(side=tk.LEFT, padx=5)

        self.atualizar_interface()

    def iniciar_jogo(self):
        self.palavra_secreta = random.choice(palavras)
        self.letras_acertadas = ['_' for _ in self.palavra_secreta]
        self.tentativas = 8
        self.erros = 0
        self.letras_erradas = []

    def verificar_letra(self):
        letra = self.entry_letra.get().lower().strip()
        self.entry_letra.delete(0, tk.END)  

        if not letra.isalpha() or len(letra) != 1:
            messagebox.showwarning("Aviso", "Digite apenas uma letra.")
            return

        if letra in self.letras_acertadas or letra in self.letras_erradas:
            messagebox.showinfo("Info", "Você já tentou essa letra.")
            return

        if letra in self.palavra_secreta:
            for idx, letra_secreta in enumerate(self.palavra_secreta):
                if letra == letra_secreta:
                    self.letras_acertadas[idx] = letra
        else:
            self.erros += 1
            self.letras_erradas.append(letra)

        self.atualizar_interface()
        self.verificar_fim_de_jogo()

    def atualizar_interface(self):
        self.label_palavra.config(text=" ".join(self.letras_acertadas))
        self.label_tentativas.config(text=f"Tentativas restantes: {8 - self.erros}")
        if self.letras_erradas:
            self.label_letras_erradas.config(text="Letras erradas: " + ", ".join(self.letras_erradas))
        else:
            self.label_letras_erradas.config(text="")

    def verificar_fim_de_jogo(self):
        if '_' not in self.letras_acertadas:
            messagebox.showinfo("Parabéns!", f"Você acertou a palavra: {self.palavra_secreta}")
            self.desabilitar_jogo()
        elif self.erros >= 8:
            messagebox.showwarning("Fim de Jogo", f"Você perdeu! A palavra era: {self.palavra_secreta}")
            self.desabilitar_jogo()

    def desabilitar_jogo(self):
        self.btn_enviar.config(state=tk.DISABLED)
        self.entry_letra.config(state=tk.DISABLED)

    def reiniciar_jogo(self):
        self.iniciar_jogo()
        self.atualizar_interface()
        self.btn_enviar.config(state=tk.NORMAL)
        self.entry_letra.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoForca(root)
    root.mainloop()
