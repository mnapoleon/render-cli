import click
from rich.table import Table
from rich.console import Console
from renderctl.render_services import fetch_services, retrieve_env_from_render

from . import __version__


@click.group()
def cli():
    pass


@cli.command('list')
@click.option('--table', is_flag=True)
def list_services(table):
    data = fetch_services()
    if table:
        table = Table(title="Services")
        table.add_column("Name")
        table.add_column("Service Id")
        table.add_column("URL")
        for service in data:
            svc = service['service']
            s_name = svc['name']
            s_id = svc['id']
            s_url = svc['serviceDetails']['url']
            table.add_row(s_name, s_id, s_url)
        console = Console()
        console.print(table)
    else:
        click.echo(data)


@cli.command()
@click.option('-sn', '--service-name', type=str, help='Render service name')
def env(service_name):
    click.echo(retrieve_env_from_render(service_name))


@cli.command()
@click.option('-sn', '--service-name', type=str, help='Deploys named service')
def deploy(service_name):
    click.echo(deploy(service_name))


@cli.command()
@click.version_option(version=__version__)
def main():
    click.echo("renderctl")


if __name__ == '__main__':
    main()
