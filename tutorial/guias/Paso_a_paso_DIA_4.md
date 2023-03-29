# Paso a Paso: Día 4

¡Hola de nuevo! Hoy vamos a ver todo lo necesario para escribir pruebas automatizadas en Python. Esto de pruebas automatizadas no es más que escribir programas que verifican el funcionamiento de otros programas. Parece complicado pero no lo es tanto. Específicamente vamos a aprender un poco sobre la importancia de las pruebas automatizadas y por qué son tan demandadas en la industria hoy en día. Luego implementaremos pruebas para el código que ya hemos escrito y comprendido y, como siempre, te dejaremos nuestras **Notas :pen:** con consejos y curiosidades del mundo Python :nerd_face:. Si te parece bien...

¡Comencemos! :rocket:

## Importancia de las pruebas automatizadas

Los errores en el software (como sucede también en la vida) causan menos daño si se descubren rápido. Si justo en el momento que escribimos una función nos damos cuenta que de un error, lo podemos arreglar en el momento sin que provoque el menor problema. Si, por el contrario, no nos damos cuenta de ese error en ese momento y al finalizar nuestro proyecto vemos que algo no funciona bien (la serpiente no se mueve o la puntuación no cambia correctamente por ejemplo), entonces sí que estamos metidos en un buen lío.

En ese momento hay que empezar a investigar la causa del error, emplear horas y horas de tiempo para descubrir dónde está el problema y quizás, para ese entonces, el proyecto es tan grande que al arreglar algo rompamos otra cosa sin darnos cuenta. En fin, todo un caos. Y eso por no mencionar lo que puede pasar si el error lo descubre un cliente que usa nuestro software, ahí nos arriesgamos a perder muchos clientes, credibilidad y dinero. Por lo tanto, en la industria del software de hoy en día existen dos únicos caminos: no cometer errores o descubrir los errores lo antes posible.

Como te estarás imaginando, el primero de los caminos es imposible de seguir :clown:. Todos, absolutamente todos, comentemos errores. La única manera de no cometer errores programando es no programar nada. Por tanto, en realidad tenemos una única alternativa: descubrir los errores lo antes posible. Pero, ¿de qué forma podemos descubrir estos errores tan rápidamente?

Ir revisando línea a línea nuestro propio código es una inversión de tiempo inasumible. Además provocaría que el trabajo de desarrollar software fuera muuuuyyy aburrido. Hay una alternativa mucho más práctica y divertida: ¡escribir código que revise nuestro propio código! :smiley:. Quizás estés pensando ahora mismo que esto es más de lo mismo, ¿qué pasa si también tengo errores en el código que escribo para descubrir errores? ¡Ufff, qué complicado! Pero descuida, hay un detalle que nos va a salvar.

Los *tests*, que son estos programas para descubrir errores, deben ser programas muy cortos, concisos y extremadamente simples. Estas son condiciones indispensables. De forma que nos aseguremos que sea demasiado improbable cometer un error que no podamos descubrir pronto.

>**Nota :pen:** Hoy en día está muy de moda la metodología conocida como *Test Driven Development (TDD)*. Esta defiende que el desarrollo de software debe ir guiado por las pruebas automatizadas. Por tanto, en TDD, primero escribimos estas pruebas aunque no hayamos hecho ningún código y luego implementamos las funcionalidades hasta el punto donde todos los tests nos dan resultado positivo. TDD no es objetivo de esta guía pero más adelante estaremos hablando de ello en [nuestro blog](https://blog.codexlacademy.com). 

En este proyecto, aunque es un material introductorio, hemos querido incluir los tests como una parte indispensable. Hoy en día carece de sentido embarcarse a hacer cualquier software sin incluir pruebas automatizadas y, por tanto, creemos que carece de sentido que un curso de programación no hable de ellas. Pero no nos quedaremos solamente en las palabras. ¡Vamos a hacer nuestros primeros tests! :rocket:

## Implementando tests para las clases `Fruit` y `Snake`

Vamos a utilizar las herramientas que nos brinda Python para realizar pruebas automatizadas. En futuros tutoriales incluiremos usos más avanzados de la biblioteca `pytest`. Por ahora vamos a centrarnos en lo principal: escribir pruebas para nuestro código.

En nuestro proyecto, dentro del directorio `tests`, vamos a agregar los archivos `test_fruit.py` y `test_snake.py`. Como debes estar pensando, en el archivo `test_fruit.py` incluiremos las pruebas para la clase `Fruit` mientras que en el `test_snake.py` probaremos la clase `Snake`. Veamos cómo se hace.

### Clase `Fruit`

Copia el siguiente código en el archivo `test_fruit.py`:

Archivo **tests/test_fruit.py**:

```python
from unittest import TestCase

from src.model.fruit import Fruit


class TestFruit(TestCase):
    def setUp(self):
        self.fruit = Fruit((10, 10))

    def test_created_as_dataclass(self):
        self.assertEqual(self.fruit.position, (10, 10))

```

Analicemos el código anterior línea a línea. En la primera línea estamos importantdo la clase `TestCase` del módulo `unittest` que viene incluido en Python. Esta clase contiene lo necesario para crear pruebas automatizadas. Lo que haremos será heredar de ella y crear nuestras propias pruebas.

Luego importamos la clase que queremos probar. En este caso es la clase `Fruit` que recordemos que se encuentra en **src/model/fruit**.

Ahora creamos nuestra clase `TestFruit` que, como dijimos, hereda de `TestCase`. En esta clase definiremos las funciones necesarias para probar nuestra clase `Fruit`. En primer lugar definimos la función `setUp`. Esta función se encarga de preparar todo lo necesario para ejecutar nuestras pruebas, en este caso, todo lo que necesitamos es crear un campo `fruit` al que le asignaremos un objeto de tipo `Fruit`. Nota como para crear un objeto a partir de una clase debemos escribir el nombre de la clase y, entre paréntesis pasar los parámetros que recibe dicha clase. En este caso, la clase `Fruit` solamente recibe una tupla de dos enteros que representa la posición de la fruta. Para nuestra prueba le hemos pasado la posición `(10, 10)`. Notemos que el nombre de la función `setUp` no sigue las reglas del **snake_casing**. Esto es debido a que esta función tiene que llamarse justo así, `setUp`, sin cambiar ni una letra. Así es como está definida en la clase padre y si la nombramos de otra manera simplemente no se ejecutará en el momento de hacer las pruebas.

Lo siguiente es crear las funciones que contienen las pruebas. Para la clase `Fruit` no hay mucho que probar, solamente verificaremos que la posición de la fruta sea realmente la que le pasamos: `(10, 10)`. Para ello creamos la función `test_created_as_dataclass` que no recibe parámetros. En este caso sí podemos usar el **snake_casing** porque lo único que necesitamos es que el nombre de nuestra función comience con la palabra **test**. Lo que tenemos que comprobar es que el campo `position` de `fruit` sea igual a `(10, 10)`. Esto lo hacemos con la función `assertEqual` que ya está definida en la clase padre `TestCase`. De esta forma, si sucede que la igualdad no se cumple, al ejecutar nuestro test obtendremos un error. ¡Probemos si todo funciona! :fear:

Dentro del directorio `fruit` abre una terminal y ejecuta el siguiente comando:

```bash
pytest
```

Debes obtener algo similar a esto:

```bash
/snake$ pytest
======================= test session starts ========================================
platform linux -- Python 3.10.6, pytest-7.2.2, pluggy-1.0.0
rootdir: /media/jj/2C3E97D93E979A82/Storage/personal-projects/codexl/snake/tutorial/DIA 4/snake
plugins: web3-5.30.0, anyio-3.6.1
collected 1 item

tests/test_fruit.py .                                                           [100%]

======================== 1 passed in 0.07s ==========================================
```

Nos va a interesar sobre todo la información a partir de la línea que empieza con *collected*. Lo que vemos en esa línea es cuántos tests se van a ejecutar, en este caso solamente 1. Luego tenemos un listado con todos los archivos que contienen tests y un punto (`.`) o una `F` para cada test en ese archivo. El punto significa que el test devolvió un resultado correcto y la `F` que el test falló.

Finalmente la última línea nos da un resumen de cuántos tests pasaron, cuántos fallaron y qué tiempo tomó ejecutarlos todos. En nuestro caso, nuestro único test fue exitoso :smiley:.

A modo de ejemplo, agreguemos a nuestra clase un test que sabemos que va a fallar:

```python
from unittest import TestCase

from src.model.fruit import Fruit


class TestFruit(TestCase):
    def setUp(self):
        self.fruit = Fruit((10, 10))

    def test_created_as_dataclass(self):
        self.assertEqual(self.fruit.position, (10, 10))
    
    def test_fail(self):
        self.assertEqual(1, 2)

```

Si volvemos a ejecutar el comando `pytest`, obtenemos la siguiente salida:

```bash
========================= test session starts ==========================================
platform linux -- Python 3.10.6, pytest-7.2.2, pluggy-1.0.0
rootdir: /media/jj/2C3E97D93E979A82/Storage/personal-projects/codexl/snake/tutorial/DIA 4/snake
plugins: web3-5.30.0, anyio-3.6.1
collected 2 items                                                                                                                        

tests/test_fruit.py .F                 [100%]

========================== FAILURES =====================================================
______________________ TestFruit.test_fail ______________________________________________

self = <tests.test_fruit.TestFruit testMethod=test_fail>

    def test_fail(self):
>       self.assertEqual(1, 2)
E       AssertionError: 1 != 2

tests/test_fruit.py:14: AssertionError
========================== short test summary info =======================================
FAILED tests/test_fruit.py::TestFruit::test_fail - AssertionError: 1 != 2
========================== 1 failed, 1 passed in 0.28s ===================================
```

A partir de la línea que comienza con `collected` vemos que ahora se detectaron dos tests. En la siguiente línea tenemos archivo que contiene los tests seguido de un punto y una `F`. Ya sabíamos que íbamos a tener un fallo porque nuestro test verifica que 1 sea igual a 2. Las siguientes líneas nos dan detalles de este fallo, en qué parte de nuestro código ocurre el error y qué tipo de error es. Luego tenemos un resumen corto del fallo y finalmente tenemos 1 test exitoso, 1 fallido y todo se ejecutó en 0.28 segundos. Antes de continuar, asegúrate de borrar la función `test_fail` para no volver a tener tests fallidos.

### Clase `Snake`

Ahora agreguemos las pruebas para la clase `Snake`:

Archivo **tests/test_snake.py**:

```python
from unittest import TestCase

from src.model.snake import Direction, Snake


class TestSnake(TestCase):
    def setUp(self):
        self.snake = Snake(position=(50, 50), direction=Direction.RIGHT, size=4)

    def test_create_body(self):
        self.assertEqual(self.snake.body, [(50, 50), (40, 50), (30, 50), (20, 50)])

    def test_move(self):
        self.snake.move()
        self.assertEqual(self.snake.position, (60, 50))
        self.assertEqual(
            self.snake.body, [(60, 50), (50, 50), (40, 50), (30, 50), (20, 50)]
        )

    def test_trim(self):
        self.snake.trim()
        self.assertEqual(self.snake.body, [(50, 50), (40, 50), (30, 50)])

    def test_change_direction(self):
        self.snake.change_direction(Direction.UP)
        self.assertEqual(self.snake.direction, Direction.UP)

    def test_change_direction_opposite(self):
        self.snake.change_direction(Direction.LEFT)
        self.assertEqual(self.snake.direction, Direction.RIGHT)

```

De la misma forma que en el caso anterior. Creamos una clase que herede de `TestCase` y una función `setUp` para inicializar la clase `Snake`. En este caso vamos a crear una serpiente que tenga la cabeza en la posición `(50, 50)`, que se esté moviendo hacia la derecha y con un tamaño igual a 4.

Vamos a agregar 5 pruebas en esta clase:

1. La función `test_create_body` prueba que nuestra serpiente se haya creado de la manera correcta. En este caso, dad la posición inicial y el tamaño de la serpiente esperamos que el cuerpo de la serpiente sea `[(50, 50), (40, 50), (30, 50), (20, 50)]`.
2. La función `test_move` prueba que la función `move` de la clase `Snake` funcione como se espera. Debido a que la serpiente se mueve hacia la derecha, se espera que después de ejecutar la función `move`, la nueva posición de la cabeza sea `(60, 50)` y el cuerpo sea `[(60, 50), (50, 50), (40, 50), (30, 50), (20, 50)]`.
3. La función `test_trim` prueba que el tamaño de la serpiente disminuya de manera correcta. Luego de ejecutarse, el cuerpo de la serpiente debe ser `[(50, 50), (40, 50), (30, 50)]`. Debemos tener en cuenta que para cada test la serpiente que se utiliza como entrada es la que se crea en el método `setUp` y no la que resulta de ejecutar el test anterior.
4. La función `test_change_directio` verifica que la dirección se cambie de manera correcta. En este caso se intenta cambiar la dirección hacia arriba y se espera que, en efecto, la nueva dirección de la serpiente pase a ser hacia arriba.
5. Por último la función `test_change_direction_opposite` verifica que la dirección de la serpiente no cambie cuando se intenta moverla en la dirección opuesta. Como inicialmente la serpiente se mueve hacia la derecha, cambiar la posición hacia la izquierda no debiera tener ningún efecto y la serpiente debiera mantener su rumbo hacia la derecha.

>:warning: Ten siempre en cuenta que el método `setUp` se ejecuta antes de cada test por lo que cada test usa la misma serpiente como entrada en este caso.

Si volvemos a ejecutar `pytest` obtenemos una salida como esta:

```bash
================================= test session starts =======================================
platform linux -- Python 3.10.6, pytest-7.2.2, pluggy-1.0.0
rootdir: /media/jj/2C3E97D93E979A82/Storage/personal-projects/codexl/snake/tutorial/DIA 4/snake
plugins: web3-5.30.0, anyio-3.6.1
collected 6 items                                                                                                                        

tests/test_fruit.py .                                                                     [ 16%]
tests/test_snake.py .....                                                                 [100%]

================================== 6 passed in 0.09s ==========================================
```

En este caso tenemos dos archivos, uno con un solo test y otro con cinco pruebas. Todas las pruebas fueron exitosas y se ejecutaron en 0.09 segundos.

Con esto hemos logrado verificar automáticamente que nuestro código funciona como esperamos. En el día de hoy hemos aprendido cuán importantes son las pruebas automatizadas en la industria del software. Además implementamos nuestras primeras pruebas automatizadas para asegurarnos de que todo el código que hemos escrito hasta ahora funciona correctamente.

Nos vamos acercando poco a poco al final de nuestro proyecto pero aún quedan muchas cosas divertidas por hacer. En el siguiente día vamos a adentrarnos en el uso de Pygame y programaremos toda la interfaz de usuario de nuestro juego. Como siempre, siéntete libre de releer las partes que no te hayan quedado claras, reproduce lo que hemos hecho hoy y experimenta por tu cuenta. No hay mejor manera de aprender.

¡Nos vemos pronto! :wave:
