# CLI de Información Climática

Este proyecto es una herramienta de línea de comandos (CLI) que permite obtener información sobre el clima de un lugar específico usando la API de Open Weather. El usuario puede elegir el formato en que se recibe la información y la unidad de medida para la temperatura.

## Requisitos

- Python 3.7 o superior
- `requests`
- `click`

## Instalación

1. Clona este repositorio o descarga los archivos necesarios.

2. Instala las dependencias necesarias ejecutando:

   ```bash
   pip install -r requirements.txt

3. Crea un archivo api_key.py en la raíz del proyecto y define las siguientes variables:

API_KEY = 'tu_api_key_aqui'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'

Reemplaza 'tu_api_key_aqui' con tu clave de API de Open Weather.

## Uso
Ejecuta el script desde la línea de comandos proporcionando los argumentos necesarios:

python nombre_del_script.py --lugar "Ciudad" --formato "formato" --unidad "unidad"

## Opciones
--lugar: Nombre de la ciudad o país de la cual se obtendrá la información sobre el clima.
--formato: Formato en el que se recibirán los datos. Las opciones disponibles son:
json (por defecto): Muestra la información en formato JSON.
csv: Muestra la información en formato CSV.
texto: Muestra la información en un formato de texto legible.
--unidad: Unidad de medida de la temperatura. Las opciones son:
metric (por defecto): Temperatura en grados Celsius.
standard: Temperatura en Kelvin.

## Manejo de Errores
El script maneja errores comunes como:

Fallos en la conexión con la API.
Respuestas no exitosas de la API.
Errores inesperados.
En caso de errores, se mostrará un mensaje descriptivo en la línea de comandos.

## Licencia
Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.





