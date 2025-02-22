# src/hypermodern-python/wikipedia.py
import click
import requests


API_URL = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


def random_page(language="en"):
    """Let’s move the Wikipedia client to a separate module."""
    url = API_URL.format(language=language)

    try:
        with requests.get(url) as response:
            response.raise_for_status()
            return response.json()
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message)
