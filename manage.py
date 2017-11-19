import click
from werkzeug.serving import run_simple
from project.web import application
from project import settings

@click.group()
def cli():
    pass

@cli.command()
def runserver():
    "Starts the web server"
    run_simple('0.0.0.0', settings.PORT, application, use_reloader=settings.DEBUG, use_debugger=settings.DEBUG)

if __name__ == '__main__':
    cli()
