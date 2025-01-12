# Creando Tu Primera Clase - Empecemos con Algo Fácil 🚀

¡Hola! Hoy vamos a aprender a crear una "clase" en Python. Si nunca has escuchado esto antes, ¡no te preocupes! Aquí tienes una explicación simple:

- Una clase es como un **molde** o una **plantilla**.
- Por ejemplo, si tuviéramos que describir "personas", podríamos crear un molde llamado `Persona`. Este molde podría decir que cada persona tiene un nombre y puede saludar a otras personas.

¡Vamos a crear nuestro propio molde llamado `Persona` para que Python pueda usarlo!

---

## 📝 Instrucciones

1. **Crea el molde.** Escribe esto en tu archivo `app.py`:

```python
class Person:
    pass
```

Ahora tienes una clase básica llamada `Person`. Aún no hace nada, pero ya existe.


2. **Agrega información básica (un nombre).** Queremos que cada persona tenga un nombre. Para eso usamos algo especial llamado `__init__`. Este es un método que configura nuestra persona cuando la creamos:

```python
class Persona:
    def __init__(self, name):
        self.name = name
```
 --

- `__init__` se ejecuta automáticamente cuando creamos una persona.
- `self.name` almacena el nombre para que podamos usarlo más tarde.

--

3. **Hacer que nuestra persona pueda saludar.** Ahora queremos que la clase haga algo. Agregaremos un método llamado `greet` que imprimirá un mensaje:

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def greet(self):
        print(f"Hello, my name is {self.name}")
```

--
- `greet` es una acción que nuestra clase puede realizar.
- Usa el nombre que guardamos con `self.name` para personalizar el saludo.

--



4. **Usa tu clase.** Escribe este código debajo de tu clase en `app.py` y ejecútalo:

   ```python
   person = Person("John")
   person.greet()
   ```

Deberías ver en la terminal:

   ```
   Hello, my name is John
   ```