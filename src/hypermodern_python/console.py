# src/hypermodern_python/console.py

import click
from datetime import datetime
from . import __version__

@click.command()
@click.version_option(version=__version__)
def main():
	"""The hypermodern Python Project. """
	click.echo(f'Hello world {datetime.now()}')