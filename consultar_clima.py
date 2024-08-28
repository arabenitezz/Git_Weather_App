import click
import requests
from api_key import API_KEY, API_URL

@click.command()
@click.option("--lugar", help="Nombre de la ciudad o país de la cual se obtendrá la información sobre el clima")
@click.option("--formato", default='json', help="Formato en que se van a recibir los datos")
@click.option("--unidad", default='metric', help="Unidad de medida: 'metric' para Celsius, 'standard' para Kelvin")

def get_weather(lugar, formato, unidad):
    try:
        params = {
            'q': lugar,
            'appid': API_KEY,
            'units': unidad, 
            'lang': 'es'
        }
        response = requests.get(API_URL, params=params)
        response.raise_for_status()

        if formato == 'json':
            weather_data = response.json()
            place_name = weather_data['name']
            temp = weather_data['main']['temp']
            weather_desc = weather_data['weather'][0]['description']

            if unidad == 'metric':
                unit_symbol = '°C'
            else:
                unit_symbol = 'K'

            click.echo(f'El clima en {place_name} es {weather_desc} con una temperatura de {temp}{unit_symbol}.')
        else:
            # Si es XML o HTML, mostrar el contenido directamente
            click.echo(response.text)

    except requests.exceptions.HTTPError as err:
        click.echo(f'Error al obtener los datos: {err}')
    except Exception as e:
        click.echo(f'Ocurrió un error: {e}')

if __name__ == '__main__':
    get_weather()

