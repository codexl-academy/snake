# Paso a Paso: Día 2

Comenzamos el día dos de creación de nuestro videojuego Snake :snake:. Hoy escribiremos nuestras primeras líneas de código Python y, mejor aún, aprenderemos un concepto fundamental en la programación de hoy en día: la **Programación Orientada a Objetos (POO)**. Así que comencemos por ahí.

## Programación Orientada a Objetos

Los lenguajes de programación que usamos comúnmente son muy genéricos, es decir, están hechos para que puedas programar cualquier programa. Si queremos programar un software para llevar las finanzas de una empresa podemos usar Python, pero si queremos crear un sitio de citas online... ¡también podemos usar Python! Este lenguaje solamente tiene un pequeño conjunto de palabras reservadas y reglas concretas que definen qué es un programa válido en Python. Con esos pequeños bloques podemos construir casi cualquier cosa.

Esto es una gran fortaleza de los lenguajes de programación que tenemos hoy en día pero también nos puede traer problemas. En el mundo de las finanzas, por ejemplo, trabajamos con *pagos*, *cobros*, *deudas*, *inventarios*, etc. Por otra parte, en sitios de citas online trabajaríamos con *perfiles de usuarios*, *gustos personales*, *compatibilidad entre personas*, etc. Parecen dos universos totalmente distintos y, sin embargo ambos los programamos en ¡el mismo lenguaje! :exploding_head:.

Pero ¿cómo distinguir estos dos universos tan diferentes? ¿Cómo puedo **hablar los idiomas** de cada uno si ambos los hago en el mismo lenguaje de programación?

La respuesta a estas preguntas las tiene la Programación Orientada a Objetos (POO). Este es un concepto más antiguo que el propio Python y defiende el principio de que el diseño de un software debe girar en torno a los objetos o entidades del problema que estamos resolviendo y no centrarse en las funciones y la lógica :nerd_face:. Cuando creamos un software de finanzas cumpliendo con el modelo de POO, expresamos directamente en el código que trabajamos con *pagos*, *deudas* e *inventarios*; mientras que si creamos un sitio de citas vamos a usar en nuestro código *perfiles*, *compatibilidades*, *gustos*, etc.

En nuestro videojuego vamos a usar la POO también, por lo que estaremos trabajando con *serpientes* y *frutas*, además de otros objetos importantes que intervienen en nuestro universo. Pero... ¿cómo podemos incluir estos objetos en nuestros programas? :monocle_face:.

## Clases en Python

Un concepto central en la POO es el de **clase**. Las clases son una plantilla para crear objetos. Por ejemplo, si decimos que la clase **Persona** tiene un nombre, una edad y un estado civil, entonces todas las personas de nuestro software tendrán estas (y solo estas) características. Veamos cómo crear clases en Python y póngamonos manos a la obra :rocket:.

### Primeras clases en Python

Los objetos de nuestro proyecto los definiremos dentro del directorio `src/model`. Allí crearemos dos archivos: el archivo `fruit.py` y el `snake.py`. En estos definiremos las clases para representar a la fruta :strawberry: y a la serpiente :snake: respectivamente.

>**Nota:** A pesar de que este es un curso en español, en nuestro código usaremos el idioma inglés para nombrar clases, funciones, variables, etc. El inglés es el idioma que todos los desarrolladores usamos para programar y poder entender el código de cada uno sin importar nuestro origen. Es muy recomendable que comiences a aprender inglés en caso de que aún no lo domines. En este proyecto te ayudaremos también con eso :wink:

