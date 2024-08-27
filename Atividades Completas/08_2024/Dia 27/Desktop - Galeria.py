import tkinter as tk
from tkinter import Scrollbar, Canvas, ttk
from PIL import Image, ImageTk

def Criar_Galeria(root, imagens, descricao):
    galeria_frame = tk.Frame(root)
    galeria_frame.pack(fill=tk.BOTH, expand=True)

    for i, (img_path, desc) in enumerate(zip(imagens, descricao)):
        img = Image.open(img_path)
        img.thumbnail((450, 250))
        img_tk = ImageTk.PhotoImage(img)

        img_frame = tk.Frame(galeria_frame)
        img_frame.grid(row=i // 3, column=i % 3, padx=10, pady=10, sticky="nsew")
