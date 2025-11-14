# EduMood Bot 🤖💬 - Por "Los Copilotos IA"

 <!-- Reemplaza esto con una URL de un banner si tienes uno -->

Hola y bienvenido al repositorio de **EduMood Bot**, un proyecto creado por el grupo "Los Copilotos IA" como parte del Samsung Innovation Campus.

Nuestra misión es crear un asistente inteligente y empático para Telegram, diseñado para ser una herramienta de apoyo para educadores. El bot ofrece respuestas a situaciones comunes en el aula y, al mismo tiempo, es capaz de analizar y responder de forma constructiva a las emociones expresadas en texto, voz e imágenes.

---

## ✨ Funcionalidades Clave

*   **🧠 Base de Conocimiento para Educadores:** Hazle preguntas sobre cómo manejar situaciones específicas en clase (ej. "¿Qué hago si un alumno interrumpe?") y obtén consejos prácticos y pedagógicos.
*   **📝 Análisis de Sentimiento en Texto:** Escribe una frase o un párrafo y el bot analizará el sentimiento, devolviendo un feedback empático generado por IA para validar tus emociones.
*   **🎤 Análisis de Notas de Voz:** Envía una nota de voz, el bot la transcribirá a texto, analizará el sentimiento y te dará una respuesta constructiva.
*   **🖼️ Análisis de Contenido en Imágenes:** Comparte una imagen y el bot identificará los elementos principales, generando un feedback basado en el contenido visual.
*   **🤖 Búsqueda Semántica Inteligente:** No necesitas escribir la pregunta exacta. El bot entiende la *intención* detrás de tus preguntas para encontrar la respuesta más relevante en su base de datos.

---

## 🚀 Puesta en Marcha - Guía de Instalación "Para Dummies"

Sigue estos pasos cuidadosamente. Si es tu primera vez, ¡no te preocupes! Están diseñados para guiarte en todo el proceso.

### Paso 0: Pre-requisitos (Lo que necesitas tener instalado en tu PC)

Antes de empezar, asegúrate de tener estas herramientas. Son estándar para el desarrollo en Python.

1.  **Git:** Para clonar el repositorio. [Descargar Git](https://git-scm.com/downloads).
2.  **Python (versión 3.10 o superior):** [Descargar Python](https://www.python.org/downloads/). Durante la instalación en Windows, **asegúrate de marcar la casilla que dice "Add Python to PATH"**.
3.  **Dependencias del Sistema para Audio:** El bot necesita estas herramientas para procesar audio. Abre tu terminal o línea de comandos y ejecuta el comando correspondiente a tu sistema:
    *   **macOS (con [Homebrew](https://brew.sh/)):**
        ```bash
        brew install portaudio ffmpeg
        ```
    *   **Linux (Debian/Ubuntu):**
        ```bash
        sudo apt-get update && sudo apt-get install portaudio19-dev ffmpeg
        ```
    *   **Windows:** Este paso es más complejo. Se recomienda instalar `ffmpeg` a través de [Chocolatey](https://chocolatey.org/) o descargarlo manualmente y añadirlo al PATH del sistema.

### Paso 1: Clonar el Repositorio

Abre tu terminal, navega a la carpeta donde quieras guardar el proyecto y ejecuta:
```bash
git clone https://github.com/rychard-rojas/Botardo-Samsung.git
cd Botardo-Samsung
```

### Paso 2: Crear y Activar un Entorno Virtual

Esto crea un espacio de trabajo aislado para nuestro bot, evitando conflictos con otros proyectos.

*   **En macOS o Linux:**
    ```bash
    # 1. Crear el entorno
    python3 -m venv testing

    # 2. Activarlo (¡Debes hacer esto cada vez que abras una nueva terminal para trabajar!)
    source testing/bin/activate
    ```

*   **En Windows:**
    ```bash
    # 1. Crear el entorno
    python -m venv testing

    # 2. Activarlo (¡Debes hacer esto cada vez que abras una nueva terminal para trabajar!)
    .\testing\Scripts\activate
    ```
    *Tu terminal ahora debería mostrar `(testing)` al principio de la línea.*

### Paso 3: Instalar las Dependencias de Python

Con el entorno activado, instala todas las librerías necesarias con un solo comando:
```bash
pip install -r requirements.txt
```

### Paso 4: Configurar las API Keys (¡Paso Crítico!)

El bot necesita "llaves" secretas para conectarse a Telegram y a la IA de Groq.

1.  Busca el archivo llamado `.env.example` en la carpeta.
2.  Crea una copia de este archivo y renómbrala a `.env`.
3.  Abre el nuevo archivo `.env` y rellena los valores:

    ```
    # .env
    TELEGRAM_TOKEN="AQUI_VA_TU_TOKEN_DE_TELEGRAM"
    GROQ_API_KEY="AQUI_VA_TU_CLAVE_DE_GROQ"
    ```

*   **Para obtener el `TELEGRAM_TOKEN`:**
    1.  Habla con el bot oficial de Telegram llamado [@BotFather](https://t.me/BotFather).
    2.  Escribe el comando `/newbot` y sigue sus instrucciones.
    3.  Al final, te dará un token. ¡Cópialo y pégalo aquí!

*   **Para obtener la `GROQ_API_KEY`:**
    1.  Crea una cuenta gratuita en [GroqCloud](https://console.groq.com/keys).
    2.  Ve a la sección "API Keys" y crea una nueva clave.
    3.  Copia la clave (empieza con `gsk_...`) y pégala aquí.

### Paso 5: ¡Ejecutar el Bot!

Con todo configurado y el entorno virtual activado, ejecuta el siguiente comando:
```bash
python main.py
```
Si todo ha ido bien, tu terminal mostrará mensajes indicando que los modelos se han cargado y que el bot está iniciado.

---

## 🤖 Cómo Interactuar con el Bot

1.  Abre tu aplicación de Telegram.
2.  Busca el nombre de usuario de tu bot (el que creaste con BotFather).
3.  Inicia una conversación y presiona el botón `/start`.

### Ejemplos de Uso:

*   **Hacer una pregunta de educador:**
    > *Tú:* `¿Cómo reacciono ante un estudiante que llega tarde e interrumpe la clase?`
    > *Bot:* `Hacer un gesto discreto para que tome asiento sin interrumpir más. Abordar al estudiante brevemente y en privado después de la clase para conocer el motivo y recordarle la importancia de la puntualidad.`

*   **Analizar un sentimiento:**
    > *Tú:* `Estoy agotado, la semana ha sido muy difícil.`
    > *Bot (respuesta empática generada por IA):* `Suena a que ha sido una semana realmente dura, y es completamente normal sentirse así de cansado. Recuerda que está bien tomarse un momento para respirar y recargar energías.`

*   **Enviar una Nota de Voz:**
    > *(Grabas un audio diciendo "Estoy feliz porque terminé mi proyecto")*
    > *Bot (transcribe y analiza):* `Texto transcrito: "Estoy feliz porque terminé mi proyecto". ¡Qué gran noticia! Terminar un proyecto importante es una sensación increíble. ¡Celebra este logro, te lo mereces!`

*   **Enviar una Imagen:**
    > *(Envías una foto de un perro jugando en un parque)*
    > *Bot (analiza el contenido):* `He detectado: "perro, césped, pelota". Parece una escena muy alegre. Los momentos de juego y naturaleza son geniales para levantar el ánimo. ¡Gracias por compartirlo!`

---

### 🧠 La Base de Conocimiento (`dataset.json`)

El archivo `dataset.json` es el cerebro del bot para respuestas directas. Contiene dos tipos de información:
1.  **Preguntas sobre el propio bot:** Su nombre, creadores, hobbies, etc.
2.  **Preguntas y respuestas para educadores:** Un conjunto de situaciones comunes en el aula con estrategias recomendadas.

Gracias a la búsqueda semántica, no tienes que hacer la pregunta exacta para obtener la respuesta correcta.

---

### 🔧 Solución de Problemas Comunes

*   **Error `ModuleNotFoundError`:** Lo más probable es que **no hayas activado el entorno virtual**. Detén el programa (`Ctrl+C`), ejecuta `source testing/bin/activate` (o el comando de Windows) y vuelve a intentarlo.
*   **Error `Invalid API Key` de Groq:** La clave en tu archivo `.env` es incorrecta. Vuelve a generarla en la página de Groq, cópiala con cuidado y reinicia el bot.
*   **Los audios dan error:** Asegúrate de haber instalado `ffmpeg` correctamente en tu sistema (Paso 0).

---

Creado con ❤️ por **Los Copilotos IA**:
*   Ricardo, Rojas
*   Rios, Marcos Nahuel
*   Aguilera, Martin Ezequiel