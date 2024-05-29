import sys
import os
from moviepy.editor import VideoFileClip
import speech_recognition as sr

def extraer_audio(video_path, audio_path):
    try:
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(audio_path)
        print(f"Audio extraído: {audio_path}")
    except Exception as e:
        print(f"Ocurrió un error al extraer el audio: {e}")

def transcribir_audio(audio_path, transcript_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
            texto = recognizer.recognize_google(audio, language='es-ES')
            print(f"Transcripción: {texto}")
            with open(transcript_path, 'w', encoding='utf-8') as f:
                f.write(texto)
            print(f"Transcripción guardada en: {transcript_path}")
    except Exception as e:
        print(f"Ocurrió un error al transcribir el audio: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        video_path = sys.argv[1]
        audio_path = os.path.splitext(video_path)[0] + '.wav'

        # Crear la carpeta 'scriptvoice' si no existe
        transcript_folder = 'scriptvoice'
        if not os.path.exists(transcript_folder):
            os.makedirs(transcript_folder)
        
        # Definir la ruta del archivo de transcripción
        transcript_path = os.path.join(transcript_folder, os.path.splitext(os.path.basename(video_path))[0] + '.txt')

        extraer_audio(video_path, audio_path)
        transcribir_audio(audio_path, transcript_path)
    else:
        print("Por favor, proporcione la ruta de un video.")
