from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox

carrinho_de_compras = []

class Valor_de_compra:
    def __init__(self):
        self.valores = {
            # Bebidas Alcoólicas
            "Caipirinha - R$6,00": 6, "Chopp - R$10,00": 10, "Espumante - R$30,00": 30, "Heineken - R$8,00": 8, "Skol - R$5,00": 5, "Vinho - R$60,00": 60,
        }

    def obter_valor(self, nome_produto):
        return self.valores.get(nome_produto, None)

def carregar_imagem(imagem_entrada):
    img = Image.open(imagem_entrada)
    img = ImageTk.PhotoImage(img)
    return img

def abrir_quantidade(nome_produto, valor_produto):
    escolher_quant = Toplevel()
    escolher_quant.title(f"Adicionar {nome_produto}")
    escolher_quant.geometry("300x150")

    def adicionar_quantidade():
        quantidade = quantidade_entry.get()
        if quantidade != "" and int(quantidade) > 0:
            total_valor = int(quantidade) * valor_produto
            carrinho_de_compras.append({
                'produto': nome_produto,
                'quantidade': int(quantidade),
                'valor_unitario': valor_produto,
                'valor_total': total_valor
            })
            messagebox.showinfo("Carrinho", f"Você adicionou {quantidade} {nome_produto}(s) ao carrinho.\nValor total: R${total_valor:.2f}")
            escolher_quant.destroy()
        else:
            messagebox.showerror("Erro!", "Por favor, insira uma quantidade válida.")

    Label(escolher_quant, text=f"Quant. de {nome_produto}", font=("Titan One", 12, "bold"), bg='#F3F3F3').pack(pady=10.5)
    quantidade_entry = Entry(escolher_quant, font=("Titan One", 10))
    quantidade_entry.pack(pady=6)
    Button(escolher_quant, text="Adicionar ao Carrinho", font=("Titan One", 10, "bold"), command=adicionar_quantidade).pack(pady=10.5)

def abrir_bebidas_alcoolicas():
    bebidas_alcoolicas = Toplevel()
    bebidas_alcoolicas.state("zoomed")
    bebidas_alcoolicas.overrideredirect(True)

    barra_titulo = Frame(bebidas_alcoolicas, bg='black', bd=2)
    barra_titulo.pack(fill=X)
    titulo_label = Label(barra_titulo, text="Bebidas Alcoólicas", font=("Titan One", 12, "bold"), bg='black', fg='white')
    titulo_label.pack(side=LEFT, padx=10)
    close_button = Button(barra_titulo, text=" X ", bg='black', fg='red', command=bebidas_alcoolicas.destroy)
    close_button.pack(side=RIGHT, padx=10)

    valores = Valor_de_compra()

    imagens_redimensionadas = [
        ("Imagens_Restaurante\\Alcoólicas_Caipirinha_red.png", "Caipirinha - R$6,00"),
        ("Imagens_Restaurante\\Alcoólicas_Chopp_red.png", "Chopp - R$10,00"),
        ("Imagens_Restaurante\\Alcoólicas_Espumante_red.png", "Espumante - R$30,00"),
        ("Imagens_Restaurante\\Alcoólicas_Heineken_red.png", "Heineken - R$8,00"),
        ("Imagens_Restaurante\\Alcoólicas_Skol_red.png", "Skol - R$5,00"),
        ("Imagens_Restaurante\\Alcoólicas_Vinho_red.png", "Vinho - R$60,00")
    ]

    canvas = Canvas(bebidas_alcoolicas, highlightthickness=0)
    canvas.pack(fill=BOTH, expand=True)

    imagens_refs = []

    def criar_retorno(img_path, text, x, y, valor):
        img = carregar_imagem(img_path)
        imagens_refs.append(img)
        canvas.create_rectangle(x - 200, y - 150, x + 200, y + 250, fill="lightgray", outline="")
        canvas.create_image(x, y, anchor="center", image=img)
        canvas.create_text(x, y + 160, text=text, font=("Titan One", 13, "bold"), fill="black")
        bnt_adicionar_quant = ttk.Button(bebidas_alcoolicas, text="Adicionar ao Carrinho", style='custom.TButton', width=25, command=lambda: abrir_quantidade(text, valor))
        bnt_adicionar_quant.place(x=x, y=y + 240, anchor="center")

    largura_janela = bebidas_alcoolicas.winfo_screenwidth()
    altura_janela = bebidas_alcoolicas.winfo_screenheight()

    espacamento_x = largura_janela // 4
    espacamento_y = altura_janela // 2.5

    for i, (img_path, text) in enumerate(imagens_redimensionadas):
        valor = valores.obter_valor(text)
        coluna = i % 3
        linha = i // 3
        x = espacamento_x * (coluna + 1)
        y = espacamento_y * (linha + 1) - 170
        criar_retorno(img_path, text, x, y, valor)

    frame_bnt_sair = Frame(bebidas_alcoolicas)
    frame_bnt_sair.pack(side=BOTTOM, padx=10, pady=10)
    bnt_sair = ttk.Button(frame_bnt_sair, text="Voltar ao Menu", style='custom.TButton', command=bebidas_alcoolicas.destroy)
    bnt_sair.pack(pady=5) 

    bebidas_alcoolicas.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.withdraw() 
    abrir_bebidas_alcoolicas()
    root.mainloop()