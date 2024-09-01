from PIL import Image

def redimensionar_imagem(imagem_entrada, imagem_saida, tamanho=(380, 280)):
    try:
        img = Image.open(imagem_entrada)
        img = img.resize(tamanho, Image.LANCZOS)
        img.save(imagem_saida)
        print(f"Imagem {imagem_entrada} redimensionada e salva como {imagem_saida}.")
    except Exception as e:
        print(f"Erro ao redimensionar {imagem_entrada}: {e}")
    finally:
        img.close()

def redimensionar_imagens_em_lote(lista_imagens, tamanho=(380, 280)):
    for imagem_entrada, imagem_saida in lista_imagens:
        redimensionar_imagem(imagem_entrada, imagem_saida, tamanho)

if __name__ == "__main__":
    tamanho_desejado = (380, 280)  # Altere aqui o tamanho desejado

    imagens_para_redimensionar = [
        ("Coloque_Imagens_Aqui\\Brownie.png", "Coloque_Imagens_Aqui\\Brownie_red.png"),
        ("Coloque_Imagens_Aqui\\Cheesecake.png", "Coloque_Imagens_Aqui\\Cheesecake_red.png"),
        ("Coloque_Imagens_Aqui\\Mousse_de_Chocolate.png", "Coloque_Imagens_Aqui\\Mousse_Chocolate_red.png"),
        ("Coloque_Imagens_Aqui\\Pave.png", "Coloque_Imagens_Aqui\\Pave_red.png"),
        ("Coloque_Imagens_Aqui\\Pudim.png", "Coloque_Imagens_Aqui\\Pudim_red.png"),
        ("Coloque_Imagens_Aqui\\Tiramisu.png", "Coloque_Imagens_Aqui\\Tiramisu_red.png"),
    ]

    redimensionar_imagens_em_lote(imagens_para_redimensionar, tamanho=tamanho_desejado)
