Aquí tienes un archivo `README.md` claro y detallado para tu proyecto:  

```markdown
# CLI para Consulta de Clima  

Este proyecto es una herramienta de línea de comandos (CLI) que permite consultar el clima actual de cualquier ciudad o país utilizando la API de OpenWeather. Es personalizable en formato de salida y unidad de medida.  

## Requisitos  

- Python 3.7 o superior  
- Clave de API de OpenWeather (colócala en el archivo `api_key.py`)  
- Librerías externas:  
  - `click`: para la creación de la CLI.  
  - `requests`: para realizar solicitudes HTTP.  

## Instalación  

1. Clona este repositorio en tu máquina local:  
   ```bash
   git clone <url-del-repositorio>
   cd <nombre-del-repositorio>
   ```  

2. Instala las dependencias necesarias:  
   ```bash
   pip install click requests
   ```  

3. Configura tu archivo `api_key.py` con las siguientes variables:  
   ```python
   API_KEY = 'tu_api_key_de_openweather'
   API_URL = 'https://api.openweathermap.org/data/2.5/weather'
   ```  

## Uso  

Ejecuta el script desde la terminal con los siguientes parámetros:  

```bash
python <nombre_del_archivo>.py --lugar <ciudad/país> --formato <formato> --unidad <unidad>
```  

### Parámetros  

- `--lugar`: Especifica el nombre de la ciudad o país para consultar el clima (obligatorio).  
- `--formato`: Define el formato de salida. Valores posibles:  
  - `json` (por defecto)  
  - `csv`  
  - `texto`  
- `--unidad`: Selecciona la unidad de temperatura. Valores posibles:  
  - `metric` para Celsius (por defecto)  
  - `standard` para Kelvin  

### Ejemplos  

1. Obtener el clima en formato JSON para Asunción:  
   ```bash
   python <nombre_del_archivo>.py --lugar "Asunción"
   ```  

2. Obtener el clima en formato CSV para Madrid con unidades Kelvin:  
   ```bash
   python <nombre_del_archivo>.py --lugar "Madrid" --formato csv --unidad standard
   ```  

3. Obtener el clima en texto para Nueva York:  
   ```bash
   python <nombre_del_archivo>.py --lugar "Nueva York" --formato texto
   ```  

## Manejo de errores  

- Si el lugar no es válido o la solicitud falla, se mostrará un mensaje de error claro.  
- Si ocurre cualquier otro problema, el programa también lo indicará.  

## Contribuciones  

Si deseas contribuir al proyecto, siéntete libre de enviar pull requests o abrir issues.  

---
Proyecto para Penguin Academy 🐧🚀
