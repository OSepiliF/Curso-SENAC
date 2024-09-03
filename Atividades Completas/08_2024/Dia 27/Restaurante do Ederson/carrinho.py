from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from bebidas_alcoolicas import carrinho_de_compras as car_bebidas_alcoolicas
from bebidas import carrinho_de_compras as car_bebidas
from menu_chef import carrinho_de_compras as car_menu_chef
from pratos_entrada import carrinho_de_compras as car_pratos_entrada
from pratos_principais import carrinho_de_compras as car_pratos_principais
from sobremesas import carrinho_de_compras as car_sobremesas

# Variável global para armazenar o valor total
valor_total = 0

def remover_item(item, todos_itens_carrinho, canvas):
    todos_itens_carrinho.remove(item)
    atualizar_carrinho(todos_itens_carrinho, canvas)

def atualizar_carrinho(todos_itens_carrinho, canvas):
    global valor_total
    canvas.delete("all")
    total = 0
    y_set = 20

    for item in todos_itens_carrinho:
        produto = item['produto']
        quantidade = item['quantidade']
        valor_unitario = item['valor_unitario']
        valor_item = item['valor_total']
        total += valor_item

        texto = f"{produto} - {quantidade} x R${valor_unitario:.2f} = R${valor_item:.2f}"
        canvas.create_text(10, y_set, anchor="nw", text=texto, font=("Titan One", 12), fill="black")
        
        # Botão de remover item
        remove_button = Button(canvas, text="Remover", command=lambda item=item:remover_item(item, todos_itens_carrinho, canvas))
        canvas.create_window(500, y_set, anchor="nw", window=remove_button)

        y_set += 30

    valor_total = total
    texto_total = f"Total: R${total:.2f}"
    canvas.create_text(10, y_set + 20, anchor="nw", text=texto_total, font=("Titan One", 14, "bold"), fill="black")

def pagamento_ficticio(todos_itens_carrinho, janela):
    todos_itens_carrinho.clear()  
    
    messagebox.showinfo("Pagamento", f"Pagamento realizado com sucesso! \nTotal: R${valor_total:.2f}")

    janela.destroy()

def abrir_carrinho():
    carrinho = Toplevel()
    carrinho.title("Carrinho")
    carrinho.state("zoomed")
    carrinho.configure(bg='#F3F3F3')

    #Plano de Fundo
    img_bg = (r"Imagens_Restaurante\\Madeira.jpg")
    bg_image = Image.open(img_bg)
    screen_width = carrinho.winfo_screenwidth()
    screen_height = carrinho.winfo_screenheight()
    bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_image_tk = ImageTk.PhotoImage(bg_image)
    bg_label = Label(carrinho, image=bg_image_tk)
    bg_label.place(relwidth=1, relheight=1)

    carrinho.overrideredirect(True)
    barra_titulo = Frame(carrinho, bg='black', bd=2)
    barra_titulo.pack(fill=X)
    titulo_label = Label(barra_titulo, text="Carrinho", font=("Titan One", 12, "bold"), bg='black', fg='white')
    titulo_label.pack(side=LEFT, padx=10)
    close_button = Button(barra_titulo, text=" X ", bg='black', fg='red', command=carrinho.destroy)
    close_button.pack(side=RIGHT, padx=10)

    canvas = Canvas(carrinho, bg='#F3F3F3', highlightthickness=0)
    canvas.pack(fill=BOTH, expand=True)

    todos_itens_carrinho = (car_bebidas_alcoolicas + car_bebidas + car_sobremesas + car_pratos_principais + car_pratos_entrada + car_menu_chef)

    atualizar_carrinho(todos_itens_carrinho, canvas)

    # Botão de pagamento
    pagamento_button = Button(carrinho, text="Pagar", font=("Titan One", 16, "bold"), bg='green', fg='white', command=lambda:pagamento_ficticio(todos_itens_carrinho, carrinho))
    pagamento_button.pack(pady=12)

    carrinho.mainloop()

if __name__ == "__main__":
    abrir_carrinho()
