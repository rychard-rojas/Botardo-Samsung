# Botardo-Samsung
Hola!

Este es el repositorio del grupo "Los Copilotos IA"

Nuestro proyecto se trata de una chatbot de Telegram que tiene como objetivo ser una guía para educadores.

## Cómo levantar el bot:
Primeramente se debe levantar un entorno virtual en la PC para evitar generar conflictos, si está usando Windows puede hacerlo con los siguientes comandos:

python -m venv entorno-virtual
entorno-virtual\Scripts\activate.bat
En caso de estar usando MacOS o alguna distribución de Linux, los scripts son los siguientes:

python -m venv entorno-virtual
source entorno-virtual/bin/activate
Una vez el entorno virtual, debe instalar el archivo requirements con el siguiente comando: pip install -r requirements.txt En caso de necesitar actualizar algo, deberá correr el comando pip install --upgrade ej pip install --upgrade pip Una vez la terminal le arroje el mensaje "Telegram está esperando un mensaje..." debe buscar el bot en telegram.

## Interacción en Telegram
En la barra de búsqueda de la aplicación, debe colocar el siguiente usuario: @Los_Copilotos_bot y presionar el botón /start. Luego de presionado el botón, el bot le dará un mensaje introductorio, de aquí en adelante usted podrá hacerle preguntas del tipo ¿Quién te creó?, datos educativos, o incluso pedir que analice el sentimiento de una frase, imágen o audio. El análisis de sentimiento está integrado por defecto para mayo comodidad del usuario.

## Funcionalidades 

* El bot busca cumplir la funcion de un apoyo para maestros principiantes dandoles respues de como actuar en determinadas situaciones que se pueden dar en un aula como por ejemplo: "¿Cómo reacciono ante un estudiante que llega tarde e interrumpe la clase?" el bot brindara como respuesta la mejor forma de actuar ante esa situacion. 

**Tambien es capaz de detectar las emociones**

* Mediante imagen (jpg), detectando las expresiones faciales y dando una sugerencia de que se expresa en esa imagen. Por ejemplo ante una foto propia sonriendo se espera que responda  un mensaje como "Me alegra ver que tienes un momento de felicidad en tu vida, ¡es algo precioso! Recuerda que la felicidad no es solo un sentimiento, sino tambien un reflejo de la belleza y la bondad que hay en ti. ¿Te gustaria compartir que te hace sentir tan feliz?".
* El bot permite tambien la grabacion de audio y analiza el tono, el ritmo y la emocion vocal y da una respuesta analita de las emociones detectadas y una respuesta empatica, por ejemplo ante un audio indicando dificultad para estudiar el bot responderia: "Me alegra escucharte y saber que estas sintiendo alegria a pesar de sentirte un poco cansado. Eso es un gran signo de que estas encontrando formas de mantener una actitud positiva incluso en momentos dificiles. ¿Te gustaria hablar un poco mas de que te esta haciendo sentir optimista?".
* Mediante texto tambien se puede escribir un mensaje y el bot analizara la emocion y el sentimiento de ese texto devolviendo un feedback emocional adaptado. Por ejemplo demostrando que estas angustiado el bot respondera "Entiendo que estás pasando por un momento muy difícil y que esto te está molestando mucho. Es normal sentirse así, y no estás solo en eso. ¿Quieres hablar un poco sobre qué pasa, y cómo te sientes al respecto?"


