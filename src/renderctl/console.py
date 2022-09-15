import json

import click
from rich.console import Console
from renderctl.render_services import \
    fetch_services, retrieve_env_from_render, deploy_service, find_service_by_name
from renderctl.output.services_output import output_services_as_table, output_env_vars_as_table
#from . import __version__
__version__ = "3.4"

@click.group()
def cli():
    pass


@cli.command('list')
@click.option('-v', '--verbose', is_flag=True, help='Display full json output from render api call.')
def list_services(verbose):
    data = fetch_services()
    if verbose:
        click.echo(json.dumps(data, indent=4))
    else:
        console = Console()
        click.echo("\n")
        console.print(output_services_as_table(data))


@cli.command('find-service')
@click.option('-sn', '--service-name', type=str, help='Find service by name')
def find_service(service_name):
    data = find_service_by_name(service_name)
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
@click.option('-sid', '--service-id', type=str, help='Render service id')
@click.option('-sn', '--service-name', type=str, help='Render service name')
@click.option('-v', '--verbose', is_flag=True)
def list_env(service_id, service_name, verbose):
    if not service_id:
        if service_name:
            service_id = find_service_by_name(service_name)['service']['id']
        else:
            click.echo("Need to provide service id or service name options")
            exit()
    data = retrieve_env_from_render(service_id)
    if verbose:
        click.echo(json.dumps(data, indent=4))
    else:
        console = Console()
        click.echo("\n")
        console.print(output_env_vars_as_table(data))


@cli.command()
@click.option('-sid', '--service-id', type=str, help='Deploys named service')
def deploy(service_id):
    result = deploy_service(service_id)
    click.echo(json.dumps(result, indent=4))


@cli.command()
@click.version_option(version=__version__)
def main():
    click.echo("renderctl")


def parse_env_file(input_data):
    var, value = input.split('=')
    var = var.strip()
    value = value.strip()
    return var, value


if __name__ == '__main__':
    #main()
    list_env([])
