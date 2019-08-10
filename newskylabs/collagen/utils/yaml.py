"""newskylabs/collagen/utils/yaml.py:

yaml tools.

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/08/02"

import yaml
import io

## =========================================================
## Load yaml files
## ---------------------------------------------------------

def load_yaml_stream(stream):
    """Load a yaml specification from the given stream and return it.

    """
    try:
        return yaml.load(stream, Loader=yaml.SafeLoader)
    
    except yaml.YAMLError as exception:
        print(exception)

def load_yaml_file(file):
    """Load a yaml specification from the given file and return it.

    """

    # When a file has not been given print an error and exit
    if not file:
        raise SystemExit('\nError: No yaml file given!\n')

    if issubclass(type(file), str):
        with open(file, 'r') as stream:
            return load_yaml_stream(stream)
        
    elif issubclass(type(file), io.IOBase):
        return load_yaml_stream(file)

    else:
        raise SystemExit('\nError: Cannot load yaml spec from object of type {}!\n'.format(type(file)))
        
## =========================================================
## =========================================================

## fin.
