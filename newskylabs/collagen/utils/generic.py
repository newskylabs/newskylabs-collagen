"""newskylabs/collagen/utils/generic.py:

Various generic utilities...

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/20"

import os, sys, re
from os.path import join, dirname, isfile
import pathlib

## =========================================================
## Setup tools
## ---------------------------------------------------------

def get_version():
    """Return package version as defined in `setup.py` (ex: 1.2.3)."""

    package_base_dir = get_package_base_dir()
    
    main_file = os.path.join(package_base_dir, 'collagen/__main__.py')
    init_py = open(main_file).read()
    match = re.search("__version__\s*=\s*['\"]([^'\"]+)['\"]", init_py)
    if match:
        version = match.group(1)
        return version
    else:
        raise RuntimeError("Unable to find version string in %s." % main_file)

def get_version_long():
    """Return long package version (ex: 1.2.3 (Python 3.4.5))."""

    return '{} (Python {})'.format(get_version(), sys.version[:5])

## =========================================================
## Tools for files and directories
## ---------------------------------------------------------

def ensure_dir(directoy):
    """Ensure that the given `directory` exists."""

    pathlib.Path(directoy).mkdir(parents=True, exist_ok=True)

def get_package_base_dir():
    """Get the base dir of the package by searching the directory tree
    upward till a directory without '__init__.py' has been found.

    """
    directory = dirname(__file__);
    while isfile(join(directory, '__init__.py')):
        directory = dirname(directory)

    return directory

def get_package_dir(package):
    """Get the base dir of the package by searching the directory tree
    upward till a directory without '__init__.py' has been found.

    """
    relative_package_dir = package.replace('.', '/')
    package_base_dir = get_package_base_dir()
    package_dir = join(package_base_dir, relative_package_dir)
    return package_dir

## =========================================================
## Tools for python dictionaries
## ---------------------------------------------------------

def set_recursively(structure, path, value):
    """Set a value in a recursive structure."""

    path = path.split('.')
    lastkey = path.pop()

    for key in path:
        if not key in structure or not isinstance(structure[key], dict):
            structure[key] = {}
        structure = structure[key]

    structure[lastkey] = value
    
def get_recursively(structure, keychain):
    """Get a value from a recursive structure."""

    val = structure

    # Follow the key chain to recursively find the value
    for key in keychain.split('.'):
        if isinstance(val, dict) and key in val:
            val = val[key]
        elif key.isdigit() and isinstance(val, list) and int(key) < len(val):
            val = val[int(key)]
        else:
            return None

    return val

## =========================================================
## Pretty printing
## ---------------------------------------------------------

def pretty_print_numpy_array(array, var='array'):
    """
    Pretty print a numpy array.
    """
    
    height, width = array.shape

    print('{} = ['.format(var))


    for y in range(height):
        
        print('    ', end='')

        for x in range(width):
            
            if x == 0:
                print('[ ', end='')
            else:
                print(', ', end='')

            print('{:3d}'.format(array[y][x]), end='')

        if y < height-1:
            print(' ],')
        else:
            print(' ]')

    print("]")

def pretty_print_numpy_array2(array):
    """
    Pretty print a numpy array.
    """
    
    height, width = array.shape
    
    for y in range(height):
        
        if y == 0:
            print('  [ ', end='')
        else:
            print('    ', end='')

        for x in range(width):
            
            if x == 0:
                print('[ ', end='')
            else:
                print(', ', end='')

            print('{:3d}'.format(array[y][x]), end='')

        if y < height-1:
            print(' ],')
        else:
            print(' ] ]')

    print("")

## =========================================================
## =========================================================

## fin.
