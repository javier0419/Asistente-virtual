import speech_recognition as sr
import tkinter as tk
from openai_chat import chat_with_gpt
from openai import OpenAI
from pathlib import Path
import os
from audio import reproducir_audio

client = OpenAI(api_key= "YOUR_APY_KEY")   

# Establece tu API key

ruta_archivo_mp3 = "D:/upds/inteligencia_artificial/psicologo/respuesta_audio.mp3"


def convertir_texto_a_voz(texto, modelo="tts-1", voz="nova", formato="mp3"):
    try:
        # Generar audio hablado a partir del texto
        response = client.audio.speech.create(
            model=modelo,
            voice=voz,
            input=texto
        )

        # Guardar el audio en un archivo temporal
        ruta_archivo_temporal = "respuesta_audio.mp3"
        response.stream_to_file(ruta_archivo_temporal)
        reproducir_audio(ruta_archivo_temporal)
        return ruta_archivo_temporal

    except Exception as e:
        print(f"Error al generar voz: {e}")
        return None


def convertir_voz_a_texto():
    # Initialize a SpeechRecognition Recognizer object
    reconocedor = sr.Recognizer()

    # Record audio from the microphone
    with sr.Microphone() as source:
        print("Di algo...")
        audio = reconocedor.listen(source)

    try:
        # Recognize the recorded audio using Google Speech Recognition
        texto_transcrito = reconocedor.recognize_google(audio, language="es-ES")

        # Return the transcribed text
        return texto_transcrito

    except sr.RequestError as e:
        print(f"Error al realizar la solicitud al servicio de reconocimiento de voz: {e}")
        return None


def iniciar_reconocimiento_voz():
    # Retrieve the recognized text
    texto_reconocido = convertir_voz_a_texto()

    # If text is available, update the GUI accordingly
    if texto_reconocido:
        entrada_pregunta.delete(0, tk.END)
        entrada_pregunta.insert(tk.END, texto_reconocido)


def enviar_pregunta():
    # Retrieve the question text from the input entry widget
    pregunta = entrada_pregunta.get()

    try:
        # Send the question to the GPT-3 API using your API key
        

     # Formatear y mostrar la respuesta en el widget de texto de salida
        texto_respuesta.insert(tk.END, f"Tú: {pregunta}\n")
        texto_respuesta.insert(tk.END, f"GPT-3: {respuesta}\n")
        entrada_pregunta.delete(0, tk.END)

        # Convertir la respuesta a audio y reproducirla
        ruta_audio = convertir_texto_a_voz(respuesta)
        if ruta_audio:
            os.system(f"start {ruta_audio}")

    except Exception as e:
        print(f"Error al enviar la pregunta: {e}")
        return
    
# Crear ventana principal
ventana = tk.Tk()
ventana.title("Asistente Virtual")
ventana.geometry("1200x700")  # Tamaño medio de la ventana

# Colores para la interfaz
color_fondo = "#F0EAD6"  # Crema
color_texto = "#333333"  # Gris oscuro
color_boton = "#FFA07A"  # Melocotón

# Configuración de la fuente
fuente = ("Arial", 14)

# Configurar colores de fondo y texto para la ventana
ventana.configure(bg=color_fondo)

# Crear nombre del asistente en la parte superior
nombre_asistente = tk.Label(ventana, text="Asistente Personal", bg=color_fondo, fg=color_texto, font=("Arial", 20, "bold"))  # Fuente más grande y en negrita
nombre_asistente.grid(row=0, column=0, columnspan=3, pady=10)  # Centrar y aplicar padding

# Crear widgets de entrada y salida de texto con colores y fuente personalizados
etiqueta_pregunta = tk.Label(ventana, text="Pregunta:", bg=color_fondo, fg=color_texto, font=fuente)
entrada_pregunta = tk.Entry(ventana, width=80, font=fuente)  # Ajustar ancho del Entry
etiqueta_respuesta = tk.Label(ventana, text="Respuesta:", bg=color_fondo, fg=color_texto, font=fuente)
texto_respuesta = tk.Text(ventana, width=80, height=20, font=fuente)  # Ajustar tamaño del Text

# Ubicar widgets en la ventana y aplicar padding
etiqueta_pregunta.grid(row=1, column=0, padx=10, pady=10)  # Aumentar padding
entrada_pregunta.grid(row=1, column=1, padx=10, pady=10, columnspan=2)  # Aumentar padding
etiqueta_respuesta.grid(row=2, column=0, padx=10, pady=10)  # Aumentar padding
texto_respuesta.grid(row=2, column=1, padx=10, pady=10, columnspan=2)  # Aumentar padding

# Crear botones con colores personalizados y tamaño grande
boton_microfono = tk.Button(ventana, text="Microfono", command=iniciar_reconocimiento_voz, bg=color_boton, fg=color_texto, font=fuente)  # Aumentar ancho del botón
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_pregunta, bg=color_boton, fg=color_texto, font=fuente)  # Aumentar ancho del botón

# Ubicar botones en la ventana y centrarlos
boton_microfono.grid(row=3, column=1, padx=10, pady=10)  # Centrar y aplicar padding
boton_enviar.grid(row=3, column=2, padx=10, pady=10)  # Centrar y aplicar padding

# Ejecutar la aplicación
ventana.mainloop()
