import os  # Módulo para manipulação de diretórios e arquivos
import yt_dlp  # Biblioteca para download de vídeos do YouTube

def baixar_video_yt_dlp(url, destino="videos"):
    """
    Função para baixar vídeos do YouTube usando a biblioteca yt_dlp.
    
    Parâmetros:
    - url (str): URL do vídeo a ser baixado.
    - destino (str): Diretório onde o vídeo será salvo. Padrão: "videos".
    """
    try:
        # Criar diretório de destino, se ele não existir
        if not os.path.exists(destino):
            os.makedirs(destino)  # Cria o diretório

        # Configurações para o yt_dlp
        ydl_opts = {
            'outtmpl': os.path.join(destino, '%(title)s.%(ext)s'),  # Caminho e nome do arquivo
            'format': 'bestvideo+bestaudio/best',  # Melhor qualidade disponível
            'noplaylist': True,  # Baixar apenas o vídeo, não uma playlist
            'http_headers': {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
        }
        
        # Inicializa o objeto do yt_dlp com as opções configuradas
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Baixa o vídeo a partir da URL

        print("Download concluído!")  # Mensagem de sucesso
    except Exception as e:
        # Exibe uma mensagem de erro em caso de falha
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso da função
url = "https://www.youtube.com/watch?v=BcF4YNNnysg&t=13s"  # URL do vídeo
baixar_video_yt_dlp(url)  # Chamada da função
