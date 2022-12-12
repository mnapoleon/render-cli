# render-cli

-------------

[![Tests](https://github.com/mnapoleon/renderctl/workflows/Tests/badge.svg)](https://github.com/mnapoleon/renderctl/actions?workflow=Tests)
[![Codecov](https://codecov.io/gh/mnapoleon/renderctl/branch/main/graph/badge.svg)](https://codecov.io/gh/mnapoleon/renderctl)
[![PyPI](https://img.shields.io/pypi/v/render-cli.svg)](https://pypi.org/project/renderctl/)

---------


## Installation
To install the renderctl package, run this command in your terminal

    $ pip install renderctl

#3 Setup
You will need to get an environment variable to your Render API key in order to use the cli

    $ export RENDER_TOKEN=<api-token>

This token can you created in your Render Account Settings -> Api Keys.


## Usage
 render-cli usage looks like:

Usage: `cli [OPTIONS] COMMAND [ARGS]...`

A cli to manage your Render services.

### Options:

  `--version  Show the version and exit.`

  `--help     Show this message and exit.`

***

## Commands:

  - **dump-help**     Command to dump all help screen.

  - **find-service**  Finds a Render service by name.

  - **list**          Returns a list of all services associated with your Render account.

  - **list-env**      Fetches list of environment variables of a service.

  - **set-env**       Will set environment variables for the specified service.

***
### list

Usage: `cli list [OPTIONS]`

Returns a list of all services associated with your Render account.

Options:

    -v, --verbose  Display full json output from render api call.
    --help         Show this message and exit.

![list services!](./assets/list_services.gif "list services")

***

### find-service

Usage: `cli find-service [OPTIONS]`

Finds a Render service by name.

Returns information about service if found.

Options:
    
    -sn, --service-name TEXT  Find service by name
    --help                    Show this message and exit.

![find servicw!](./assets/find_service.gif "find service")

***

### list-env

Usage: `cli list-env [OPTIONS]`

  Fetches list of environment variables of a service.

  Returns and lists the environment variables associated with the passed
  in service id or service name.  Verbose mode will display json.


  Options:

      -sid, --service-id TEXT   Render service id
      -sn, --service-name TEXT  Render service name
      -v, --verbose             Display full json output from render api call.
      --help                    Show this message and exit.

![list env!](./assets/list_env.gif "list env")

***

### set-env

Usage: `cli set-env [OPTIONS]`

  Will set environment variables for the specified service.

Options:

  -f, --file TEXT  File to load env vars from
  -sn, --service-name TEXT  Render service name
  --help           Show this message and exit.

![set_envs!](./assets/set_envs.gif "set envs")

***

#### dump-help

Usage: `cli dump-help [OPTIONS]`

  Command to dump all help screen.

  Options:
    
    --help  Show this message and exit.
