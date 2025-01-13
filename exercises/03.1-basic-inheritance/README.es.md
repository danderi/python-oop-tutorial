# ¡Creando una familia de mascotas! 🐾

Vamos a crear nuestra propia familia de programación con animales. En este ejercicio, aprenderás sobre herencia en programación creando una clase base y una clase hija. Esto te ayudará a entender cómo las clases pueden compartir y extender funcionalidades.


## 📝 Instrucciones


1. Define una clase base llamada `Animal`

2. En su método __init__, define los siguientes atributos: name, species.

3. Agrega un método llamado `make_sound` que imprima un sonido genérico como: `"Some generic sound"`.

4. Define una clase `Dog` que herede de Animal.

```python
class Dog(Animal):
    pass
```
5. En el método __init__ de `Dog`, utiliza `super().__init__()` para llamar al constructor de Animal. Asegúrate de que la clase **Dog** reciba también los parámetros name y species y los pase al constructor de la clase base.

```python
# Clase derivada Dog
class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)  # Inicializa los atributos de la clase base
```

6. Sobrescribe el método make_sound en la clase `Dog` para que imprima `"Woof!"` en lugar del sonido genérico.

7. Agrega a la clase `Dog` un método llamado fetch que imprima un mensaje como `"<name> is fetching the ball"`.

8. **Prueba tu solución.** Crea una instancia de la clase `Dog` llamada `my_dog` con:

```bash
name: "Buddy"
specie: "Canine"
```
9. Llama a los métodos `make_sound` y `fetch` en `my_dog`.

Deberías ver en pantalla:

```bash
¡Guau!  
Buddy está trayendo la pelota 
```
 