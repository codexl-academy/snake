# Paso a Paso: Día 3

Ya tenemos conocimientos básicos sobre POO y clases en Python. No obstante, del día anterior quedan algunas *cosas sueltas* que vamos a explicar para que todo quede bien claro y poder continuar haciendo nuestro videojuego. Este día contendrá un poco más de teoría y estará dedicado principalmente a entender todo el código que se implementó el día anterior. Además explicaremos brevemente un concepto fundamental en la POO: **la herencia**.

¡Comencemos! :rocket:

## La Herencia

El día anterior definimos un tipo de dato enumerable en Python de la siguiente forma:

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
```

Definimos la clase `Direction` de una manera un poco *rara*. Luego del nombre de la clase usamos los paréntesis encerrando a la clase `Enum`. ¿Qué representa esto? Esto representa que nuestra clase `Direction` **hereda** de la clase `Enum`.

Ya comentamos que el enfoque de la POO es programar tomando en cuenta las entidades que intervienen en el problema por encima de la lógica y las funciones. En muchas ocasiones estas entidades se relacionan entre sí de una manera jerárquica, como si unas pudieran verse como un caso particular de las otras. Mejor pongamos un ejemplo:

Supongamos que tenemos una clase `Persona` que contiene los campos `edad`, `sexo` y `estado_civil`. Ahora queremos añadir un nuevo tipo de persona, una `PersonaConEmpleo`. Esta, además de tener toda la información de una persona, contiene un nuevo campo `salario`. ¿Cómo representamos esto en Python?

```python

class Persona:

    def __init__(self, edad, sexo, estado_civil):
        self.edad = edad
        self.sexo = sexo
        self.estado_civil = estado_civil

class PersonaConEmpleo:

    def __init__(self, edad, sexo, estado_civil, salario):
        self.edad = edad
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.salario = salario
```

Más adelante ahondaremos en la función `__init__` en las clases de Python. Por ahora solamente decir que es el método que se usa para iniciar un objeto de esa clase. En esta función creamos los campos que tiene nuestra clase y le asignamos los valores con los que deseamos inicializar cada uno de esos campos. Por ejemplo, cuando escribimos `self.edad = edad`, estamos creando el campo `edad` en la clase y asignándole el valor del parámetro `edad`.

Nota como en el caso de la clase `PersonaConEmpleo` tenemos que repetir el mismo código para los campos que ya contiene la clase `Persona`. Esto es ya de por sí un problema, estamos trabajando el doble. Además, si luego decidimos cambiar el nombre de algún campo en la clase `Persona` (por ejemplo cambiar el campo `sexo` por `genero`), entonces tendríamos que cambiar también la clase `PersonaConEmpleo`. En un software con miles de líneas de código y decenas de clases que se relacionan de esta forma, esta situación se vuelve insostenible.

Afortunadamente tenemos **la herencia**. Es evidente que una `PersonaConEmpleo` es un caso particular de una `Persona`. Es decir, es una persona que **además** tiene otros atributos y/o comportamientos. Cuando esto sucede, decimos que `PersonaConEmpleo` **hereda** de `Persona`. Y en Python podemos expresarlo de la siguiente manera:

```python

class Persona:

    def __init__(self, edad, sexo, estado_civil):
        self.edad = edad
        self.sexo = sexo
        self.estado_civil = estado_civil

class PersonaConEmpleo(Persona):

    def __init__(self, edad, sexo, estado_civil, salario):
        super().__init__(edad, sexo, estado_civil)
        self.salario = salario
```

En la clase `PersonaConEmpleo` anterior expresamos la relación "`PersonaConEmpleo` **hereda** de `Persona`" con los paréntesis a continuación del nombre `PersonaConEmpleo`. Nuestro método `__init__` sigue recibiendo los mismos parámetros, después de todo estamos inicializando a una persona. Pero esta vez no es necesario repetir el código sino que usamos la función especial de Python `super`, que nos da una referencia al padre de nuestra clase, en este caso la clase `Persona`. Entonces podemos reusar el método `__init__` de nuestra clase padre y así ahorrarnos dolores de cabeza a futuro.

>> **Nota :pen:** En la terminología de la programación orientada a objetos se le llama clase **hijo** a la clase que hereda y clase **padre** a la clase de la cual se hereda.

Es por eso que para crear nuestra clase `Direction` necesitamos heredar de la clase `Enum` y especificar los campos que queremos incluir.

>> **Nota :pen:** Si tienes buena memoria te estarás preguntando por qué cuando definimos la clase `Fruit` no heredamos de `dataclass` sino que usamos una línea al inicio: `@dataclass`. En este caso, `dataclass` no es una clase de la cual heredamos sino que es un **decorador**. El concepto de decorador en Python es más complejo y su explicación escapa del alcance de estas guías. Por el momento limitémonos a conocer su uso en casos específicos como este. En futuros proyectos y posts en [nuestro blog](https://blog.codexlacademy.com) trataremos este tema en profundidad.

## Entendiendo la clase Snake

Ya conocimos la herencia en Python pero queda mucho del código del día anterior que no hemos explicado. Epecíficamente la clase `Snake`. Veamos de nuevo esta clase:

Archivo **src/model/snake.py**:

```python
class Snake:
    """Representation of the Snake entity."""

    def __init__(self, position: Tuple[int, int], direction: Direction, size: int):
        self.position = position
        self.direction = direction
        self.body = self._create_body(position, size)

    def _create_body(self, position: Tuple[int, int], size: int) -> List[Tuple[int, int]]:
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

Comencemos por el método `__init__` que ya conocemos. En este caso, el método recibe los parámetros `position` que representa la posición inicial de la cabeza de la serpiente y es de tipo tupla de dos enteros, `direction` que representa la dirección inicial hacia la que se mueve la serpiente y es del tipo enumerable `Direction` y `size` que representa el largo de la serpiente y es un número entero. En las primeras dos líneas del método creamos los campos `position` y `direction` como ya habíamos visto. Sin embargo, la tercera línea del método es un poco distinta. Estamos creando el campo `body` (cuerpo) de la serpiente pero le estamos asignando el resultado de un llamado a una función.

### Función `_create_body`

Con la función `_create_body` creamos el cuerpo de la serpiente. Esta función está justo debajo de la función `__init__` y recibe la posición de la cabeza y el largo que va a tener el cuerpo. En el comentario inicial nos explican que el cuerpo es generado comenzando por la posición de la cabeza y extendiéndolo horizontalmente de forma que la serpiente quede mirando hacia la derecha. Esta función nos devuelve una lista de tuplas de dos enteros. Esta lista contendrá las coordenadas de cada parte del cuerpo de la serpiente. Inicialmente el cuerpo contiene solo la cabeza de la serpiente: `body = [position]` (una lista con una única tupla con las coordenadas de la cabeza).

La siguiente línea es un poco complicada. Vamos a dividirla. Primeramente analizaremos lo que está entre los paréntesis internos:

```python
(body[i - 1][0] - 10, position[1])
```

Primero que todo tenemos que decir que las posiciones en nuestro juego se representan por tuplas de dos enteros. El primer entero es la **coordenada horizontal**. Mientras mayor sea el valor de esta coordenada, más a la derecha en la pantalla estará el elemento. El segundo entero es la **coordenada vertical**. Mientras mayor sea el valor de esta coordenada, más hacia arriba estará el elemento. Ahora, analicemos el código anterior.

En Python podemos definir una tupla colocando sus valores entre paréntesis y separados por coma. Esta tupla tiene como primer valor `body[i-1][0] - 10`. Recordemos que `body` es una lista de tuplas. Por tanto `body[i-1]` es una tupla. Es la tupla que se encuentra en la posición `i-1` de la lista `body`. En unos instantes veremos de dónde sale `i`.

>**Nota :pen:** Las posiciones en las listas comienzan en cero. Es decir, la tupla que está en la primera posición de la lista `body` es `body[0]`.

Por tanto, `body[i-1][0]` es la primera coordenada de la tupla de dos enteros que está en la posición `i-1` de la lista `body`. Y `body[i-1][0] - 10` es dicha coordenada disminuida por `10`. Ya sabemos cuál es la primera coordenada de la tupla del código anterior. La segunda coordenada es `position[1]`. Recordemos que position es la tupla que representa la posición de la cabeza de nuestra serpiente. Que la coordenada vertical de todas las partes del cuerpo de la serpiente tengan el mismo valor (el mismo que el de la posición inicial de la cabeza `position[1]`) significa que lo único que varía es la posición horizontal. O sea, que la serpiente se extiende horizontalmente. Además, como vimos anteriormente, cada nueva parte del cuerpo tiene una posición horizontal igual a la anterior disminuida por 10. Esto quiere decir que la cola de la serpiente se extiende hacia la izquierda de la pantalla inicialmente y la cabeza es lo que queda más a la derecha. Justo como lo describe el comentario al inicio de la función.

Veamos el contexto dentro del cuál se está definiendo la tupla que describimos anteriormente:

```python
(body[i - 1][0] - 10, position[1]) for i in range(1, size)
```

De aquí es de donde viene la variable `i`. En Python podemos definir colecciones ordenadas de elementos (en este caso tuplas de dos enteros) usando la técnica que se conoce como *list comprehension*. El código anterior se puede entender mejor si comenzamos a leerlo a partir de la palabra `for`.

>Para cada `i` en el rango de `1` a `size`, se define la tupla `(body[i - 1][0], position[1])`.

Recordemos que `size` es un número que define el tamaño de la serpiente.

>**Nota :pen:** La función `range` nos devuelve una colección oredenada del rango de números que determinan sus argumentos. Por ejemplo, `range(0, 3)` devuelve la colección `[0, 1, 2]`. O sea todos los números enteros entre el primer parámetro y el segundo, excluyendo el segundo.

Para ilustrar mejor, tomemos `position = (30, 2)` y `size = 3`. ¿Qué colección nos devuelve el código anterior? En primer lugar recordemos que inicialmente `body = [position]`, o sea, `body = [(30,2)]` en nuestro ejemplo. La variable `i` toma los valores sucesivos `1, 2` debido a que `size = 3`. Por tanto:

```python
# cuando i = 1
(body[i - 1][0] - 10, position[1]) = (20, 2)

# cuando i = 2
(body[i - 1][0] - 10, position[1]) = (10, 2)

# la colección queda
[(20, 2), (10, 2)]
```

>**Nota :pen:** Seguramente te preguntarás por qué restamos 10 a cada posición. En nuestro juego esta es la separación mínima en pantalla: 10 píxeles.

El último eslabón para comprender la línea entera es la función `extend`:

```python
body.extend((body[i - 1][0] - 10, position[1]) for i in range(1, size))
```

Como `body` es una lista, tiene todas las funciones que Python tiene predefinidas para sus listas. Una de esas funciones es `extend`. La función `extend` recibe una colección y la concatena con la lista actual. Siguiendo el ejemplo anterior, si tenemos inicialmente `body = [(30, 2)]` y hacemos `body.extend([(20, 2), (10, 2)])`, la lista `body` aumenta de tamaño y se convierte en la lista `[(30, 2), (20, 2), (10, 2)]`. De esta forma tenemos en la lista `body` la posición de cada parte del cuerpo de la serpiente. Lo último que tenemos que hacer es devolver esta lista y así completamos la función `_create_body`

>**Nota :pen:** ¿No te llama la atención por qué el nombre de la función `_create_body` comienza con un `_`? En Python existe un convenio a la hora de nombrar los campos y funciones. Si el nombre de un campo o función comienza con un `_` significa que está pensado para ser usado solamente dentro de la clase y que no se debe acceder a ese campo o función desde fuera de la clase. En efecto, solamente queremos crear el cuerpo de la serpiente en un único momento del juego y dentro de esta clase. Esto de poder usar las cosas dentro y fuera de las clases tiene que ver con otro principio fundamental de la POO llamado **encapsulamiento**.

### Funciones `trim`, `_are_opposites` y `change_direction`

Vamos olvidarnos por un momento del orden en el que aparecen las funciones en la clase `Snake` y comentemos ahora estas tres funciones.

La función `trim` se utiliza para acortar el cuerpo de la serpiente. En la versión del juego que estamos haciendo, el usuario nunca verá el cuerpo de la serpiente recortarse. La serpiente solamente crece cuando se come una fruta y mientras no lo haga su longitud se mantiene igual. No obstante, esta función nos será de ayuda más adelante, ya lo descubrirás.

Esta función tiene sólo una línea `self.body.pop()`. Recordemos que `self.body` es la lista de tuplas que representa el cuerpo de la serpiente. La función `pop` es otra de las predefinidas por Python para listas. Esta función elimina el último elemento de la lista. Por tanto, una lista `body = [(30, 2), (20, 2), (10, 2)]` luego de hacer `body.pop()` se convierte en `body = [(30, 2), (20, 2)]`. Con lo que se logra acortar el cuerpo de la serpiente como se quería.

La función `_are_opposites` se utiliza solamente dentro de esta clase para determinar si la nueva dirección en la que el usuario quiere moverse es la opuesta a la que actualmente lleva la serpiente. Por ejemplo, si la serpiente se mueve hacia la derecha y el jugador presiona la flecha izquierda de su teclado, la serpiente debe continuar moviéndose a la derecha porque no puede cambiar su dirección 180 grados en un sólo movimiento.

Esta función recibe dos direcciones: `direction1` y `direction2`. Y determina que no sean totalmente opuestas. Cada sentencia entre paréntesis es una condición. Por ejemplo la primera:

```python
(direction1 == Direction.RIGHT and direction2 == Direction.LEFT)
```

Es verdadera sólo si la primera (`direction1`) es derecha (`Direction.RIGHT`) **y** la segunda (`direction2`) es izquierda (`Direction.LEFT`). Las dos cosas tienen que suceder al mismo tiempo para que la condición sea verdadera.

Todas estas condiciones están unidas por el operador `or`. De la misma forma que en la línea anterior se usa el operador `and` para decir que dos cosas tenían que suceder al mismo tiempo para que la condición se cumpla, el operador `or` hace que la condición completa sea verdadera si **al menos** una de las condiciones que la componen se cumple. De esta forma la función `_are_opposites` nos devuelve verdadero (`True`) si ambas direcciones forman alguna de las posibles combinaciones de direcciones opuestas (derecha - izquierda, izquierda - derecha, arriba - abajo, abajo - arriba).

Luego la función `change_direction` se utiliza para cambiar la dirección actual hacia la que se mueve la serpiente. Esta es la función que se ejecutará cuando el jugador presione las teclas de dirección del teclado. En este caso la función solamente cambia el campo `direction` de la clase si es que la nueva dirección no es opuesta a la que actualmente lleva la serpiente.

### Funciones `_grow` y `move`

Estas son las funciones que nos quedan por analizar. Primero veremos la función `_grow`. Con esta función lo único que hacemos es colocar al inicio de la lista `body` el valor actual de la posición de la cabeza. Para eso usamos la función `insert` predefinida para las listas de Python. Esta función inserta elementos en la lista y recibe dos parámetros: la posición en la que se quiere insertar y el elemento que se quiere insertar. En este caso se quiere insertar la posición de la cabeza justo al inicio, por eso los parámetros son `0` y `self.position` (campo que almacena la posición de la cabeza). Quizás no quede claro cómo esta función realmente hace crecer a la serpiente (*grow* significa crecer en inglés) debido a que parece estar insertando la misma posición en la que estaba la cabeza antes, pero ahora veremos la función `move` y lo comprenderemos mejor.

La función `move` consta de dos partes. La primera en la que solamente modifica la posición de la cabeza, y la segunda donde se llama a la función `_grow`. En la primera parte, dependiendo de la dirección en la que se mueva la serpiente, se modifica la posición en la que se encontrará la cabeza. Por ejemplo, si la serpiente se mueve hacia la derecha, entonces la nueva posición de la cabeza se mantendrá con la misma coordenada vertical y aumentará en 10 la posición horizontal actual.

Notemos que hasta este momento solamente se ha cambiado la posición de la cabeza pero no la lista `body` que contiene todas las posiciones del cuerpo de la serpiente antes de haberse movido. Es por eso que se llama a la función `_grow` que agregará al inicio de la lista `body` la nueva posición de la cabeza. Con esto obtenemos una nueva serpiente, con la cabeza en la posición a la que se quería mover y un poco más larga. Seguramente pensarás que no es exactamente así como funciona el juego, que la serpiente no va por ahí creciendo cada vez que se mueve. Te aseguramos que esto no es lo que va a pasar. Ya verás como poco a poco todas estas piezas se engranan para conseguir el videojuego que buscamos.

Y bueno, creemos que por hoy es suficiente :tada:. Se hacía necesario entender bien todo el código que habíamos hecho ayer y esperamos que haberlo conseguido. Si no es así lee nuevamente esta lección y la anterior para que te enteres de todo. ¡No hay prisa! Tómate el tiempo que necesites. En la siguiente lección te introduciremos en el mundo del *testing*. ¿Cómo hacer programas que comprueben que todo lo que hemos hecho funciona correctamente? Ya lo verás. Esta es una de las habilidades más demandadas en la industria de hoy en día y te lo mostraremos todo de forma práctica mañana.

¡Hasta pronto! :wave:
