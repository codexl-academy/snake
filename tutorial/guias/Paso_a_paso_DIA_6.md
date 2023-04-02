# Paso a Paso: Día 6

Este es probablemente el día más importante y extenso de todos. No queremos desalentarte con esto, todo lo contrario, queremos que sepas que aprenderás un montón hoy sobre todo porque verás mucho código nuevo, y lo reproducirás. Como ya sabes, en CodeXL creemos firmemente que esta es la mejor manera de aprender.

Así que si te parece... ¡comencemos! :rocket:

## Uniendo las piezas: los módulos de Python

En el día 4, cuando escribimos tests para nuestro código, incluimos un archivo `__init__.py` para poder importar las clases dentro del directorio model. Un proyecto de Python por lo general se compone de varios **módulos**. En nuestro videojuego, los directorios **model**, **game_state** y **renderer** son módulos. Un módulo puede ser visto como una parte de nuestro proyecto que tiene una funcionalidad específica y que a menudo puede ser incluso usado en otros proyectos.

Por ejemplo, nuestro módulo **model**, puede ser usado en otra versión del videojuego **Snake** ya que solamente contiene las definiciones de lo que son una serpiente y una fruta en este videojuego.

La forma de declarar que un directorio es un módulo es agregando un archivo `__init__.py` en él. Así que lo primero que haremos con los módulos de nuestro proyecto será agregar este archivo en cada uno.

>**Nota :pen:** Un módulo puede contener archivos **.py** y también otros módulos. Por ejemplo, pudiéramos decir que el directorio **src** es también un módulo que contiene los submódulos **game_state**, **model** y **renderer**.

En un proyecto Python, los módulos se relacionan entre sí para dar vida al software que se quiere crear, como en un automóvil donde los sistemas eléctrico, mecánico e hidráulico se interconectan para llevarnos con seguridad de un lado a otro de la ciudad. Hoy aprenderemos a interconectar los módulos de nuestro proyecto para posteriormente dar vida a nuestro videojuego.

## El módulo `game_state`

En este módulo vamos a usar las entidades creadas `model` y la clase `renderer` para completar la lógica de nuestro juego. Vamos echar un primer vistazo al código. Agrega el archivo **game.py** al directorio **game_state** y pega en él el siguiente código.

Archivo **src/game_state/game.py**:

```python
"""Module that handles the Game entities.

As of now, it consist of a `Game` class handling the
main cycle and events of the game.
"""


import random
import sys
import time

import pygame

from model.fruit import Fruit
from model.snake import Direction, Snake
from renderer.render import Color, Renderer


class Game:
    """Class representing the Game entity."""

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.snake_speed = 15
        self.window_x = 720
        self.window_y = 480
        self.game_window = pygame.display.set_mode((self.window_x, self.window_y))
        self.fps = pygame.time.Clock()

        self.snake = Snake(position=(100, 50), direction=Direction.RIGHT, size=4)
        self.fruit = self._generate_fruit()
        self.score = 0
        self.paused = False

    def _touch_boundaries(self) -> bool:
        """Checks whether the snake's head is touching the
        boundaries of the board.

        Returns:
            bool: True in case the snake's head is touching the boundaries, False otherwise.
        """
        return (
            self.snake.position[0] < 0
            or self.snake.position[0] > self.window_x - 10
            or self.snake.position[1] < 0
            or self.snake.position[1] > self.window_y - 10
        )

    def _touch_body(self) -> bool:
        """Checks wheter the snake's head is touching its body.

        Returns:
            bool: True in case the snake's head is touching its body, False otherwise.
        """
        return any(self.snake.position == block for block in self.snake.body[1:])

    def game_over(self):
        """Checks for the conditions of Game Over.

        The conditions are:
            * Snake's head touches boundaries.
            * Snake's head touches body.

        Returns:
            bool: True if any condition is met, False otherwise.
        """
        return self._touch_boundaries() or self._touch_body()

    def get_user_input(self):
        """Listens to KEYDOWN events to recognize
        direction changes.

        If no KEYDOWN event occurs, the direction doesn't change.

        Returns:
            Direction: The new direction of the snake.
        """
        change_to = self.snake.direction
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = Direction.UP
                if event.key == pygame.K_DOWN:
                    change_to = Direction.DOWN
                if event.key == pygame.K_LEFT:
                    change_to = Direction.LEFT
                if event.key == pygame.K_RIGHT:
                    change_to = Direction.RIGHT
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        return change_to

    def _generate_fruit(self) -> Fruit:
        """Generate new fruit."""
        return Fruit(
            position=(
                random.randrange(1, (self.window_x // 10)) * 10,
                random.randrange(1, (self.window_y // 10)) * 10,
            )
        )

    def _increase_game_speed(self):
        self.snake_speed += 1

    def run(self):
        """Runs the main cycle of the Game."""
        while True:

            if self.paused:
                continue
            
            new_direction = self.get_user_input()

            self.snake.change_direction(new_direction)
            self.snake.move()

            if self.snake.position == self.fruit.position:
                self.score += 10
                self.fruit = self._generate_fruit()
                self._increase_game_speed()
            else:
                self.snake.trim()

            Renderer.render_game_state(
                self.snake.body,
                self.fruit.position,
                self.game_window,
                Color.GREEN.value,
                Color.WHITE.value,
                Color.BLACK.value,
            )

            if self.game_over():
                Renderer.render_game_over(
                    self.score,
                    self.game_window,
                    self.window_x,
                    self.window_y,
                    Color.RED.value,
                    "times new roman",
                    50,
                )
                time.sleep(2)
                pygame.quit()
                sys.exit()

            Renderer.render_score(
                self.score, self.game_window, Color.WHITE.value, "times new roman", 20
            )
            pygame.display.update()
            self.fps.tick(self.snake_speed)
```

La clase `Game` anterior representa todo nuestro juego, con todas sus piezas usadas de manera que todo cobra sentido. Pero antes vamos a fijarnos en todo lo que estamos importando en las primeras líneas. Primeramente importamos los módulos `random`, `sys` y `time` que ya vienen definidos por defecto en Python. El módulo `random` nos permite generar números aleatorios (*random* significa aleatorio en inglés). Con el módulo `sys` podremos interactuar con el sistema de nuestro ordenador. Además, como podrás imaginarte, el módulo `time` nos deja manipular el tiempo dentro de nuestro programa.

Luego importamos `pygame` que contiene todas las funcionalidades necesarias para nuestro videojuego. Por último importamos las clases que ya hemos creado en nuestro proyecto: del archivo **fruit.py** dentro del módulo **model** importamos la clase `Fruit`. De manera análoga importamos las clases `Snake`, `Direction`, `Renderer` y `Color`. Ahora veamos cómo engranar todo en la clase `Game`.

## La clase `Game`

Lo primero, como siempre, es el método `__init__`. En este caso no recibiremos ningún parámetro. En la primera línea iniciamos el motor gráfico de Pygame, que es el que nos muestra todo en pantalla. Luego con `pygame.display.set_caption("Snake")` estamos creando el título de nuestro juego, el texto **Snake** se verá en el borde superior de la ventana del juego. A continuación damos valores a la velocidad de juego, el ancho y la altura de la ventana de juego. El campo `game_window` se crea haciendo `self.game_window = pygame.display.set_mode((self.window_x, self.window_y))`. Este representa la ventana donde se desarrolla el juego y es el que tanto se usa en las funciones que ya vimos el día anterior en la clase `Renderer`. Además creamos el campo `fps` (fraps per second) o sea, la cantidad de veces que se dibuja nuestro juego en la pantalla por segundo. Este valor se toma directamente del reloj de Pygame haciendo `self.fps = pygame.time.Clock()`.

Lo próximo que hacemos es crear nuestra serpiente en la posición `(100, 50)`, dirigiéndose hacia la derecha y con un tamaño de `4`. También generamos la primera fruta con la función `_generate_fruit` que veremos en la siguiente sección. Por último, ponemos el `score` a 0 y el campo `paused` - que controla si el juego está pausado o no - a falso (`False`).

### Funciones `_touch_boundaries`, `_touch_body`, `_increase_game_speed` y `_generate_fruit`

Estas funciones son usadas solamente dentro de esta clase `Game` y contienen código útil para la lógica del juego. La función `_touch_boundaries`, por ejemplo, nos dice si la serpiente ha tocado uno de los bordes de la pantalla.

```python
def _touch_boundaries(self) -> bool:
    """Checks whether the snake's head is touching the
    boundaries of the board.

    Returns:
        bool: True in case the snake's head is touching the boundaries, False otherwise.
    """
    return (
        self.snake.position[0] < 0
        or self.snake.position[0] > self.window_x - 10
        or self.snake.position[1] < 0
        or self.snake.position[1] > self.window_y - 10
    )
```

Esta función no recibe parámetros y devuelve un valor booleano (`True` - verdadero -  o `False` - falso). La serpiente toca un borde cuando la posición horizontal o vertical de su cabeza está en uno de esos bordes. En nuestro caso, la posición de la cabeza se almacena en el campo `position` del objeto `snake`. Recordemos que este campo es una tupla y que la posición horizontal está en la posición 0 de la tupla mientras que la posición vertical está en la posición 1.

El borde izquierdo de la pantalla se identifica con el número 0 y el borde derecho estará justo 10 píxeles antes del valor del ancho de la pantalla. De la misma forma, el borde inferior de la pantalla se identifica con 0 y el superior justo 10 píxeles antes del valor de la altura de la pantalla. La serpiente, por tanto, tocará un borde cuando su posición horizontal o vertical sea menor que 0 o mayor que los valores para los bordes derecho y superior respectivamente. Esto lo expresamos en la función con cuatro condiciones unidas por el operador `or` que indica que toda la expresión será verdadera si al menos una de las condiciones es verdadera.

>**Nota :pen:** Luego de la palabra reservada **return** hemos usado paréntesis para poder escribir una condición por línea. De esta forma no tenemos que escribir una línea muy extensa y nuestro código se puede leer más fácilmente.

La siguiente función es `_touch_body`, que verifica si la serpiente ha tocado su propio cuerpo:

```python
def _touch_body(self) -> bool:
    """Checks wheter the snake's head is touching its body.

    Returns:
        bool: True in case the snake's head is touching its body, False otherwise.
    """
    return any(self.snake.position == block for block in self.snake.body[1:])
```

Hay varios detalles en esta función. Analicemos primero lo que tenemos dentro de los paréntesis en la sentencia **return**:

```python
self.snake.position == block for block in self.snake.body[1:]
```

Como ya sabemos, esto es una forma de crear una colección ordenada de elementos. En este caso, cada elemento será `True` o `False`. Será verdadero (`True`) si la posición de la cabeza es igual a la tupla `block` (ya veremos de dónde sale `block`), y falso (`False`) en otro caso. La tupla `block` no es más que cada elemento del cuerpo de la serpiente (campo `body` del objeto `snake`). No obstante, recordemos que el primer elemento del cuerpo de la serpiente es la cabeza pero no nos interesa comprobar que la cabeza haya chocado consigo misma, por tanto solamente consideramos los elementos de esta lista a partir del segundo. Esto lo logramos con `self.snake.body[1:]`.

Por último usamos la función `any` de Python. Esta función devuelve `True` si **al menos uno de los elementos** de una colección es `True` y falso en otro caso. Por tanto lo que estamos diciendo es que la serpiente ha chocado con su propio cuerpo si la posición de su cabeza es igual a la posición de alguna de las partes de su cuerpo. ¿Tiene sentido no? :nerd_face:

>**Nota :pen:** El operador `==` se usa para saber si dos elementos son iguales. No se debe confundir con el operador `=` que se usa para asignar un valor a una variable. Por ejemplo, `self.snake.position == block` nos devuelve `True` si se cumple la igualdad pero `self.snake.position = block` le asigna la tupla `block` al campo `position`.

La función `_increase_game_speed` es bastante simple. Lo único que hace es incrementar por 1 la velocidad del juego. En nuestro juego incrementaremos la velocidad cada vez que la serpiente come una fruta.

>**Nota :pen:** El operador `+=` se usa para escribir líneas más cortas. Hubiese sido equivalente escribir: `self.snake_speed = self.snake_speed + 1`.

```python
def _generate_fruit(self) -> Fruit:
    """Generate new fruit."""
    return Fruit(
        position=(
            random.randrange(1, (self.window_x // 10)) * 10,
            random.randrange(1, (self.window_y // 10)) * 10,
        )
    )
```

Finalmente, la función `_generate_fruit`, genera una nueva fruta en una posición aleatoria. Esto lo logramos usando el módulo `random`, específicamente la función `randrange` de este módulo. Lo que queremos es generar una posición aleatoria para pasársela a la clase `Fruit`. También debemos recordar que nuestra fruta se representa con un cuadrado de 10 píxeles de lado. Por tanto debemos ubicarla de forma que quepa dentro de nuestra ventana de juego sabiendo el área que va a ocupar. La función `randrange` nos devuelve un número entero aleatorio que se encuentra en el rango definido por los parámetros que le pasamos. O sea `random.randrange(1, 10)` nos da un número aleatorio entre uno y diez. En este caso queremos un número que sea mayor que 0 y que sea menor que el ancho de la pantalla divido entre 10 para la posción horizontal (para la vertical es lo mismo pero en lugar del ancho es el alto lo que dividimos entre 10). Luego este número lo multiplicamos por 10 para obtener la coordenada donde representaremos la fruta. Con esto logramos que la coordenada de nuestra fruta se encuentre en números que son múltiplos de 10 y que no se salga de la pantalla de juego.

El operador `//` representa la **división entera** en Python. Cuando usamos `//` en lugar de `/` estamos diciendo que no nos interesa la parte fraccionaria del resultado de la división, sólo la parte entera. Por ejemplo, `5 / 2` nos devuelve `2.5` mientras que `5 // 2` nos devuelve `2`.

### Funciones `game_over`, `get_user_input` y `run`

Con estas funciones terminamos de construir nuestro juego. La primera de todas es `game_over` que es bastante simple. Nuestro juego acaba si la serpiente toca un borde o si toca su propio cuerpo. Si cualesquiera de estas condiciones sucede, entonces habremos perdido :cry:.

La función `get_user_input` nos permite cambiar el estado del juego de acuerdo con las teclas que presione el jugador. Veamos más detalles:

```python
def get_user_input(self):
    """Listens to KEYDOWN events to recognize
    direction changes.

    If no KEYDOWN event occurs, the direction doesn't change.

    Returns:
        Direction: The new direction of the snake.
    """
    change_to = self.snake.direction
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = Direction.UP
            if event.key == pygame.K_DOWN:
                change_to = Direction.DOWN
            if event.key == pygame.K_LEFT:
                change_to = Direction.LEFT
            if event.key == pygame.K_RIGHT:
                change_to = Direction.RIGHT
            if event.key == pygame.K_SPACE:
                self.paused = not self.paused
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
    return change_to
```

Aquí devolveremos el resultado de la interacción del usuario con el juego. Este resultado se almacenará en la variable `change_to` cuando implique un cambio de dirección. Inicialmente `change_to` contendrá la dirección actual de nuestra serpiente.

Luego iteramos por todos los eventos que ha capturado Pygame. Durante la ejecución de nuestro juego, Pygame va almacenando todas las acciones que hacemos: teclas que presionamos, movimientos del mouse, clicks, etc. Estos eventos los podemos leer en nuestros programas y decidir qué hacer cuando ocurren. En nuestro caso, solamente nos interesará cuando el usuario presione las teclas de dirección para cambiar el movimiento de la serpiente, la tecla espaciadora para pausar el juego, o la tecla <kb>q</kb> para quitar el juego. El resto de eventos serán ignorados.

Los eventos, como ya vimos, pueden ser de varios tipos. El único tipo que nos interesa es el `KEYDOWN` que representa que se presionó una tecla. A partir de ahí podemos saber qué tecla se presionó a partir del campo `key` que poseen todos los eventos de tipo `KEYDOWN`. Pygame nos ofrece variables para referirnos a las teclas con nombres sugerentes. Por ejemplo, la flecha de dirección hacia arriba es `K_UP`. Si la tecla presionada representa una dirección, almacenamos la dirección correspondiente en la variable `change_to`. Si la tecla es la barra espaciadora, le asignamos al campo `paused` el valor contrario al que tenía antes (si era `True` lo cambiamos a `False` y viceversa), de esta forma pausamos y reanudamos el juego. Por último, si se presiona la tecla <kb>q</kb> cerramos el juego usando `pygame.quit()` y `sys.exit()`. Al final devolvemos la variable `change_to` con la dirección actualizada.

>**Nota :pen:** El operador `not` actúa sobre valores booleanos y devuelve el valor contrario. Si se aplica sobre algo que es `True` devolverá `False` y viceversa.

Y para cerrar tenemos la función más importante. La que finalmente reúne todos los elementos de nuestro juego y los hace interactuar de manera que todo cobre sentido. La función `run`:

```python
def run(self):
    """Runs the main cycle of the Game."""
    while True:

        if self.paused:
            continue
        
        new_direction = self.get_user_input()

        self.snake.change_direction(new_direction)
        self.snake.move()

        if self.snake.position == self.fruit.position:
            self.score += 10
            self.fruit = self._generate_fruit()
            self._increase_game_speed()
        else:
            self.snake.trim()

        Renderer.render_game_state(
            self.snake.body,
            self.fruit.position,
            self.game_window,
            Color.GREEN.value,
            Color.WHITE.value,
            Color.BLACK.value,
        )

        if self.game_over():
            Renderer.render_game_over(
                self.score,
                self.game_window,
                self.window_x,
                self.window_y,
                Color.RED.value,
                "times new roman",
                50,
            )
            time.sleep(2)
            pygame.quit()
            sys.exit()

        Renderer.render_score(
            self.score, self.game_window, Color.WHITE.value, "times new roman", 20
        )
        pygame.display.update()
        self.fps.tick(self.snake_speed)
```

Todo nuestro juego es un gran ciclo que no acaba hasta que el jugador pierde o cierra voluntariamente el juego. Es por eso que nuestra función es un gran ciclo `while` que no tiene condición de parada (`while True:`). Así, nuestro juego se mantedrá ejecutándose mientras las condiciones para terminarlo no se cumplan.

En primer lugar, verificamos si el juego está pausado, en cuyo caso no hacemos más nada en esta iteración y dejamos que el ciclo `while` se vuelva a ejecutar. Luego actualizamos la dirección de la serpiente. Si no se modifica con las flechas del teclado, entonces se mantiene la misma dirección. Con esta dirección movemos a la serpiente usando las funciones `change_position` y `move` de la clase `Snake`. Recordemos que la función `move` provoca que la serpiente crezca.

Lo siguiente es verificar si la serpiente comió una fruta. Esto sucede cuando la posición de la fruta y la de la cabeza de la serpiente coinciden. En este caso, aumentamos el score en 10, generamos una nueva fruta e incrementamos la velocidad del juego. Como ya la función `move` hizo crecer a la serpiente, no nos tenemos que preocupar por ello.

En caso de que no se haya comido una fruta, entonces tenemos que revertir el crecimiento de la serpiente y para eso usamos la función `trim`.

Luego usamos la función `render_game_sate` de la clase `Renderer` para representar todos los elementos del juego. Después toca verificar si hemos perdido, o sea, si la función `game_over` nos devuelve `True` en las condiciones actuales del juego. En caso afirmativo, procedemos a dibujar la pantalla de *game over*. Usamos la fuente *time new roman* con tamaño 50. Dejamos esta pantalla durante 2 segundos con `time.sleep(2)` y luego cerramos el juego.

Si no hemos perdido aún, representamos nuestro score en pantalla. Usaremos para ello la fuente *times new roman* pero esta vez con tamaño 20.

Usamos la función `pygame.display.update()` para que nuestra pantalla se actualice con la situación actual del juego y adaptamos los *fraps per second* a la velocidad del juego con `self.fps.tick(self.snake_speed)`.

¡Y con esto hemos terminado la lógica de nuestro juego! :grin:

Y nuestro tutorial también está próximo al final. Solamente resta un día. En este último día vamos a ver cómo jugar nuestro juego (para eso hemos llegado hasta aquí) y luego vamos a ver nuevamente todo lo que hemos construido juntos, las cosas buenas y también los errores que podemos haber cometido. Estaremos también reflexionando sobre cómo mejorar todo esto, qué más podemos agregar a nuestro videojuego y te contaremos cómo puedes seguir aprendiendo más sobre Python y crear un mejor videojuego junto a nosotros.

¡Ya casi llegas a la meta! :checkered_flag:
