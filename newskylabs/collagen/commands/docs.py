"""newskylabs/collagen/commands/docs.py:

Documentation related utility functions:

  - collagen_docs(): 

    Start a local documentation server.

  - collagen_build_docs():

    Build static documentation for deployment on the documentation
    server.

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/23"

## =========================================================
## Main entry points
## ---------------------------------------------------------

import os
from mkdocs import exceptions, config
from mkdocs.commands import serve, build
from newskylabs.collagen.utils.generic import get_package_dir

def collagen_docs():
    """Utility function to start a local documentation server.
    
    The server allows for easy preview during the editing procedure:
    The pages displayed in the browser are automatically updated when
    the markdown sources are edited.

    """

    # Get the mkdocs collagen documentatio directory
    docs_package_dir = get_package_dir('collagen.docs')
    mkdocs_dir = os.path.join(docs_package_dir, 'docs')

    # Change working directory to the mkdocs documentation directory
    # containing the `mkdocs.yml` file
    os.chdir(mkdocs_dir)

    try:
        # See:
        # 
        #   - @cli.command(name="serve")
        #     in https://github.com/mkdocs/mkdocs/blob/master/mkdocs/__main__.py
        # 
        serve.serve()
    except (exceptions.ConfigurationError, socket.error) as e:

        # Avoid ugly, unhelpful traceback
        raise SystemExit('\n' + str(e))
    
def collagen_build_docs():
    """Build the collagen documentation."""

    # Get the mkdocs collagen documentatio directory
    docs_package_dir = get_package_dir('collagen.docs')
    mkdocs_dir = os.path.join(docs_package_dir, 'docs')

    print("Building Collagen's documentation to directory:", mkdocs_dir)

    # Change working directory to the mkdocs documentation directory
    # containing the `mkdocs.yml` file

    os.chdir(mkdocs_dir)

    # Build configuration
    config_file = None
    strict      = None
    theme       = None
    theme_dir   = None
    site_dir    = None
    clean       = True

    try:
        # See:
        # 
        #   - @cli.command(name="build")
        #     in https://github.com/mkdocs/mkdocs/blob/master/mkdocs/__main__.py
        # 
        build.build(config.load_config(
            config_file=config_file,
            strict=strict,
            theme=theme,
            theme_dir=theme_dir,
            site_dir=site_dir
        ), dirty=not clean)
        
    except exceptions.ConfigurationError as e:
        
        # Avoid ugly, unhelpful traceback
        raise SystemExit('\n' + str(e))
    
## =========================================================
## =========================================================

## fin.
