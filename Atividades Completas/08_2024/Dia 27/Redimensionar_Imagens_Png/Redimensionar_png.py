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
        ("Coloque_Imagens_Aqui\\Canelone_Berinjela.png", "Coloque_Imagens_Aqui\\Menu_Chef_Canelone_Berinjela_red.png"),
        ("Coloque_Imagens_Aqui\\Espaguete_Carbonara.png", "Coloque_Imagens_Aqui\\Menu_Chef_Espaguete_Carbonara_red.png"),
        ("Coloque_Imagens_Aqui\\File_Mignon.png", "Coloque_Imagens_Aqui\\Menu_Chef_File_Mignon_red.png"),
        ("Coloque_Imagens_Aqui\\Pizza_Gourmet.png", "Coloque_Imagens_Aqui\\Menu_Chef_Pizza_Gourmet_red.png"),
        ("Coloque_Imagens_Aqui\\Risoto_Cogumelos.png", "Coloque_Imagens_Aqui\\Menu_Chef_Risoto_Cogumelos_red.png"),
        ("Coloque_Imagens_Aqui\\Salmao_Grelhado.png", "Coloque_Imagens_Aqui\\Menu_Chef_Salmao_Grelhado_red.png"),
    ]

    redimensionar_imagens_em_lote(imagens_para_redimensionar, tamanho=tamanho_desejado)