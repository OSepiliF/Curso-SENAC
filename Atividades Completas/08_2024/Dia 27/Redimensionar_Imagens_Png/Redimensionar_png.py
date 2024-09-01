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
    imagens_para_redimensionar = [
        #("Caminho da Imagem \\ Nome do arquivo .png"), ("Novo Caminho da Imagem \\ Novo Nome do Arquivo .png") 
        ("Coloque_Imagens_Aqui\\Bebidas_Agua.png", "Coloque_Imagens_Aqui\\Bebidas_Agua_red.png"),
        ("Coloque_Imagens_Aqui\\Bebidas_Coca.png", "Coloque_Imagens_Aqui\\Bebidas_Coca_red.png"),
        ("Coloque_Imagens_Aqui\\Bebidas_Fanta.png", "Coloque_Imagens_Aqui\\Bebidas_Fanta_red.png"),
        ("Coloque_Imagens_Aqui\\Bebidas_Guarana.png", "Coloque_Imagens_Aqui\\Bebidas_Guarana_red.png"),
        ("Coloque_Imagens_Aqui\\Bebidas_SucoLaranja.png", "Coloque_Imagens_Aqui\\Bebidas_SucoLaranja_red.png"),
        ("Coloque_Imagens_Aqui\\Bebidas_VitaminaFrutas.png", "Coloque_Imagens_Aqui\\Bebidas_VitaminaFrutas_red.png")
    ]

    redimensionar_imagens_em_lote(imagens_para_redimensionar)