# Paso a Paso: Día 1

A través de esta serie de tutoriales escritos construiremos juntos el videojuego Snake en Python desde cero. No importa tu nivel de experiencia con Python, te llevaremos paso a paso y te explicaremos con lujo de detalles cada línea de código del proyecto. Si te parece empezamos ya con el primer día de código.

## Instalación de las herramientas necesarias

Lo primero que hay que hacer antes de comenzar cualquier proyecto (no solo de programación) es establecer qué vamos a necesitar y cómo podemos conseguir esas herramientas indispensables para la tarea que queremos hacer. En este caso no necesitamos mucho, solamente lo siguiente:

1. :snake: Una versión de Python 3 instalada
2. :book: El gestor de paquetes de Python `pip`
3. :pen: Un editor para programar en Python con comodidad
4. :video_game: La biblioteca `Pygame` para crear videojuegos en Python

Para los puntos del **1 al 3**, puedes consultar [este artículo de nuestro blog](https://blog.codexlacademy.com/guia-definitiva-para-instalar-python-pip-y-visual-studio-code) donde te explicamos cómo hacer estas instalaciones en los Sistemas Operativos más usados. Así que si no leíste este tutorial o no lo seguiste en su momento, apresúrate y complétalo antes de seguir con este proyecto. No te preocupes, te esperamos a que termines :wink:.

¿Ya estás de vuelta? ¡Genial, continuemos! :rocket:

Para instalar `Pygame` solamente tienes que usar `pip`, no importa el sistema operativo de tu ordenador. Ejecuta el siguiente comando en una terminal.

```bash
pip install pygame
```

>:warning: Es posible que necesites permisos de administrador en algunos casos o que debas usar `pip3` en lugar de `pip`.

Recapitulando, hemos instalado `Python 3`, `pip`, un editor para programar (en nuestro tutorial recomendamos Visual Studio Code) y la biblioteca `Pygame` para crear videojuegos en Python.

¡Listo! Ya tenemos todo lo necesario para comenzar con el proyecto.

## Estructura del proyecto

Entrando en la parte interesante, lo primero que debemos hacer es crear el directorio donde vamos a crear nuestro proyecto. Crea un directorio llamado `snake` en tu ordenador. Una vez creado, agrega dentro otros dos directorios.

* **src:** La abreviatura de **source**, que en inglés quiere decir **fuente**. Usualmente los directorios con nombre **src** contienen el código fuente del proyecto. En nuestro caso, aquí es donde agregaremos todos los archivos Python para implementar nuestro videojuego.
* **tests:** Las pruebas automáticas son un eslabón fundamental en el desarrollo de software en nuestros días. Para nosotros sería un verdadero sacrilegio crear un proyecto sin agregar pruebas. Es por eso que estas pruebas forman parte de este tutorial. Usualmente los archivos que contienen las pruebas de un proyecto se guardan en un directorio llamado `tests` o `test`.

Notarás que en [nuestro repositorio](https://github.com/codexl-academy/snake) agregamos otros directorios y archivos extras pero no los vamos a añadir a esta implementación. Estos archivos extras controlan otras cosas como la licencia para el uso del software, las instrucciones básicas para usar el proyecto, las bibliotecas requeridas y otros relacionados con el control de versiones. Nada de esto interviene directamente en nuestro videojuego así que concentrémonos en nuestra implementación.

### Código fuente

Dentro del directorio `src` vamos a crear a su vez otros directorios y archivos. Serán los siguientes:

* **game_state (directorio):** Aquí pondremos la lógica principal del videojuego. Este será el corazón de nuestro proyecto.
* **model (directorio):** En este agregaremos las *entidades* que intervienen en nuestro juego. En este caso serán **la fruta** y **la serpiente**, nuestros dos personajes principales. Más adelante ahondaremos en este tema de las entidades.
* **renderer (directorio):** Aquí tendremos todo el código necesario para que podamos visualizar nuestro videojuego. Esto es lo que nos permite realmente jugar sin que nuestro proyecto se quede en la teoría.
* **main.py (archivo):** Este es el punto de entrada a nuestro videojuego, lo primero que se ejecuta y arranca todo el andamiaje que vamos a construir juntos paso a paso.

De esta forma dejamos todo organizado para comenzar a programar. En resumen, la estructura del proyecto por ahora debe ser la siguiente:

```plain
snake
|-- src
|---|-- game_state (directorio vacío)
|---|-- model (directorio vacío)
|---|-- renderer (directorio vacío)
|---|-- main.py
|-- tests (directorio vacío)
```

Como habrás notado, tenemos muchos directorios vacíos que ya iremos llenando poco a poco. Dejemos hasta aquí nuestro primer día de proyecto. Durante este día hemos instalado las herramientas necesarias para crear nuestro videojuego **Snake** en Python. Luego hemos creado el directorio del proyecto y los subdirectorios necesarios para trabajar organizadamente. Esta organización es muy común en todo tipo de proyectos en el mundo real. Este tutorial pretende ser un ejemplo de buenas prácticas y organización para iniciarte en el buen camino de la programación :smiley:.

En el siguiente día estaremos conociendo un poco sobre módulos de Python, Programación Orientada a Objetos, creación de clases de Python y las entidades de nuestro juego. Escribiremos nuestras primeras líneas de código y estaremos más cerca de haber creado nuestro proyecto.

¡Sigue aprendiendo con nosotros!
