import json

import click
from rich.table import Table
from rich.console import Console
from renderctl.render_services import fetch_services, retrieve_env_from_render, deploy_service

#from . import __version__
__version__  = "3.4"

@click.group()
def cli():
    pass


@cli.command('list')
@click.option('--table', is_flag=True)
def list_services(table):
    data = fetch_services()
    if table:
        tb = Table(title="Services")
        tb.add_column("Name")
        tb.add_column("Service Id")
        tb.add_column("URL")
        for service in data:
            svc = service['service']
            s_name = svc['name']
            s_id = svc['id']
            s_url = svc['serviceDetails']['url']
            tb.add_row(s_name, s_id, s_url)
        console = Console()
        console.print(tb)
    else:
        click.echo(json.dumps(data, indent=4))


@cli.command('set-env')
@click.option('-f', '--file', type=str, help='File to load env vars from')
def set_env(file):
    env_vars = {}
    with open(file) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            else:
                var, value = parse_env_file(line)
                env_vars[var] = value
    for k, v in env_vars.items():
        click.echo(f"{k} = {v}")


@cli.command('list-env')
@click.option('-sn', '--service-name', type=str, help='Render service name')
@click.option('--table', is_flag=True)
def list_env(service_name, table):
    data = retrieve_env_from_render(service_name)
    if table:
        tb = Table(title="Env Vars")
        tb.add_column("Name")
        tb.add_column("Value")
        for item in data:
            name = item['envVar']['key']
            value = item['envVar']['value']
            tb.add_row(name, value)
        console = Console()
        console.print(tb)
    else:
        click.echo(json.dumps(data, indent=4))


@cli.command()
@click.option('-sn', '--service-name', type=str, help='Deploys named service')
def deploy(service_name):
    result = deploy_service(service_name)
    click.echo(json.dumps(result, indent=4))


@cli.command()
@click.version_option(version=__version__)
def main():
    click.echo("renderctl")


def parse_env_file(input):
    var, value = input.split('=')
    var = var.strip()
    value = value.strip()
    return var, value


if __name__ == '__main__':
    list_env(['-sn', 'srv-cc3vjrhgp3jqnl0qugog', '--table'])
