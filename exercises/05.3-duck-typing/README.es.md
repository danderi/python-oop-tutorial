# ¡Creando Manejadores de Datos Inteligentes - Al Estilo Duck Typing! 🦆

Vamos a aprender algo divertido llamado "duck typing" construyendo diferentes formas de manejar datos. ¿Sabes cómo dicen "si camina como un pato y grazna como un pato, es un pato"? ¡Eso es exactamente lo que vamos a hacer con el código!

Para este ejercicio crearemos diferentes procesadores de datos **(JsonProcessor, CsvProcessor, XmlProcessor)** y un **DataManager** genérico que pueda trabajar con cualquiera de ellos, sin preocuparse de qué tipo son. Esto es útil para aprender duck typing porque cada formato necesita ser manejado de manera diferente, además:

- Nos enfocamos en el comportamiento, no en la herencia o los tipos de clase.
- Podemos agregar nuevos procesadores sin cambiar el código existente.
- Es un ejemplo perfecto de la flexibilidad de Python.

¡Empecemos!

## Instrucciones

1. Define 3 clases para manejar datos en diferentes formatos `JsonProcessor, CsvProcessor, XmlProcessor` y definele a cada procesador los siguientes métodos: `load_data(data), process(), export()`

```python
#Example
class JsonProcessor:
    def load_data(self, data):
        self.data = f"Loading JSON data: {data}"

    def process(self):
         self.data = f"Processing JSON data: {self.data.upper()}"  # Convert to uppercase as an example

    def export(self):
        return f"Exporting JSON data: {self.data}"
```

2. Luego define una clase `DataManager` que tenga un método `process_data(data)` y que funcione con cualquier procesador que tengan los métodos:

- load_data: para cargar datos.
- process: para procesarlos.
- export: para exportarlos.

Al DataManager no deberia importarle qué procesador recibe, solo usa cualquier procesador que le des.

3. **Prueba tu solución.** Crea instancias de la clase `JsonProcessor, CsvProcessor, XmlProcessor` y verifica que funcionen correctamente.


```python
# Create your processors
json_proc = JsonProcessor()
csv_proc = CsvProcessor()
xml_proc = XmlProcessor()

# Test with different data
json_data = '{"name": "John", "age": 30}'
csv_data = 'name,age\nJohn,30'
xml_data = '<person><name>John</name><age>30</age></person>'

# JSON Processor
manager = DataManager(json_proc)
print(manager.process_data(json_data))  # Process and display results for JSON

# CSV Processor
manager = DataManager(csv_proc)
print(manager.process_data(csv_data))  # Process and display results for CSV

# XML Processor
manager = DataManager(xml_proc)
print(manager.process_data(xml_data))  # Process and display results for XML
```

## 💡 Consejos

- No necesitas herencia o clases abstractas
- Solo asegúrate de que cada procesador tenga los mismos nombres de métodos
- Enfócate en lo que las cosas pueden hacer, no en lo que son
- Piensa "¡si puede procesar datos, es un procesador!"
