# ¡Construyendo un Sistema de Biblioteca Inteligente! 📚

Vamos a crear un sistema de biblioteca donde los libros puedan ser compartidos entre diferentes partes de nuestro programa, ¡pero de una manera segura y organizada!. El objetivo de este ejercicio es aprender sobre atributos protegidos en Python mientras construimos un sistema básico de gestión de biblioteca.


Este ejercicio es perfecto para aprender sobre atributos protegidos porque:
- Alguna información necesita ser compartida (como los títulos de los libros)
- Queremos ser cuidadosos sobre cómo se usa
- ¡Es como tener áreas de "solo personal" en una biblioteca!

## 📝 Instrucciones

1. Crea una clase llamada `LibraryItem`.  

2. En el constructor (`__init__`), agrega atributos protegidos:  
   - `_title`: título del ítem (cadena de texto).  
   - `_author`: autor del ítem (cadena de texto).  
   - `_is_available`: estado de disponibilidad (booleano, inicia como `True`).  

3. Crea un método protegido llamado `_update_availability` que actualice el estado de disponibilidad del ítem. 


```python
   def _update_availability(self, is_available):
       self._is_available = is_available
```

4. Define un método público lend_item que verifique si el ítem está disponible. Si está disponible, actualice el estado a "no disponible" utilizando `_update_availability`. Si no está disponible, imprima un mensaje indicando que ya está prestado.

5. Define otro método público `return_item` que marque el ítem como disponible.

6. Crea una clase `Book` que herede de `LibraryItem` y añade un atributo protegido `_isbn` en el constructor para almacenar el número ISBN del libro.

```python
   def __init__(self, title, author, isbn):
        super().__init__(title, author)
        self._isbn = isbn
```

7. Implementa un método público llamado `display_info` que muestre toda la información del libro (título, autor, disponibilidad e ISBN) de manera ordenada. Ejemplo: `Book: {title} by {author} (ISBN: {isbn}) - Available: {available}`

8. **Prueba tu solución.** Crea una instancia de la clase `Book` llamada `book` con información como título, autor e ISBN. Llama a los métodos lend_item y return_item para verificar que funcionan correctamente. Usa el método display_info para mostrar la información del libro en cada paso.


## 💡 ¿Necesitas Ayuda?

- Usa `_` (guion bajo) para cosas protegidas
- Protegido significa "por favor, ten cuidado con esto"
- Las clases hijas pueden usar cosas protegidas de su padre
- Usa nombres claros para mostrar lo que debe ser protegido