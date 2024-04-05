import speech_recognition as sr


# Configura el reconocedor de voz
reconocedor = sr.Recognizer()

# Utiliza el micrófono como fuente de audio
with sr.Microphone() as fuente_audio:
    print("Di algo...")

    # Escucha el audio del micrófono
    audio = reconocedor.listen(fuente_audio)
    print("Escuchando completado...")

try:
    # Reconoce el texto del audio utilizando Google Speech Recognition
    texto = reconocedor.recognize_google(audio, language='es-ES')
    print("Has dicho:", texto)
except sr.UnknownValueError:
    print("No se pudo entender la voz.")
except sr.RequestError as e:
    print("Error al realizar la solicitud al servicio de reconocimiento de voz:", str(e))
except Exception as e:
    print("Error inesperado:", str(e))

