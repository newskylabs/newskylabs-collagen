"""newskylabs/collagen/utils/dataset_catalog.py:

A Catalog of available datasets - and their corresponding package.

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2019/08/08"

## =========================================================
## _dataset_catalog
## ---------------------------------------------------------

_dataset_catalog = {

    'kuzushiji.kkr': 'newskylabs-datasets-kuzushiji'
}

_dataset_package_catalog = {
    
    'newskylabs-datasets-kuzushiji': {
        'datasets': ['kkr'],
        'installation': 'pip install git+https://github.com/newskylabs/newskylabs-datasets-kuzushiji',
    },
}

## =========================================================
## Exported functionality
## ---------------------------------------------------------

def lookup_dataset_package(dataset):
    
    if dataset in _dataset_catalog:

        package_name = _dataset_catalog[dataset]

        if package_name in _dataset_package_catalog:

            package_info = _dataset_package_catalog[package_name]

            # Add the name of the package to the package info
            package_info['name'] = package_name
            return package_info

    # Not found
    return None

## =========================================================
## =========================================================

## fin.
