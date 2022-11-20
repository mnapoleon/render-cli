"""Render Command-line interface."""
import json
from typing import Any


import click
from rich.console import Console


from renderctl.output.services_output import (
    output_env_vars_as_table,
    output_services_as_table,
)
from renderctl.render_services import (
    deploy_service,
    fetch_services,
    find_service_by_name,
    retrieve_env_from_render,
)
from . import __version__


@click.group()
@click.version_option(version=__version__)
def cli() -> None:
    """A cli to manage your Render services."""
    pass


@cli.command("list")
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    help="Display full json output from render api call.",
)
def list_services(verbose) -> Any:
    """Returns a list of all services associated with your Render account.

    Args:
        verbose: option to return a formatted json dump of all services
            instead of the default table view which just displays the
            service name, service id and service url.
    """
    data = fetch_services()
    if verbose:
        click.echo(json.dumps(data, indent=4))
    else:
        console = Console()
        click.echo("\n")
        console.print(output_services_as_table(data))


@cli.command("find-service")
@click.option("-sn", "--service-name", type=str, help="Find service by name")
def find_service(service_name) -> Any:
    """Finds a Render service by name.

    Returns information about service if found.

    Args:
        service_name: name of service to search for.
    """
    data = find_service_by_name(service_name)
    click.echo(json.dumps(data, indent=4))


@cli.command("set-env")
@click.option("-f", "--file", type=str, help="File to load env vars from")
def set_env(file):
    """Will set environment variables for the specified service.

    Args:
        file: path to file containing the environment variables to set.

    """
    env_vars = {}
    with open(file) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            else:
                var, value = line.split("=")
                env_vars[var.strip()] = value.strip()
    for k, v in env_vars.items():
        click.echo(f"{k} = {v}")


@cli.command("list-env")
@click.option("-sid", "--service-id", type=str, help="Render service id")
@click.option("-sn", "--service-name", type=str, help="Render service name")
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    help="Display full json output from render api call.",
)
def list_env(service_id, service_name, verbose):
    """Fetches list of environment variables of a service.

    Returns and lists the environment variables associated with
        the passed in service id or service name.  Verbose mode
        will display json.

    Args:
        service_id: id of service whose environment variables to find.
        service_name: name of service whose environment variables to find.
        verbose: option to return a formatted json dump of all environment
            variable information.

    """
    if not service_id:
        if service_name:
            service_id = find_service_by_name(service_name)["service"]["id"]
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
@click.option("-sid", "--service-id", type=str, help="Deploys named service")
def deploy(service_id):
    """Will deploy a service to Render...maybe.

    Args:
        service_id: id of service to deploy.

    """
    result = deploy_service(service_id)
    click.echo(json.dumps(result, indent=4))
