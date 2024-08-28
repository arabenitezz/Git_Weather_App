import click
import requests
from api_key import API_KEY, API_URL

@click.command()
@click.option("--place", prompt="Nombre de la ciudad o pais", help="Nombre de la ciudad o pais de la cual se obtendrá la información sobre el clima")
@click.option("--format", prompt="Elija un formato", type=click.Choice(['json', 'xml', 'html']), help="Es el formato en que se va a recibir los datos")

def get_weather (place, format):
    try:
        params = {
            'q': place,
            'appid': API_KEY,
            'units': 'metric',
            'lang': 'es'
        }

    except requests.exceptions.HTTPError as err:
        click.echo(f'Error al obtener los datos: {err}')
    except Exception as e:
        click.echo(f'Ocurrió un error: {e}')
