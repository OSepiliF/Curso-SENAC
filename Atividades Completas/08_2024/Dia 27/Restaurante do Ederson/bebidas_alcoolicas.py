from tkinter import *
from PIL import Image, ImageTk  # Importar do Pillow

def abrir_bebidas_alcoolicas():
    bebidas_alcoolicas = Toplevel()
    bebidas_alcoolicas.title("Bebidas Alcólicas")
    bebidas_alcoolicas.state("zoomed")
    bebidas_alcoolicas.configure(bg='#F3F3F3')

    # Configuração da Barra de Título
    title_bar = Frame(bebidas_alcoolicas, bg='black', bd=2)
    title_bar.pack(fill=X)
    title_label = Label(title_bar, text="Restaurante do Ederson", bg='black', fg='white', font=("Titan One", 12, "bold"))
    title_label.pack(side=LEFT, padx=10)
    close_button = Button(title_bar, text=" X ", bg='black', fg='red', command=bebidas_alcoolicas.destroy)
    close_button.pack(side=RIGHT, padx=10)

    def resize_image(image_path, width, height):
        with Image.open(image_path) as img:
            img = img.resize((width, height), Image.ANTIALIAS)
            return ImageTk.PhotoImage(img)

    img_1 = resize_image("Imagens_Restaurante/Alcoólicas_Caipirinha.png", 200, 300)
    Label(bebidas_alcoolicas, image=img_1).place(relx=0.3, rely=0.3, anchor="center")

    img_2 = resize_image("Imagens_Restaurante/Alcoólicas_Chopp.png", 200, 300)
    Label(bebidas_alcoolicas, image=img_2).place(relx=0.3, rely=0.6, anchor="center")

    img_3 = resize_image("Imagens_Restaurante/Alcoólicas_Espumante.png", 200, 300)
    Label(bebidas_alcoolicas, image=img_3).place(relx=0.5, rely=0.3, anchor="center")

    img_4 = resize_image("Imagens_Restaurante/Alcoólicas_Heineken.png", 200, 300)
    Label(bebidas_alcoolicas, image=img_4).place(relx=0.5, rely=0.6, anchor="center")

    img_5 = resize_image("Imagens_Restaurante/Alcoólicas_Skol.png", 200, 300)
    Label(bebidas_alcoolicas, image=img_5).place(relx=0.7, rely=0.3, anchor="center")

    img_6 = resize_image("Imagens_Restaurante/Alcoólicas_Vinho.png", 200, 300)
    Label(bebidas_alcoolicas, image=img_6).place(relx=0.7, rely=0.6, anchor="center")

    bebidas_alcoolicas.img_refs = [img_1, img_2, img_3, img_4, img_5, img_6]

    bebidas_alcoolicas.mainloop()

# Execute a função para testar
abrir_bebidas_alcoolicas()
