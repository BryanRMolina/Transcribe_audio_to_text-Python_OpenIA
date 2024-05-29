import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import os

# Función que se ejecuta al presionar el botón "Descargar"
def ejecutar_descarga():
    url = entry_url.get()
    if url:
        try:
            # Ejecutar el script videodownload.py con la URL como argumento
            result = subprocess.run(['python', 'videodownload.py', url], check=True, capture_output=True, text=True)
            output = result.stdout.strip()
            transcript_path = output.split("\n")[-1]
            mostrar_transcripcion(transcript_path)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Ocurrió un error al descargar el video: {e}")
    else:
        messagebox.showwarning("Advertencia", "Por favor ingrese una URL.")

# Función para mostrar la transcripción en la interfaz gráfica
def mostrar_transcripcion(transcript_path):
    if os.path.exists(transcript_path):
        with open(transcript_path, 'r', encoding='utf-8') as file:
            transcripcion = file.read()
            text_transcripcion.delete(1.0, tk.END)
            text_transcripcion.insert(tk.END, transcripcion)
    else:
        messagebox.showerror("Error", "No se encontró el archivo de transcripción.")

# Crear la ventana principal
root = tk.Tk()
root.title("Descargar Video de YouTube")
root.geometry("600x400")
root.resizable(False, False)

# Crear un marco para centrar los widgets
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(expand=True)

# Crear el label y el Entry para la URL
label_url = tk.Label(frame, text="URL:")
label_url.grid(row=0, column=0, pady=10, sticky='e')

entry_url = tk.Entry(frame, width=50)
entry_url.grid(row=0, column=1, pady=10)

# Crear el botón "Descargar"
boton_descargar = tk.Button(frame, text="Descargar y transcribir", command=ejecutar_descarga, bg="#4CAF50", fg="white", padx=10, pady=5)
boton_descargar.grid(row=1, columnspan=2, pady=20)

# Crear el widget Text para mostrar la transcripción
text_transcripcion = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=70, height=15)
text_transcripcion.grid(row=2, columnspan=2, pady=10)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
