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
5. Sobrescribe el método make_sound en la clase `Dog` para que imprima `"Woof!"` en lugar del sonido genérico.

6. Agrega a la clase `Dog` un método llamado fetch que imprima un mensaje como `"<name> is fetching the ball"`.

7. **Prueba tu solución.** Crea una instancia de la clase `Dog` llamada `my_dog` con:

```bash
name: "Buddy"
specie: "Canine"
```
8. Llama a los métodos `make_sound` y `fetch` en `my_dog`.

Deberías ver en pantalla:

```bash
¡Guau!  
Buddy está trayendo la pelota 
```
 