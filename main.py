import time

import click
import click_spinner


@click.command()
def cli():
    click.echo("it works")
    with click_spinner.spinner():
        click.echo("it works2")
        time.sleep(1)
        click.echo("it works3")
