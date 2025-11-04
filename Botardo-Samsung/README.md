# Botardo-Samsung
Hola!

Este es el repositorio del grupo "Los Copilotos IA"

Nuestro proyecto se trta de una chatbot de Telegram que tiene como objetivo ser una guía para educadores.


## Cómo levantar el bot:
Primeramente se debe levantar un entorno virtual en la PC para evitar generar conflictos, si está usando Windows puede hacerlo con los siguientes comandos:
1. python -m venv entorno-virtual
2. entorno-virtual\Scripts\activate.bat


En caso de estar unsando MacOS o alguna distribución de Linux, los scripts son los siguientes:
1. python -m venv entorno-virtual
2. source entorno-virtual/bin/activate

Una vez el entorno virtual, debe instalar el archivo requirements con el siguiente comando: pip install -r requirements.txt
En caso de necesitar actualizar algo, deberá correr el comando npip install --upgrade <nombre de la herramienta> ej pip install --upgrade pip 
Una vez la terminal le arroje el mensaje "Telegram está esperando un mensaje..." debe buscar el bot en telegram.

## Interacción en Telegram
En la barra de búsqueda de la aplicación, debe colocar el sihuiente usuario: @Los_Copilotos_bot y presionar el botón /start.
Luego de poresionado el botón, el bot le dará un mensaje introductorio, de aquí en adelante usted podrá hacerle preguntas del tipo ¿Quién te creó?, datos educativos, o incluso pedir que analice el sentimiento de una frase, imágen o audio.
El análisis de sentimiento está integrado por defecto para mayo comodidad del usuario.


