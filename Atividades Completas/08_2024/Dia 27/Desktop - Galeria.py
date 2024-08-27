import tkinter as tk
from tkinter import Scrollbar, Canvas, ttk
from PIL import Image, ImageTk

class ImageGalleryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Galeria de Imagens")
        root.geometry("850x650")

        self.canvas = Canvas(root)
        self.scrollbar = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.images = [
            "C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\08_2024\\Dia 27\\Imagens\\Paisagem1.png",
            "C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\08_2024\\Dia 27\\Imagens\\Paisagem2.png",
            "C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\08_2024\\Dia 27\\Imagens\\Paisagem3.png",
            "C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\08_2024\\Dia 27\\Imagens\\Paisagem4.png"
        ]

        self.create_gallery()

    def create_gallery(self):
        for idx, image_path in enumerate(self.images):
            frame = tk.Frame(self.scrollable_frame)
            frame.pack(pady=25, padx=35, fill="x")
    
            img = Image.open(image_path)
            img = img.resize((725, 450), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)


            label_image = tk.Label(frame, image=img_tk)
            label_image.image = img_tk  
            label_image.pack()

            description_label = tk.Label(frame, text="Descrição:")
            description_label.pack(anchor="w")

            description_entry = tk.Entry(frame, width=120)
            description_entry.pack(pady=5)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGalleryApp(root)
    root.mainloop()
