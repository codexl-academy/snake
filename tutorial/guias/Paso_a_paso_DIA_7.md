# Paso a Paso: Día 7

¡Hoy es el gran día! Finalizaremos nuestro proyecto y podremos jugar nuestro propio videojuego. Además reflexionaremos sobre todo lo que hemos hecho, cuánto hemos aprendido y, más importante aún, cuánto nos queda por aprender. De esta forma sabrás el camino a seguir para continuar tu aprendizaje. Así que sin más dilación... ¡comencemos! :rocket:

## Últimos pasos para ejecutar el juego

A pesar de que ya hemos hecho toda la lógica de nuestro juego todavía no podemos jugarlo. Esto lo vamos a arreglar de inmediato. ¿Recuerdas el archivo **main.py** que creamos desde el primer día? No lo hemos usado aún, y precisamente es lo último que haremos para ejecutar nuestro videojuego. Añade el siguiente código:

Archivo **src/main.py**:

```python
from game_state.game import Game

if __name__ == "__main__":

    game = Game()
    game.run()

```

¿Te esperabas mucho más código? Pues no, con estas pocas líneas basta para terminar nuestro juego. Lo primero que hacemos es importar la clase `Game` que creamos el día anterior. Luego lo único que tenemos que haces es crear un objeto a partir de esa clase y llamar a la función `run` que como ya sabemos ejecuta todo el ciclo del juego.

Hay, no obstante, una línea un poco extraña: `if __name__ == "__main__":`. Todo lo hacemos dentro de esta sentencia `if`. Esta es una línea que aparece muchísimo en los scripts de Python. Con esto queremos decir que todo el código dentro de este *if* se ejecuta cuando es el intérprete de Python quién está llamando directamente al archivo. Por ejemplo, nuestro archivo **game.py** dentro del módulo **game_state** está siendo importado en **main.py**. Por tanto, todo el código de **game.py** se ejecuta. Pero no estamos ejecutando directamente ese archivo, sino que lo estamos importando en otro archivo. Por otra parte, si **main.py** fuera importado desde un nuevo archivo, entonces todo el código dentro del *if* **no** sería ejecutado. Este código se ejecuta solamente cuando llamamos al script directamente desde el intérprete de Python.

Para que ordenarle al intérprete ejecutar **main.py** vamos a abrir una terminal en el directorio **src** y escribimos:

```bash
python main.py
```

>:warning: Ten en cuenta que puede que tengas que usar el comando `python3` en lugar de `python`.

¡Y ya está! ¡Ya puedes jugar tu propio videojuego! :rocket:

Ahora entretente durante un rato con el videojuego que has creado. Te lo mereces.

## ¿Qué hemos aprendido?

Luego de jugar, sería bueno echar un vistazo a atrás y hacer un recuento de todo lo que hemos aprendido. Haremos una lista aquí pero esta lista no es exhaustiva. Cada persona tendrá su propia lista de acuerdo a todo lo que haya experimentado e investigado a partir de este tutorial. Pero entre las cosas que a todos nos deben haber quedado claras están:

1. **Instalar Python, pip, Visual Studio Code y algunas bibliotecas como Pygame y pytest**: Esto es lo que siempre necesitaremos para crear proyectos con Python.
2. **Organizar un proyecto por módulos que se relacionan entre sí**: Aunque parezca algo simple, la organización y la separación de responsabilidades es quizás la principal habilidad que todo desarrollador debería adquirir, y es también una de las habilidades que más valoran las empresas.
3. **Programación Orientada a Objetos**: Este es el paradigma dominante en la industria del software de hoy. Aquí aprendimos varios de los conceptos fundamentales como **clases** y **herencia**. Si la curiosidad te pudo, quizás también aprendiste sobre otros conceptos como **encapsulamiento** o **polimorfismo**. Más adelante hablaremos de todo esto en próximas guías y en nuestro blog.
4. **Convenciones de nombres en Python**: El código que escribimos debe ser fácil de leer y entender. Esto es una premisa fundamental, es indispensable que escribas código claro y limpio. Las convenciones de nombre nos ayudan a lograr este objetivo. Aprendimos las convenciones para nombrar clases, funciones, variables, etc.
5. **Tipos de datos en Python y herramientas avanzadas como `Enum`, `dataclass` y `staticmethod`** que nos permiten crear programas más robustos. En este proyecto hicimos un uso **profesional** de estas herramientas que se puede decir que son avanzadas en la programación.
6. **Algoritmia y abstracción**: Para crear nuestro juego tuvimos que implementar lógicas bastante complejas sobre la dinámica del juego. Nos abstraímos de los conceptos habituales de serpiente o fruta y nos quedamos con la esencia, lo fundamental para nuestro juego. Estas son habilidades muy difíciles de conseguir. En este proyecto tuvimos la oportunidad de ponerlas en práctica.
7. **Manejo avanzado de listas**: Vimos el **list comprehension** y el **slicing** entre otras técnicas avanzadas para el manejo de listas en Python. Además usamos muchísimas funciones de listas como **append**, **extend**, **pop**, **any**, etc.
8. **Pruebas automátizadas**: En su momento lo repetimos mucho pero vale la pena repetirlo una vez más. Las pruebas automatizadas son indispensables en la industria del software de hoy en día. Esta es otra de las habilidades más valoradas por las empresas. En este proyecto enseñamos cómo crear pruebas automatizadas en Python usando la biblioteca pytest.
9. **Uso de la biblioteca Pygame**: No importa si luego no te interesa crear más videojuegos, lo que has aprendido en este proyecto sobre cómo usar una biblioteca tan grande como lo es Pygame te va a acompañar y a ser útil siempre. Aprendimos cómo importarla, cómo dibujar, actualizar las pantallas, controlar el tiempo, leer las acciones del usuario y actuar de acuerdo con esas acciones, cerrar el juego, etc.
10. **Uso de otras bibliotecas incluídas en Python como `random`, `time` y `sys`**: Nuestro proyecto es complejo y necesita muchas herramientas sofisticadas para funcionar correctamente. Es por eso que tuvimos que aprender a generar números aleatorios, manipular el tiempo e interactuar con el sistema de nuestro ordenador. Para todo esto usamos bibliotecas que nos facilitan las cosas.
11. **Engranar todas las piezas de un proyecto para conformar un todo**: Si es importante saber dividir nuestros proyectos en pequeños módulos, igualmente importante es orquestar todas esas piezas para que funcionen adecuadamente y den vida a nuestros programas. Eso también lo aprendiste aquí.

>**Nota :pen:** Si no recuerdas algunas de las cosas que mencionamos en la lista, no te preocupes. Regresa al código y a los tutoriales tantas veces como necesites y experimenta con el proyecto. (Esta es la última **Nota :pen:** de este tutorial :cry:).

Pero esto es sólo el comienzo. Ahora te mostraremos cómo puedes seguir tu camino por si te quedaste con ganas de más (que esperamos que así sea).

## ¿Qué nos falta por aprender?

A pesar de que hemos aprendido muchísimo en un tiempo récord, hay muchas cosas que nos quedan por conocer. Pero esto no debe ser motivo para que te desanimes. Al contrario, debería despertar tu curiosidad y tus ganas de aprender. Entre las cosas que faltan por aprender están:

1. **Programación Orientada a Objetos avanzada**: Además de los conceptos que ya hemos mencionados hay otros como el de **interface** y los principios **SOLID**.
2. **Decoradores**: Los decoradores son uno de los recursos más potentes de Python. En este proyecto usamos varios de ellos pero no tenemos todavía mucha idea de qué son y cómo crearlos.
3. **Estructuras de datos**: Uno de los temas preferidos en las entrevistas de trabajo. En este proyecto vimos estructuras simples como listas y tuplas pero hay muchísimas más y mucho más complejas.
4. **Patrones de diseño**: Estos no son más que soluciones a problemas muy comunes que surgen cuando creamos software. Conocerlos e implementarlos en problemas reales es una fuente incalculable de conocimiento y experiencia.
5. **Otros conceptos avanzados de Python** como los métodos mágicos, *unpacking* y clausuras.
6. Utilidades como **escritura y lectura de archivos**, **ejecución de procesos** y **manejo del sistema de archivos** desde código Python.

Muchísimos artículos se han escrito sobre todo esto. Muchos de ellos muy buenos y otros no tanto. La gran mayoría de ellos están en inglés. No obstante, si te ha gustado esta experiencia de **aprender haciendo**, te tenemos buenas noticias.

Estamos comenzando a preparar una **Versión Premium** de este proyecto donde añadiremos muchísimas cosas nuevas y pondremos en práctica todo lo que mencionamos en el listado anterior y mucho más. Por ejemplo, pensamos mejorar el juego agregando:

1. **Modalidad multijugador** donde puedes jugar con alguien más y competir por ver quién se lleva más frutas.
2. **Modalidad *humano vs. computadora***: Crearemos una especie de *inteligencia artificial* que hará que la serpiente controlada por nuestro programa sea invencible.
3. Capacidad para **salvar el progreso del juego**.
4. **Configuraciones** de la dificultad y el aspecto del juego.
5. **Mejoras en el código** para enfrentar problemas que surgen a la hora de querer hacer todos estos cambios.
6. **Testing avanzado**.
7. **Contacto directo con nosotros** para aclarar cualquier duda sobre Python que te surja.

Esto no es todo lo que aprenderás en la **Versión Premium**. Incluiremos muchísimas cosas más. De hecho, queremos escuchar qué más quisieras que incluyéramos en este nuevo proyecto. Dinos lo que te interesa en [este LINK](https://codexlacademy.com/#form01) y déjanos tu email para que te puedas enterar de todos los detalles sobre esta nueva etapa del proyecto.

Y eso no es todo, sino que puedes esperar muchas más formaciones de nuestra academia y aprender muchísimo de nuestro [blog](https://blog.codexlacademy.com) y nuestra [newsletter semanal](https://codexl.substack.com).

Y ahora sí que sí. Ponemos punto final a nuestro proyecto. Esperamos que hayas aprendido muchísimo y te hayas divertido. Si es así, no dudes en compartir este conocimiento cualquiera que conozcas y que esté interesado en  la programación. De nuestra parte, estamos extremadamente agradecidos porque hayas decidido recorrer todo este camino con nosotros y si esto ha provocado un cambio positivo en tu vida, ya quedamos más que contentos. De todo corazón...

¡Muchas gracias por leernos!
