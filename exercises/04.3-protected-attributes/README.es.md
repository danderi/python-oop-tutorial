# ¡Construyendo un Sistema de Biblioteca Inteligente! 📚

Vamos a crear un sistema de biblioteca donde los libros puedan ser compartidos entre diferentes partes de nuestro programa, ¡pero de una manera segura y organizada!. El objetivo de este ejercicio es aprender sobre atributos protegidos en Python mientras construimos un sistema básico de gestión de biblioteca.


Este ejercicio es perfecto para aprender sobre atributos protegidos porque:
- Alguna información necesita ser compartida (como los títulos de los libros)
- Queremos ser cuidadosos sobre cómo se usa
- ¡Es como tener áreas de "solo personal" en una biblioteca!

## 📝 Instrucciones

1. Crea una clase llamada `LibraryItem`. Esto será como el "modelo" para todos los objetos de nuestra biblioteca (libros, revistas, etc.)

2. Agrega algunos atributos dentro del constructor. En el método (`__init__`) de la clase `LibraryItem`, agrega atributos protegidos:  
   - `_title`: título del ítem, que será texto.  
   - `_author`: autor del ítem, tambien texto.  
   - `_is_available`: indicará si el ítem está disponible. Siempre empezará como True (o sea, disponible). 

   ```python
      class LibraryItem:
         def __init__(self, title, author):
            self._title = title
            self._author = author
            self._is_available = True

   ``` 

3. Crea un método protegido llamado `_update_availability` que actualice el estado de disponibilidad del ítem. Este método cambiará el estado de disponibilidad de los ítems. Piensa en él como el encargado de marcar algo como "prestado" o "disponible"


```python
   def _update_availability(self, is_available):
       self._is_available = is_available
```

4. Define un método público `check_out`. Este método se encargará de prestar el ítem:

- Si el ítem está disponible, cámbialo a "no disponible" usando _update_availability `_update_availability`. 
- Si ya está prestado, imprime un mensaje como: 

```python
"{title} not available"
```
5. Define otro método público `return_item`. Este marcará el ítem como disponible nuevamente (como si alguien devolviera el libro).

6. Crea una clase `Book` que herede de `LibraryItem` y añade un atributo protegido `_isbn` en el constructor para almacenar el número ISBN del libro.

```python
   def __init__(self, title, author, isbn):
        super().__init__(title, author)
        self._isbn = isbn
```

7. Implementa un método público llamado `display_info` que muestre toda la información del libro (título, autor, disponibilidad e ISBN) de manera ordenada. Ejemplo: 
```python
"Book: {title} by {author} (ISBN: {isbn}) - Available: {available}"
```

8. **Prueba tu solución.** Crea una instancia de la clase `Book` llamada `book` con datos ficticios:

```python
book = Book("Harry Potter", "J.K. Rowling", "123456789") 
```

- Usa `display_info` para mostrar la información del libro.
- Usa `check_out` para prestar el libro y vuelve a mostrar la información con `display_info`.
- Usa `return_item` para devolver el libro y verifica que todo funciona correctamente.


## 💡 Consejos

- Usa `_ ` (guion bajo) para atributos y métodos protegidos.
- "Protegido" significa "ten cuidado al interactuar con esto".
- Las clases hijas pueden acceder a los atributos y métodos protegidos de su clase padre.
- Elige nombres claros para indicar qué debe ser tratado como protegido.