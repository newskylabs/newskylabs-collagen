"""newskylabs/collagen/scripts/cdt.py:

Definition of the `cdt` script.

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/23"

import sys, os, click, socket
from subprocess import call

from newskylabs.collagen.commands.deploy import command as deploy
from newskylabs.collagen.commands.docs import collagen_docs, collagen_build_docs
from newskylabs.collagen.utils.generic import get_version_long, get_package_dir

## =========================================================
## Commands 
## ---------------------------------------------------------

@click.group(
    # Help options: -h and --help rather than only --help
    context_settings={'help_option_names': ['-h', '--help']}
)
# Version options: -V, --version
@click.version_option(get_version_long(), '-V', '--version')
def cli():
    """cdt - Collagen development tools."""
    
## =========================================================
## Command: docs
## ---------------------------------------------------------

@cli.command(name="docs")
def command_docs():
    """Run the local collagen documentation development server."""
    collagen_docs()

## =========================================================
## Command: build
## ---------------------------------------------------------

@cli.command(name="build")
def command_build():
    """Build the collagen documentation."""
    collagen_build_docs()

## =========================================================
## Command: deploy
## ---------------------------------------------------------

@cli.command(name="deploy")
def command_deploy():
    """Deploy the documentation on the server."""
    deploy()

## =========================================================
## Command: install
## ---------------------------------------------------------

@cli.command(name="install")
def command_install():
    """Install collagen."""

    # TODO: Add cdt-* scripts dynamically
    call(["cdt-install"])

## =========================================================
## Command: reinstall
## ---------------------------------------------------------

@cli.command(name="reinstall")
def command_reinstall():
    """Reinstall collagen."""
    
    # TODO: Add cdt-* scripts dynamically
    call(["cdt-reinstall"])

## =========================================================
## Command: clean
## ---------------------------------------------------------

# Command: clean
@cli.command(name="clean")
def command_clean():
    """Clean the collagen sources."""
    
    # TODO: Add cdt-* scripts dynamically
    call(["cdt-clean"])

## =========================================================
## Main
## ---------------------------------------------------------

if __name__ == '__main__':
    cli()

## =========================================================
## =========================================================

## fin.
