import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Função para criar a interface da galeria
def create_gallery(root, images, descriptions):
    # Cria um frame para a galeria
    gallery_frame = tk.Frame(root)
    gallery_frame.pack(padx=0, pady=0, fill=tk.BOTH, expand=True)
    
    # Adiciona imagens e descrições ao frame
    for i, (img_path, desc) in enumerate(zip(images, descriptions)):
        # Carrega a imagem
        img = Image.open(img_path)
        img.thumbnail((150, 150))  # Redimensiona a imagem
        img_tk = ImageTk.PhotoImage(img)
        
        # Cria um frame para cada imagem
        img_frame = tk.Frame(gallery_frame)
        img_frame.grid(row=i // 3, column=i % 3, padx=10, pady=10, sticky="nsew")

        # Adiciona a imagem
        img_label = tk.Label(img_frame, image=img_tk)
        img_label.image = img_tk  # Mantém uma referência para a imagem
        img_label.pack()

        # Adiciona a descrição
        desc_label = tk.Label(img_frame, text=desc, wraplength=150, justify=tk.CENTER)
        desc_label.pack()

    # Ajusta o tamanho das colunas e linhas
    for i in range(3):
        gallery_frame.grid_columnconfigure(i, weight=1)
    rows = (len(images) + 2) // 3  # Número de linhas necessárias
    for i in range(rows):
        gallery_frame.grid_rowconfigure(i, weight=1)

# Cria a janela principal
root = tk.Tk()
root.title("Galeria de Imagens")


image_paths = [
    "C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\08_2024\\Dia 27\\Imagens_Galeria\\Paisagem1.png",
    "C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\08_2024\\Dia 27\\Imagens_Galeria\\Paisagem2.png",
    "C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\08_2024\\Dia 27\\Imagens_Galeria\\Paisagem3.png",
    "C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\08_2024\\Dia 27\\Imagens_Galeria\\Paisagem4.png"
]
descriptions = [
    "Descrição da Imagem 1",
    "Descrição da Imagem 2",
    "Descrição da Imagem 3",
    "Descrição da Imagem 4",
    "Descrição da Imagem 5",
    "Descrição da Imagem 6",
]

# Cria a galeria
create_gallery(root, image_paths, descriptions)

# Inicia o loop principal do Tkinter
root.mainloop()
