from pytube import YouTube as y
from random import randint
from time import sleep
import os
from platform import uname
from colorama import Fore,Style
reset = Style.RESET_ALL 
nome = uname().node
nomeArquivo = input('Digite o nome do arquivo para eu criar ou colocar os videos: ')
def linha(msg='-=',quantasVezesRepete=20):
    print(msg*quantasVezesRepete)
def Baixar(quantidadeDeVideos:int,criarPasta:bool=True):
    num = randint(1,10)
    if criarPasta:
        diretorio_videos = f'./{nomeArquivo}'
        if not os.path.exists(diretorio_videos): # Verifica se existe um arquivo com o nome que o usuario informou
            diretorio_videos = f'./{nomeArquivo}{num}'
            os.mkdir(diretorio_videos) # Cria a pasta com o nome que o usuario informou
    for i in range(quantidadeDeVideos):
        url = input(f'Digite a URL do {i} vídeo: ')
        yt = y(url)
        linha()
        print(f'Baixando {i} video!...')
        video = yt.streams.get_highest_resolution()
        if criarPasta:
            video.download(output_path=diretorio_videos)
        else:
            video.download()
    return f'{Fore.GREEN}Download de todos os {quantidadeDeVideos} video(s), eles foram colocados na pasta {diretorio_videos}, muito obrigado por ussar esse codigo, {nome}.{reset}'

videos = Baixar(1)
print(videos)
