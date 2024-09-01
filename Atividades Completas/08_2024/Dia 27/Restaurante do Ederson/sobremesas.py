from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox

carrinho_de_compras = []

class Valor_de_compra:
    def __init__(self):
        self.valores = {
            # Sobremesas
            "Brownie - R$8,00": 8, "Cheesecake - R$12,00": 12, "Tiramisu - R$15,00": 15, "Pudim - R$10,00": 10, "Mousse de Chocolate - R$9,00": 9, "Pavê - R$11,00": 11
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
    escolher_quant.configure(bg='#F3F3F3')

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

def abrir_sobremesas():
    sobremesas = Toplevel()
    sobremesas.state("zoomed")
    sobremesas.configure(bg='#F3F3F3')

    sobremesas.overrideredirect(True)
    barra_titulo = Frame(sobremesas, bg='black', bd=2)
    barra_titulo.pack(fill=X)
    titulo_label = Label(barra_titulo, text="Sobremesas", font=("Titan One", 12, "bold"), bg='black', fg='white')
    titulo_label.pack(side=LEFT, padx=10)
    close_button = Button(barra_titulo, text=" X ", bg='black', fg='red', command=sobremesas.destroy)
    close_button.pack(side=RIGHT, padx=10)

    valores = Valor_de_compra()

    imagens_redimensionadas = [
        ("Imagens_Restaurante\\Sobremesas_Brownie_red.png", "Brownie - R$8,00"),
        ("Imagens_Restaurante\\Sobremesas_Cheesecake_red.png", "Cheesecake - R$12,00"),
        ("Imagens_Restaurante\\Sobremesas_Tiramisu_red.png", "Tiramisu - R$15,00"),
        ("Imagens_Restaurante\\Sobremesas_Pudim_red.png", "Pudim - R$10,00"),
        ("Imagens_Restaurante\\Sobremesas_Mousse_Chocolate_red.png", "Mousse de Chocolate - R$9,00"),
        ("Imagens_Restaurante\\Sobremesas_Pave_red.png", "Pavê - R$11,00")
    ]

    canvas = Canvas(sobremesas, bg='#F3F3F3', highlightthickness=0)
    canvas.pack(fill=BOTH, expand=True)

    imagens_refs = []

    def criar_retorno(img_path, text, x, y, valor):
        img = carregar_imagem(img_path)
        imagens_refs.append(img)
        canvas.create_rectangle(x - 200, y - 150, x + 200, y + 250, fill="lightgray", outline="")
        canvas.create_image(x, y, anchor="center", image=img)
        canvas.create_text(x, y + 160, text=text, font=("Titan One", 13, "bold"), fill="black")
        bnt_adicionar_quant = ttk.Button(sobremesas, text="Adicionar ao Carrinho", style='custom.TButton', width=25, command=lambda:abrir_quantidade(text, valor))
        bnt_adicionar_quant.place(x=x, y=y + 240, anchor="center")

    largura_janela = sobremesas.winfo_screenwidth()
    altura_janela = sobremesas.winfo_screenheight()

    espacamento_x = largura_janela // 4
    espacamento_y = altura_janela // 2.5

    for i, (img_path, text) in enumerate(imagens_redimensionadas):
        valor = valores.obter_valor(text)
        coluna = i % 3
        linha = i // 3
        x = espacamento_x * (coluna + 1)
        y = espacamento_y * (linha + 1) - 170
        criar_retorno(img_path, text, x, y, valor)

    frame_bnt_sair = Frame(sobremesas, bg='#F3F3F3', bd=2)
    frame_bnt_sair.pack(side=BOTTOM, fill=X, padx=10, pady=10)
    bnt_sair = ttk.Button(frame_bnt_sair, text="Voltar ao Menu", style='custom.TButton', command=sobremesas.destroy)
    bnt_sair.pack(pady=5) 
    sobremesas.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.withdraw() 
    abrir_sobremesas()
    root.mainloop()