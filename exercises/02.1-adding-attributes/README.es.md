# ¡Construyamos una Clase de Estudiante! 📚

¿Recuerdas cómo hablamos de que las clases tienen atributos (como características)? Ahora vamos a crear una clase `Student` que muestra cómo usar tanto atributos de clase (cosas que todos los estudiantes comparten) como atributos de instancia (cosas únicas para cada estudiante).


## 📝 Instrucciones

1. Define una clase llamada `Student` en `app.py`

2. **Añade un atributo de clase.** Declara un atributo de clase llamado school_name y asígnale el valor "Python Academy". Nota: Este atributo será compartido por todos los estudiantes.

3. **Define tres atributos.** Dentro del método __init__, configura los siguientes atributos: name, age, grade

4. **Define un método llamado student_info.** Este método debe retornar una descripción que incluya el nombre, la edad, el grado del estudiante y el nombre de la escuela.
Ejemplo: 

```python
"Alice is 15 years old, in 10th grade, and studies at Python Academy."
```

5. Instancia de la clase Student 2 nuevos objetos con los siguientes valores:

```python
student1 = Student("Alice", 15, "10th")  
student2 = Student("Bob", 16, "11th")  
```

6. Imprime la información de cada estudiante llamando el metodo `student_info`


## 💡 ¿Necesitas Ayuda?

- Los atributos de clase van fuera de `__init__` (¡son para todos!)
- Los detalles personales van dentro de `__init__` (son solo para ese estudiante)
- Usa f-strings para que tu método `student_info` se imprima de manera agradable
- Recuerda usar `self` cuando trabajes con atributos de instancia