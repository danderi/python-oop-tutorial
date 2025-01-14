# ¡Construyendo un sistema de reproductor multimedia! 🎵

En este ejercicio, aprenderás cómo usar **clases abstractas** en Python para crear reglas compartidas entre clases relacionadas y cómo sobrescribir métodos abstractos en clases derivadas para implementar comportamientos específicos, a través de la creación de un sistema que pueda reproducir música y videos.

Antes de iniciar recordemos que las **clases abstractas** son plantillas para otras clases. Te ayudan a garantizar que todas las clases relacionadas sigan ciertas reglas.  

- Contienen **métodos abstractos**, que son como promesas y deben ser definidos en las clases que heredan de ellas.  
- No puedes crear objetos directamente a partir de una clase abstracta.

![abstract-class-image](../../.learn/assets/abstract-class-image-05.png)

## Instrucciones

1. Define una clase abstracta llamada `MediaPlayer`. Asegúrate de incluir métodos abstractos como: `play`, `pause` y 
`stop`.

2. Define una clase `AudioPlayer` que herede de `MediaPlayer` y defina los métodos requeridos `play`, `pause`, 
`stop`. Esta clase manejará solo archivos de audio.

3. Define una clase `VideoPlayer` que herede de `MediaPlayer` y defina los métodos requeridos `play`, `pause`, 
`stop`, pero con una función adicional llamada `show_video` para mostrar el video mientras se reproduce.


4. **Prueba tu solución.** Crea instancias de la clase `AudioPlayer` y `VideoPlaye` y verifica que funcionen correctamente.

```python
# Example Code
audio = AudioPlayer("song.mp3")
video = VideoPlayer("video.mp4")

audio.play()
audio.pause()
audio.stop()

video.play()
video.show_video()
video.stop()
```

## 💡 Consejos

- Usa `ABC` y `abstractmethod` del módulo `abc` de Python
- Los métodos abstractos son como promesas, es como decir "¡Definiré esto más tarde!"
- Cada reproductor debe tener todos los métodos requeridos `play`, `pause`, 
`stop`
- Piensa en lo que cada tipo de reproductor necesita hacer.
