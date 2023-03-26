# Paso a Paso: Día 2

Comenzamos el día dos de creación de nuestro videojuego Snake :snake:. Hoy escribiremos nuestras primeras líneas de código Python y, mejor aún, aprenderemos un concepto fundamental en la programación de hoy en día: la **Programación Orientada a Objetos (POO)**. Así que comencemos por ahí.

## Programación Orientada a Objetos

Los lenguajes de programación que usamos comúnmente son muy genéricos, es decir, están hechos para que puedas programar cualquier programa. Si queremos programar un software para llevar las finanzas de una empresa podemos usar Python, pero si queremos crear un sitio de citas online... ¡también podemos usar Python! Este lenguaje solamente tiene un pequeño conjunto de palabras reservadas y reglas concretas que definen qué es un programa válido en Python. Con esos pequeños bloques podemos construir casi cualquier cosa.

Esto es una gran fortaleza de los lenguajes de programación que tenemos hoy en día pero también nos puede traer problemas. En el mundo de las finanzas, por ejemplo, trabajamos con *pagos*, *cobros*, *deudas*, *inventarios*, etc. Por otra parte, en sitios de citas online trabajaríamos con *perfiles de usuarios*, *gustos personales*, *compatibilidad entre personas*, etc. Parecen dos universos totalmente distintos y, sin embargo, ambos los programamos en ¡el mismo lenguaje! :exploding_head:.

Pero ¿cómo distinguir estos dos universos tan diferentes? ¿Cómo puedo **hablar los idiomas** de cada uno si ambos los hago en el mismo lenguaje de programación?

La respuesta a estas preguntas las tiene la Programación Orientada a Objetos (POO). Este es un concepto más antiguo que el propio Python y defiende el principio de que el diseño de un software debe girar en torno a los objetos o entidades del problema que estamos resolviendo y no centrarse en las funciones y la lógica :nerd_face:. Cuando creamos un software de finanzas cumpliendo con el modelo de POO, expresamos directamente en el código que trabajamos con *pagos*, *deudas* e *inventarios*; mientras que si creamos un sitio de citas vamos a usar en nuestro código *perfiles*, *compatibilidades*, *gustos*, etc.

En nuestro videojuego vamos a usar la POO también, por lo que estaremos trabajando con *serpientes* y *frutas*, además de otros objetos importantes que intervienen en nuestro universo. Pero... ¿cómo podemos incluir estos objetos en nuestros programas? :monocle_face:.

## Clases en Python

Un concepto central en la POO es el de **clase**. Las clases son una plantilla para crear objetos. Por ejemplo, si decimos que la clase **Persona** tiene un nombre, una edad y un estado civil, entonces todas las personas de nuestro software tendrán estas (y solo estas) características. Veamos cómo crear clases en Python y pongámonos manos a la obra :rocket:.

### Primeras clases en Python

Los objetos de nuestro proyecto los definiremos dentro del directorio `src/model`. Allí crearemos dos archivos: el archivo `fruit.py` y el `snake.py`. En estos definiremos las clases para representar a la fruta :strawberry: y a la serpiente :snake: respectivamente.

>**Nota :pen:** A pesar de que este es un curso en español, en nuestro código usaremos el idioma inglés para nombrar clases, funciones, variables, etc. El inglés es el idioma que todos los desarrolladores usamos para programar y poder entender el código de cada uno sin importar nuestro origen. Es muy recomendable que comiences a aprender inglés en caso de que aún no lo domines. En este proyecto te ayudaremos también con eso :wink:

Comencemos por definir la clase `Fruit`. Pensemos, ¿qué es lo que nos interesa del objeto fruta en el juego? En programación debemos ser minimalistas, abstraernos de todo lo que no sea fundamental y extraer la esencia de cada componente de nuestro software. En este caso, de una fruta no nos interesa nada más que su posición en nuestro espacio de juego. Ten en mente que ahora mismo no nos estamos preocupando de cómo vamos a representar esa fruta en el videojuego, sino que estamos construyendo la lógica de nuestro juego, los fundamentos. Y esos fundamentos no incluyen la experiencia del usuario, sino las reglas y la evolución del sistema que describe el juego. Por tanto vamos a definir la clase `Fruit` como sigue:

Archivo **src/model/fruit.py**:
```python
"""Module with the representation of the Fruit entity."""


from dataclasses import dataclass
from typing import Tuple


@dataclass
class Fruit:
    """Representation of the Fruit entity."""

    position: Tuple[int, int]

```

Expliquemos el código anterior. Las líneas entre las comillas triples `"""` son comentarios. Estas líneas no son ejecutadas por el intérprete de Python sino que se usan para describir qué estamos haciendo con el código que escribimos y así hacer que otras personas puedan entender dicho código. El primer comentario que encontramos nos está diciendo que este archivo o módulo contiene la representación de la entidad Fruta.

>**Nota :pen:** En Python se pueden definir comentarios de una línea usando el símbolo `#`. Las comillas triples son usadas para comentarios de varias líneas y para documentar el código.

Lo siguiente que vemos en el código anterior son dos sentencias para importar unas bibliotecas muy especiales de Python. El módulo `dataclass` de la biblioteca `dataclasses` se utiliza para declarar que una clase solamente contiene datos y que no contiene ninguna función. Este es el caso de la clase `Fruit` que solamente va a contener la posición en la que se encuentra. Por otra parte, la biblioteca `typing` contiene tipos de datos que no están definidos en Python por defecto. Como nuestro juego se desarrolla en un plano de dos dimensiones (alto y ancho), la posición de la fruta es una tupla de dos números que definen la ubicación horizontal y vertical de la fruta. Este tipo de datos se llama `Tuple` en la biblioteca `typing`.

Ahora pasamos a definir la clase `Fruit` como tal. Primero declaramos que es una clase que solamente contendrá datos usando la línea `@dataclass`. Luego, en la siguiente línea definimos la clase, usamos la palabra reservada `class` para indicar que vamos a crear una clase y a continuación el nombre de la clase. Luego agregamos los dos puntos `:` para indicar que la línea termina y que a continuación escribiremos el cuerpo de la clase.

>**Nota :pen:** En Python podemos escribir el nombre de una clase de diferentes formas. Hay algunas reglas que debemos cumplir: no debe contener espacios, los únicos caracteres permitidos son letras, número y el caracter `_` y solamente pueden comenzar con una letra o con el caracter `_`. No obstante, nosotros usamos la notación conocida como **PascalCasing**. Comenzamos el nombre siempre con letra mayúscula seguida de letras minúsculas, cada nueva palabra en el nombre comienza con una letra mayúscula. Por ejemplo: `Fruit`, `Snake`, `SnakeFruit`, `AwesomeClassExampleInPascalCase`. Recuerda siempre usar nombres cortos y descriptivos para las clases que definas.

Lo siguiente es otro comentario aclarando qué contiene nuestra clase. Por último, añadimos el campo `position` que representa la posición de la fruta. Además aclaramos el tipo de datos de este campo. Analicemos esta línea:

```python
position: Tuple[int, int]
```

Lo primero es el nombre del campo. En este caso es `position`. Para los nombre de campos, variables y funciones usaremos otro tipo de notación: el **snake_casing**. Esta vez solamente usamos letras minúsculas y números, el caracter `_` lo usamos como sustituto del espacio. Por ejemplo: `position`, `previous_position`, `position_2`.

Luego del nombre agregamos dos puntos `:` para indicar que vamos a definir el tipo de datos. En este caso el tipo es una tupla de dos enteros, uno para representar la posición horizontal y otro para la vertical. Esto lo definimos escribiendo `Tuple[int, int]`.

>**Nota :pen:** En Python no es necesario definir los tipos de datos de los campos de una clase. Podemos solamente definir el nombre sin más. No obstante, es una buena práctica definirlos de esta manera pues de esta forma Python nos alertará cuando parezca que hacemos un mal uso de dicho campo. Por ejemplo, si más adelante en el código intentamos asignar una cadena de texto al campo `position` de una fruta, nos saltará una alerta diciendo que este campo está diseñado para contener una tupla de enteros. Esto nos protege de hacer malos usos de nuestros objetos y funciones por descuido.

Ya tenemos nuestra clase `Fruit`, puedes copiar el código anterior en el archivo `src/model/fruit.py`. Ahora vamos a agregar también la clase `Snake`.

Archivo **src/model/snake.py**:
```python
"""Module with the representation of the Snake entity
along with some util classes such as Direction.
"""


from enum import Enum
from typing import List, Tuple


class Direction(Enum):
    """Enum class representing directions."""

    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3


class Snake:
    """Representation of the Snake entity."""

    def __init__(self, position: Tuple[int, int], direction: Direction, size: int):
        self.position = position
        self.direction = direction
        self.body = self._create_body(position, size)

    def _create_body(
        self, position: Tuple[int, int], size: int
    ) -> List[Tuple[int, int]]:
        """Generates the body of the snake starting from the
        position of the head. The body will be of size `size`
        and the snake will be placed horizontally, facing right.

        Args:
            position (Tuple[int, int]): The position of the head.
            size (int): Size of the snake.

        Returns:
            List[Tuple[int, int]]: Body of the snake, including the head.
        """
        body = [position]
        body.extend((body[i - 1][0] - 10, position[1]) for i in range(1, size))
        return body

    def move(self):
        """Updates the position of the head."""
        if self.direction == Direction.RIGHT:
            self.position = (self.position[0] + 10, self.position[1])
        elif self.direction == Direction.LEFT:
            self.position = (self.position[0] - 10, self.position[1])
        elif self.direction == Direction.UP:
            self.position = (self.position[0], self.position[1] - 10)
        else:
            self.position = (self.position[0], self.position[1] + 10)
        self._grow()

    def _grow(self):
        """Inserts the position of the head as the front position in the body."""
        self.body.insert(0, self.position)

    def trim(self):
        """Removes the tail of the body."""
        self.body.pop()

    def change_direction(self, new_direction: Direction):
        """Changes the direction of the snake in case the new direction
        is not opposite to the current direction.

        Args:
            new_direction (Direction): The candidate direction to change.
        """
        if not self._are_opposites(self.direction, new_direction):
            self.direction = new_direction

    def _are_opposites(self, direction1: Direction, direction2: Direction):
        return (
            (direction1 == Direction.RIGHT and direction2 == Direction.LEFT)
            or (direction1 == Direction.LEFT and direction2 == Direction.RIGHT)
            or (direction1 == Direction.UP and direction2 == Direction.DOWN)
            or (direction1 == Direction.DOWN and direction2 == Direction.UP)
        )

```

Ufff las cosas parecen complicarse bastante con esta clase. Pero descuida, vamos a explicarte todo paso a paso y verás que no es tan complicado. Ya conoces los comentarios y la biblioteca `typing`. Aquí además usamos la clase `Enum` de la biblioteca `enum`.

Los enumerables son tipos de datos que toman un conjuto fijo de valores. En este caso lo usaremos para definir las direcciones en las que puede moverse nuestra serpiente, estas direcciones son cuatro a saber: izquierda :arrow_left:, derecha :arrow_right:, arriba :arrow_up: y abajo :arrow_down:. Como los valores solamente pueden ser uno de estos cuatro posibles, un enumerable parece ser la opción indicada para representar la dirección. Es por eso que usamos la clase `Enum` para definir la clase `Direction`. A los campos de estos tipos de clase se les asigna un número entero. A partir de ahora para referirnos a la dirección derecha, por ejemplo, usamos `Direction.RIGHT`. En la siguiente lección explicaremos más a fondo por qué esta clase se define de esta manera.

>**Nota :pen:** Para nombrar constantes y opciones de los enumerables usamos letras mayúsculas y el caracter `_` como sustituto del espacio entre palabras.

¿Qué necesitamos de nuestra serpiente? Como datos necesitamos la posición en la que se encuentra la cabeza, la dirección en la que se está desplazando y la posición de cada parte de su cuerpo. Pero no solo eso, también necesitamos una forma de crear la serpiente inicialmente, desplazarla en la dirección actual, incrementar su tamaño cuando come una fruta y cambiar su dirección. Es por eso que debemos incluir **funciones** además de sólo datos. Esta vez no usaremos `dataclass`.

Casi siempre, la primera función que definiremos en una clase de Python es la función `__init__`. En esta función se crea el objeto específico que queremos. Le pasamos los parámetros necesarios y obtenemos el objeto. Pero primero hagamos un breve resumen de cómo definiremos cualquier función dentro de una clase.

```python
def nombre_de_funcion(self, parametro1: Tipo1, parametro2: Tipo2) -> TipoRetorno:
    ...
    cuerpo de la funcion
    ...
```

Lo primero es la palabra reservada `def` que indica que estamos definiendo una función. Luego el nombre de la función, en nuestros ejemplos usaremos el **snake_casing**. Entre paréntesis irán los parámetros de nuestra función. El primero de ellos siempre será `self` que es una referencia al objeto mismo, o sea, a la serpiente misma en este caso. Luego vienen los demás parámetros necesarios. Escribimos el nombre de dicho parámetro seguido de dos puntos y de su tipo. El tipo no es necesario pero es recomendable definirlo y lo estaremos haciendo de esa manera en nuestros ejemplos. Los parámetros se separan por comas. Por último, si nuestra función nos devuelve algo, definiremos el tipo de dato que nos devuelve usando el operador `->` seguido de dicho tipo de dato. Terminamos la declaración con `:` para indicar que comenzaremos a escribir el cuerpo de la función.

> :warning: Es importante recordar que en Python los espacios importan. El cuerpo de una función, clase, ciclo, condicional, etc debe ir siempre indentado con respecto a la declaración. En el ejemplo anterior, nota como el cuerpo de la función se comienza a escribir dejando un espacio al inicio de la línea para que quede completamente indentado con respecto a la declaración de la función. Los editores modernos de Python nos ayudan con esto.

Puedes copiar todo el código escrito anteriormente para la clase `Snake` en el archivo `src/model/snake.py`. Sabemos que quedan muchas preguntas por responder sobre esta clase. Todas esas preguntas las vamos a respoder en la siguiente lección de manera más detallada. Creemos que ha sido suficiente por hoy. Puedes echar un ojo a todo lo que hemos visto y repasar los códigos que hemos escrito.

En resumen, hoy aprendimos sobre el paradigma de la **Programación Orientada a Objetos (POO)** que nos dice que debemos crear el software alrededor de los datos y objetos que intervienen en el problema y no de la lógica. Para ello, vimos que una clase es una plantilla que define a los objetos y a partir de la cual podremos crear instancias de dichos objetos. Pero no nos quedamos solamente en la teoría y creamos nuestras primeras clases para definir las entidades que intervienen en nuestro videojuego: la fruta y la serpiente. La clase `Fruit` es una clase muy simple que solamente incluye la posición en la que se encuentra dicha fruta en el espacio. Por otra parte, la clase `Snake` es mucho más compleja y la estaremos analizando línea a línea en la próxima lección.

Adicionalmente aprendimos sobre tipos de datos, enumerables, funciones; convenciones para nombrar clases, campos, parámetros, funciones, etc :sleepy:. En fin, que fue un día intenso y bien vale que volvamos a analizar todo lo que hemos aprendido y hecho hoy.

En la siguiente lección conoceremos la POO más a fondo. Mencionaremos algunos elementos avanzados de Python y comprenderemos a detalle la clase `Snake`. Esto nos dejará listo el terreno para empezar a programar las interacciones de nuestro juego. ¡Nos vemos pronto! :wave:
