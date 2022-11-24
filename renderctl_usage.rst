renderctl
=========

.. |Tests| image:: https://github.com/mnapoleon/renderctl/workflows/Tests/badge.svg
    :target: https://github.com/mnapoleon/renderctl/actions?workflow=Tests

Installation
------------
To install the renderctl package, run this command in your terminal

.. code-block:: console

    $ pip install renderctl

Setup
-----
You will need to get an environment variable to your Render API key in order to use the cli
 .. code-block:: console

    $ export RENDER_TOKEN=<api-token>

This token can you created in your Render Account Settings -> Api Keys.

Usage
-----
renderctl usage looks like:

Usage: cli [OPTIONS] COMMAND [ARGS]...

  A cli to manage your Render services.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  dump-help     Command to dump all help screen.

  find-service  Finds a Render service by name.

  list          Returns a list of all services associated with your Render account.

  list-env      Fetches list of environment variables of a service.

  set-env       Will set environment variables for the specified service.

====
list
====

Usage: cli list [OPTIONS]

  Returns a list of all services associated with your Render account.

  Args:     verbose: option to return a formatted json dump of all services
  instead of the default table view which just displays the         service
  name, service id and service url.

Options:
  -v, --verbose  Display full json output from render api call.
  --help         Show this message and exit.

============
find-service
============

Usage: cli find-service [OPTIONS]

  Finds a Render service by name.

  Returns information about service if found.

  Args:     service_name: name of service to search for.

Options:
  -sn, --service-name TEXT  Find service by name
  --help                    Show this message and exit.

=======
set-env
=======

Usage: cli set-env [OPTIONS]

  Will set environment variables for the specified service.

  Args:     file: path to file containing the environment variables to set.

Options:
  -f, --file TEXT  File to load env vars from
  --help           Show this message and exit.

========
list-env
========

Usage: cli list-env [OPTIONS]

  Fetches list of environment variables of a service.

  Returns and lists the environment variables associated with     the passed
  in service id or service name.  Verbose mode     will display json.

  Args:     service_id: id of service whose environment variables to find.
  service_name: name of service whose environment variables to find.
  verbose: option to return a formatted json dump of all environment
  variable information.

Options:
  -sid, --service-id TEXT   Render service id
  -sn, --service-name TEXT  Render service name
  -v, --verbose             Display full json output from render api call.
  --help                    Show this message and exit.

=========
dump-help
=========
Usage: cli dump-help [OPTIONS]

  Command to dump all help screen.

Options:
  --help  Show this message and exit.
