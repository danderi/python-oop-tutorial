# Herencia Múltiple en Python

## 📝 Instrucciones

1. Crea tres clases base en `app.py`:
    - `Flying` con un método `fly()` que imprime "¡Puedo volar!"
    - `Swimming` con un método `swim()` que imprime "¡Puedo nadar!"
    - `Bird` con atributos `name` y `species`

2. Crea una clase llamada `Duck` que herede de las tres clases:
    - En el método __init__ de `Duck`, utiliza `super().__init__()` para llamar al constructor de `Bird` como lo hicimos en el ejericio anterior.
    - Define un método `introduce()` que imprima: `"I'm {name}, a {species} that can both fly and swim!`

3. **Prueba tu solución.** Crea una instancia de la clase `Duck` llamada `duck` con:

```bash
name: "Donald"
specie: "Mallard"
```

Al ejecutar el código de prueba debería imprimir:

```python
"I'm Donald, a Mallard that can both fly and swim!"
"I can fly!"
"I can swim!"
```

## 💡 Consejos

- Usa herencia múltiple listando todas las clases padre: `class Duck(Bird, Flying, Swimming):`
- El orden de herencia importa (Orden de Resolución de Métodos - MRO)
- Usa `super().__init__()` para inicializar correctamente las clases padre