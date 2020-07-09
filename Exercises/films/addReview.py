import click

@click.command()
@click.option("--film-name", help="Film Title")
@click.option("--stars", help="Rating out of 5 stars")

def hello(film, stars):
    click.echo(% film % stars)


hello()
