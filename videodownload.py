import sys
import os
from pytube import YouTube
import subprocess

def descargar_video(url):
    try:
        # Crear la carpeta 'downloadervideos' si no existe
        download_folder = 'downloadervideos'
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video_path = video.download(output_path=download_folder)
        print(f"Video descargado: {yt.title}")

        # Llamar a transcribe.py para transcribir el audio del video descargado
        subprocess.run(['python', 'transcribe.py', video_path], check=True)
        
        # Retornar la ruta del archivo de transcripción
        transcript_folder = 'scriptvoice'
        transcript_path = os.path.join(transcript_folder, os.path.splitext(os.path.basename(video_path))[0] + '.txt')
        return transcript_path

    except Exception as e:
        print(f"Ocurrió un error al descargar el video: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        transcript_path = descargar_video(url)
        if transcript_path:
            print(transcript_path)
    else:
        print("Por favor, proporcione una URL.")
