# Entendiendo las Partes de una Clase: Atributos y Métodos 🧩

Ahora que has creado tu primera clase, hablemos de las dos partes principales que componen una clase: atributos y métodos. ¡No te preocupes, son más simples de lo que parecen!

## Piénsalo Como un Robot de Juguete 🤖

Imagina que tienes un robot de juguete:
- **Atributos** son como las características del robot (su color, altura, nivel de batería)
- **Métodos** son como las cosas que el robot puede hacer (bailar, hablar, moverse hacia adelante)

## ¡Dos Tipos de Cada Uno! 📦

1. **Atributos y Métodos de Instancia**
   - Estos pertenecen a cada cosa individual que creamos
   - Como cada robot tiene su propio nivel de batería
   - Creamos estos usando `self` dentro de `__init__`

2. **Atributos y Métodos de Clase**
   - Estos son compartidos por todas las instancias de la clase
   - Como todos los robots de la misma fábrica pueden compartir el mismo número de modelo
   - Creamos estos fuera de `__init__`

## Ejemplo del Mundo Real 🌟

Piensa en los estudiantes de una escuela:
- **Atributos de Instancia**: El nombre, edad y calificaciones de cada estudiante (diferentes para cada estudiante)
- **Atributos de Clase**: Nombre de la escuela, mascota de la escuela (igual para todos los estudiantes)
- **Métodos de Instancia**: Tomar un examen, hacer la tarea (acciones que hace cada estudiante)
- **Métodos de Clase**: Anunciar un día festivo escolar (afecta a todos los estudiantes)

En el próximo ejercicio, crearemos una clase `Student` que pondrá en práctica estas ideas. ¿Listo para intentarlo? ¡Vamos! 🚀