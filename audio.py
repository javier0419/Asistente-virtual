import pygame

def reproducir_audio(ruta_archivo):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(ruta_archivo)
        pygame.mixer.music.play()

        # Esperar a que termine la reproducción
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        # Mantener la aplicación en ejecución después de la reproducción
        while True:
            pygame.event.poll()
            pygame.time.delay(100)

    except Exception as e:
        print(f"Error al reproducir audio: {e}")
