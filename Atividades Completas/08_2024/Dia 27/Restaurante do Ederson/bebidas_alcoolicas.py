from tkinter import *
from PIL import Image, ImageTk

def redimensionar_imagem(image_path, output_path, tamanho=(200, 300)):
    with Image.open(image_path) as img:
        img = img.resize(tamanho, Image.LANCZOS)
        img.save(output_path)

def carregar_imagem(image_path):
    img = Image.open(image_path)
    img = ImageTk.PhotoImage(img)
    return img

def abrir_bebidas_alcoolicas():
    bebidas_alcoolicas = Toplevel()
    bebidas_alcoolicas.state("zoomed")
    bebidas_alcoolicas.configure(bg='#F3F3F3')

    bebidas_alcoolicas.overrideredirect(True)
    barra_titulo = Frame(bebidas_alcoolicas, bg='black', bd=2)
    barra_titulo.pack(fill=X)
    titulo_label = Label(barra_titulo, text="Bebidas Alcoólicas", font=("Titan One", 12, "bold"), bg='black', fg='white')
    titulo_label.pack(side=LEFT, padx=10)
    close_button = Button(barra_titulo, text=" X ", bg='black', fg='red', command=bebidas_alcoolicas.destroy)
    close_button.pack(side=RIGHT, padx=10)

    imagens_redimensionadas = [
        ("Imagens_Restaurante/Alcoólicas_Caipirinha.png", "Imagens_Restaurante/Alcoólicas_Caipirinha_redimensionada.png"),
        ("Imagens_Restaurante/Alcoólicas_Chopp.png", "Imagens_Restaurante/Alcoólicas_Chopp_redimensionada.png"),
        ("Imagens_Restaurante/Alcoólicas_Espumante.png", "Imagens_Restaurante/Alcoólicas_Espumante_redimensionada.png"),
        ("Imagens_Restaurante/Alcoólicas_Heineken.png", "Imagens_Restaurante/Alcoólicas_Heineken_redimensionada.png"),
        ("Imagens_Restaurante/Alcoólicas_Skol.png", "Imagens_Restaurante/Alcoólicas_Skol_redimensionada.png"),
        ("Imagens_Restaurante/Alcoólicas_Vinho.png", "Imagens_Restaurante/Alcoólicas_Vinho_redimensionada.png")
    ]

    for img_path, output_path in imagens_redimensionadas:
        redimensionar_imagem(img_path, output_path)

    img_1 = carregar_imagem("Imagens_Restaurante\\Alcoólicas_Caipirinha_redimensionada.png")
    Label(bebidas_alcoolicas, image=img_1).place(relx=0.3, rely=0.3, anchor="center")

    img_2 = carregar_imagem("Imagens_Restaurante\\Alcoólicas_Chopp_redimensionada.png")
    Label(bebidas_alcoolicas, image=img_2).place(relx=0.3, rely=0.6, anchor="center")

    img_3 = carregar_imagem("Imagens_Restaurante\\Alcoólicas_Espumante_redimensionada.png")
    Label(bebidas_alcoolicas, image=img_3).place(relx=0.5, rely=0.3, anchor="center")

    img_4 = carregar_imagem("Imagens_Restaurante\\Alcoólicas_Heineken_redimensionada.png")
    Label(bebidas_alcoolicas, image=img_4).place(relx=0.5, rely=0.6, anchor="center")

    img_5 = carregar_imagem("Imagens_Restaurante\\Alcoólicas_Skol_redimensionada.png")
    Label(bebidas_alcoolicas, image=img_5).place(relx=0.7, rely=0.3, anchor="center")

    img_6 = carregar_imagem("Imagens_Restaurante\\Alcoólicas_Vinho_redimensionada.png")
    Label(bebidas_alcoolicas, image=img_6).place(relx=0.7, rely=0.6, anchor="center")

    bebidas_alcoolicas.mainloop()