import click # --> CLI
import requests # --> solicitudes HTTP 
import csv # --> manejar csv
import io
from api_key import API_KEY, API_URL


@click.command()
@click.option("--lugar", help="Nombre de la ciudad o país de la cual se obtendrá la información sobre el clima")
@click.option("--formato", default='json', help="Formato en que se van a recibir los datos: 'json' para json 'csv' para csv 'texto' para texto")
@click.option("--unidad", default='metric', help="Unidad de medida: 'metric' para Celsius, 'standard' para Kelvin")

def get_weather(lugar, formato, unidad):
    try:
        # parametros para la solicitud a la API
        params = {
            'q': lugar,
            'appid': API_KEY,
            'units': unidad, 
            'lang': 'es'
        }
        # solicitud GET
        response = requests.get(API_URL, params=params)
        # Verifica si la solicitud fue exitosa; si no, lanza una excepción.
        response.raise_for_status()

        weather_data = response.json()
        place_name = weather_data['name']
        temp = weather_data['main']['temp']
        weather_desc = weather_data['weather'][0]['description']

        if unidad == 'metric':
            unit_symbol = '°C'
        else:
            unit_symbol = 'K'

        if formato == 'json':
            click.echo(f'El clima en {place_name} es {weather_desc} con una temperatura de {temp}{unit_symbol}.')
        elif formato == 'csv':
            output = io.StringIO() # Crea un objeto StringIO para almacenar datos CSV en memoria.
            writer = csv.writer(output) # Crea un escritor CSV.
            writer.writerow(['Lugar', 'Descripción', 'Temperatura', 'Unidad'])
            writer.writerow([place_name, weather_desc, temp, unit_symbol])
            click.echo(output.getvalue())
        elif formato == 'texto':
            click.echo(f'Lugar: {place_name}\nDescripción: {weather_desc}\nTemperatura: {temp} {unit_symbol}')
    # Captura y muestra errores específicos de solicitudes HTTP
    except requests.exceptions.HTTPError as err:
        click.echo(f'Error al obtener los datos: {err}')
    # Captura y muestra cualquier otro error general
    except Exception as e:
        click.echo(f'Ocurrió un error: {e}')

if __name__ == '__main__':
    get_weather()

