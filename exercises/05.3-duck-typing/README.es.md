# ¡Creando Manejadores de Datos Inteligentes - Al Estilo Duck Typing! 🦆

Vamos a aprender algo divertido llamado "duck typing" construyendo diferentes formas de manejar datos. ¿Sabes cómo dicen "si camina como un pato y grazna como un pato, es un pato"? ¡Eso es exactamente lo que vamos a hacer con el código!


Piensa en los diferentes tipos de archivos en tu computadora algunos archivos son JSON (como archivos de configuración), algunos son CSV (como hojas de cálculo), algunos son XML (como datos web). Son diferentes, ¡pero queremos manejarlos todos fácilmente!

Esto es perfecto para aprender duck typing porque:
- Cada formato necesita ser manejado de manera diferente
- Pero queremos usarlos todos de la misma manera. No nos importa qué tipo son, solo lo que pueden hacer.

## Instrucciones

1. Crearemos tres manejadores de datos diferentes:
    - `JsonProcessor` para datos JSON (como configuraciones web)
    - `CsvProcessor` para datos CSV (como archivos de hojas de cálculo)
    - `XmlProcessor` para datos XML (como páginas web)

2. Cada procesador sabrá cómo:
    - Cargar datos desde una cadena
    - Procesar los datos (ponerlos en mayúsculas en nuestro ejemplo)
    - Exportar los datos procesados

3. Luego haremos un `DataManager` inteligente que:
    - No le importa qué procesador recibe
    - Solo usa cualquier procesador que le des
    - Funciona con cualquier procesador que tenga los métodos correctos

## 💡 ¿Necesitas Ayuda?

- No necesitas herencia o clases abstractas
- Solo asegúrate de que cada procesador tenga los mismos nombres de métodos
- Enfócate en lo que las cosas pueden hacer, no en lo que son
- Piensa "¡si puede procesar datos, es un procesador!"

## ¿Por Qué Duck Typing? 🦆

El duck typing es genial porque:
1. Es súper flexible - ¡agrega nuevos procesadores en cualquier momento!
2. No hay relaciones complicadas entre clases
3. Solo asegúrate de que las cosas puedan hacer lo que se necesita
4. Como tener diferentes controles remotos que todos tienen un botón de encendido

## ¿Qué Debería Pasar? 🎯

Cuando ejecutes tu código:
```python
# Crea tus procesadores
json_proc = JsonProcessor()
csv_proc = CsvProcessor()
xml_proc = XmlProcessor()

# Prueba con diferentes datos
json_data = '{"name": "John", "age": 30}'
csv_data = 'name,age\nJohn,30'
xml_data = '<person><name>John</name><age>30</age></person>'

# Procesa cada tipo
for processor, data in [(json_proc, json_data), 
                              (csv_proc, csv_data),
                              (xml_proc, xml_data)]:
     manager = DataManager(processor)
     manager.process_data(data)
     print(manager.get_processed_data())  # ¡Cada procesador muestra sus resultados!

# Crea un procesador personalizado - ¡simplemente funciona!
class CustomProcessor:
     def load_data(self, data): pass
     def process(self): pass
     def export(self): return "Datos procesados personalizados"

custom = DataManager(CustomProcessor())  # ¡Funciona perfectamente!
```

Piénsalo como tener diferentes herramientas de cocina - mientras puedan cortar vegetales, no importa si es un cuchillo, un procesador de alimentos o un gadget sofisticado. ¡Si puede hacer el trabajo, funciona! 🔨