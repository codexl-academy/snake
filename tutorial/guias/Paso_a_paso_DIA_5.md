# Paso a Paso: Día 5

Hoy aprenderemos a usar Pygame para crear la interfaz de usuario de nuestro juego. La interfaz de usuario de un software es lo que ven y con lo que interactúan los usuarios de ese software. En nuestro caso, la interfaz será una pantalla que mostrará los detalles del juego, la serpiente moviéndose, la fruta, los puntos que hemos alcanzado. Además esta interfaz debe mostrar cómo cambia el estado del juego bajo la interacción de los jugadores. Para el videojuego Snake esto quiere decir que se debe ver cómo la serpiente cambia de dirección cuando el usuario usa las flechas de su teclado. Hasta ahora todo ha sido muy abstracto, hemos hablado de posiciones, coordenadas, listas, etc. En el día de hoy exploraremos un nuevo mundo.

Así que vamos a comenzar directamente escribiendo código. :nerd_face:

## Archivo `renderer.py`

Todo el control de la interfaz de usuario lo llevaremos a cabo en el archivo `renderer.py`. Copia el siguiente contenido en dicho archivo.

Archivo **src/renderer/renderer.py**:

```python
"""Module that handles the rendering of the components and states of the game.

As of now, it handles the rendering of:

    * The Score.
    * The Game Over screen.
    * The Current State of the Game.
"""


from enum import Enum
from typing import List, Tuple

import pygame


class Color(Enum):
    """Enum representing the colors to be used in the game.

    Values are represented as RGB vectors.
    """

    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0)
    GREEN = pygame.Color(0, 255, 0)


class Renderer:
    """Class that handles the rendering of the components and states of the Game."""

    @staticmethod
    def render_score(score: int, game_window, color: Color, font: str, font_size: int):
        """Renders the score on the top left corner of the screen.

        Args:
            score (int): The score of the Game.
            game_window (pygame.display): The window where the Game is being displayed.
            color (Color): Color of the font.
            font (str): Style of the font.
            font_size (int): Size of the font.
        """
        score_font = pygame.font.SysFont(font, font_size)
        score_surface = score_font.render(f"Score : {score}", True, color)
        score_rect = score_surface.get_rect()
        game_window.blit(score_surface, score_rect)

    @staticmethod
    def render_game_over(
        score: int,
        game_window,
        window_x: int,
        window_y: int,
        color: Color,
        font: str,
        font_size: int,
    ):
        """Renders the `Game Over` state.

        Red-colored sign with the score in the middle of the screen.

        Args:
            score (int): The score of the Game.
            game_window (pygame.display): The window where the Game is being displayed.
            window_x (int): Dimension `x` of the window.
            window_y (int): Dimension `y` of the window.
            color (Color): Color of the font.
            font (str): Style of the font.
            font_size (int): Size of the font.
        """
        my_font = pygame.font.SysFont(font, font_size)
        game_over_surface = my_font.render(f"Your Score is : {score}", True, color)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x / 2, window_y / 4)
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()

    @staticmethod
    def render_game_state(
        snake_body: List[Tuple[int, int]],
        fruit_position: Tuple[int, int],
        game_window,
        snake_color: Color,
        fruit_color: Color,
        window_color: Color,
    ):
        """Renders the state of the Game.

        Handles the rendering of the Snake and the Fruit.

        Args:
            snake_body (List[Tuple[int, int]]): List of positions of the snake's body.
            fruit_position (Tuple[int, int]): Position of the fruit.
            game_window (pygame.display): The window where the Game is being displayed.
            snake_color (Color): Color of the snake.
            fruit_color (Color): Color of the fruit.
            window_color (Color): Color of the window.
        """
        game_window.fill(window_color)
        for pos in snake_body:
            pygame.draw.rect(
                game_window, snake_color, pygame.Rect(pos[0], pos[1], 10, 10)
            )
        pygame.draw.rect(
            game_window,
            fruit_color,
            pygame.Rect(fruit_position[0], fruit_position[1], 10, 10),
        )

```

Aunque parezca mucho código no te preocupes, entenderlo va a ser mucho más fácil de lo que piensas. En primer lugar leamos el comentario inicial. Nos dice que en este módulo es donde se representa en pantalla el juego. Actualmente se está representando el *score* del jugador, la pantalla de *game over* y el estado del juego como tal. Entonces vamos a ver cómo lo hacemos.

Primeramente importamos algunas clases que ya conocemos como *Enum* y los tipos *List* y *Tuple*. Además importamos la biblioteca Pygame que contiene muchas funcionalidades que nos facilitarán representar nuestro juego en pantalla.

Luego definimos un tipo enumerado `Color` para representar los colores que vamos a usar en nuestro juego. En este caso usaremos el blanco (WHITE), negro (BLACK), rojo (RED) y verde (GREEN). A cada uno de estos colores le asignamos el código que nos da la clase `Color` de Pygame. Esta clase recibe los colores en formato RGB. Si quieres aprender los detalles sobre esta codificación de color consulta [este enlace](https://es.wikipedia.org/wiki/RGB).

Luego definimos la clase `Renderer`, que es la que se va a encargar de representar nuestro juego. Todas las funciones de la clase `Renderer` comienzan con `@staticmethod`. Este es un decorador incluido en Python para definir que una función puede ser llamada sin crear un objeto de la clase. Esto es algo que veremos en práctica el próximo día. Solamente para dar una explicación básica, recordemos que en el día anterior hicimos pruebas para la clase `Snake`. En esas pruebas creamos un objeto `snake` a partir de la clase haciendo `self.snake = Snake(position=(50, 50), direction=Direction.RIGHT, size=4)`. Luego podíamos llamar a las funciones de este objeto haciendo, por ejemplo, `self.snake.move()`. O sea, tuvimos que crear un objeto y luego llamar a la función de ese objeto. Cuando dentro de una clase una función se declara como `@staticmethod` no es necesario crear un objeto para usar esa función, sino que podemos simplemente hacer `Renderer.render_score(...)`.

Como ya dijimos, vamos a ver esto en práctica en la próxima guía. Por ahora volvamos a nuestra clase `Renderer`.

### Función `render_score`

La primera función es `render_score`, que se encarga de representar nuestra puntuación durante el juego. Esta clase recibe varios parámetros:

1. `score`: De tipo entero. Representa la cantidad de puntos obtenida.
2. `game_window`: No especificamos tipo. Esto será un objeto que nos da Pygame que contiene la ventana de nuestro juego.
3. `color`: De tipo `Color`. El color con que dibujaremos el score.
4. `font`: De tipo string. La fuente con la que dibujaremos el score.
5. `font_size`: De tipo entero. El tamaño de letra con la que se representa el score.

El comentario nos dice que el score lo representaremos en la esquina superior izquierda y nos describe cada argumento de la función.

Luego creamos un objeto `Font` usando el módulo `font` de Pygame. La clase `SysFont` de este módulo recibe la fuente y el tamaño de fuente y devuelve un objeto de tipo `Font`. Luego este objeto que se almacena en la variable `score_font`, lo usamos para crear la superficie del texto que vamos a escribir. El método `render` definido en la clase `Font` recibe el texto a representar, un parámetro de tipo *bool* que determina si queremos que el texto tenga bordes suaves y el color del texto. El llamado a esta función nos devuelve un objeto de tipo `Surface` que representa una región en nuestra pantalla que contiene el texto especificado.

>**Nota :pen:** En la línea anterior usamos lo que se conoce como *string interpolation*. Cuando anteponemos la letra `f` antes de un string en Python, podemos incluir dentro del string código Python. En este caso queremos escribir *Score: x* donde *x* es el número que representa el score. Como dicho score está en la variable `score`, podemos escribir el string como: `f"Score: {score}"`. Al anteponer una `f` y encerrar la variable score entre llaves, obtenemos el resultado deseado.

>**Nota :pen:** Toda la documentación sobre Pygame la puedes encontrar [aqui](https://www.pygame.org/docs/) (en inglés).

Luego tenemos que obtener el rectángulo que contiene a la región definida anteriormente. Esto lo hacemos con la función `get_rect` del objeto `Surface`. Por último usamos el método `blit` definido en el objeto `game_window` que pinta la superficie dentro del rectángulo.

### Función `render_game_over`

La siguiente función es la que representará la pantalla de *game over*. Esta es la pantalla que nos sale cuando perdemos en el juego :cry:. Como esta función recibe muchos parámetros, hemos decidido escribir un parámetro por línea. De otra forma acabaríamos con una línea tan extensa que no cabría en nuestra pantalla y tendríamos que usar la barra de scroll horizontal para leerla completamente. Los parámetros `score`, `game_window`, `color`, `font` y `font_size` representan lo mismo que en la función anterior. El parámetro `window_x` representa el ancho de la ventana del juego y el parámetro `window_y` la altura.

Al terminar el juego, saldrá en la pantalla un cartel rojo con la puntuación que hemos obtenido. Las primeras tres líneas de código de esta función deben resultar familiares luego de analizar la función anterior. Estamos creando la fuente, la superficie y el rectángulo donde se dibujará nuestro cartel. Lo próximo que hacemos es establecer la posición del cartel. Vamos a hacer que el centro del borde superior se ubique a la mitad del ancho de la pantalla y a un cuarto de la altura del borde superior de la pantalla. Esto se hace modificando el campo `midtop` de nuestro rectángulo:

```python
game_over_rect.midtop = (window_x / 2, window_y / 4)
```

Le asignamos una tupla cuyo primer elemento es la coordenada horizontal y el segundo la coordenada vertical. El campo `midtop` contiene la posición del centro del borde superior del rectángulo. Al ser la primera coordenada la mitad del ancho y la segunda un cuarto del alto, ubicamos el rectángulo en la posición deseada.

Por último usamos la función `blit` como en el caso anterior y luego la función `flip` del módulo `display` que provoca que lo que estaba anteriormente en pantalla se borre y en su lugar se represente lo que acabamos de dibujar.

### Función `render_game_state`

Hasta ahora hemos visto cómo mostrar aspectos del juego, pero es en esta función donde mostramos el juego en sí mismo. Representamos la serpiente y la fruta en su estado actual. La lista de parámetros en este caso cambia un poco:

1. `snake_body`: Lista de tuplas con la posición de cada parte del cuerpo de la serpiente en el momento actual.
2. `fruit_position`: Posición actual de la fruta.
3. `game_window`: Exactamente igual que en las funciones anteriores.
4. `snake_color`: Color de la serpiente.
5. `fruit_color`: Color de la fruta.
6. `window_color`: Color de la ventana donde se desarrolla el juego.

Con todos estos parámetros vamos a representar nuestro juego. Lo primero es rellenar toda la ventana con el color deseado. Esto lo hacemos con la función `fill` de `game_window`. Luego pintamos cada parte del cuerpo de la serpiente:

```python
for pos in snake_body:
    pygame.draw.rect(
        game_window, snake_color, pygame.Rect(pos[0], pos[1], 10, 10)
    )
```

Por cada posición en la lista que representa el cuerpo de la serpiente, usamos el campo `draw` de Pygame para dibujar. Específicamente vamos a representar cada parte del cuerpo como un pequeño cuadrado de 10 píxeles de lado. Para ello usamos la función `rect` para pintar rectángulos, le pasamos la ventana del juego, el color, y un objeto de tipo `Rect` que está definido en Pygame. A este último objeto le debemos pasar la posición de la esquina superior izquierda, el ancho y el largo del rectángulo. De esta forma queda pintado nuestro pequeño cuadradito con el color deseado :snake:.

```python
pygame.draw.rect(
    game_window,
    fruit_color,
    pygame.Rect(fruit_position[0], fruit_position[1], 10, 10),
)
```

Por último, y de manera análoga, pintamos un pequeño cuadrado para representar la fruta. La única diferencia es que este cuadrado tendrá el color definido para la fruta.

¡Y ya está! Hemos creado todo lo necesario para que quienes jueguen puedan visualizar todo lo que pasa y divertirse (que al final es lo que importa). En la siguiente guía agregaremos la última pieza de este rompecabezas. ¡Cada vez el final está más cerca!
