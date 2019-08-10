"""newskylabs/collagen/utils/dataset_tools.py:

Dataset tools.

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/21"

import sys
import importlib
from newskylabs.collagen.utils.dataset_catalog import lookup_dataset_package

## =========================================================
## Utilities
## ---------------------------------------------------------

def import_dataset_module(dataset):
    """Load the given DATASET module.

    """

    # Load the corresponding dataset module
    package = 'newskylabs.datasets.{}'.format(dataset)
    module  = '.dataset'

    print("DEBUG dataset: '{}', package: '{}', module: '{}'".format(dataset, package, module))

    try:
        dataset_module = importlib.import_module(module, package)
    
    except ModuleNotFoundError:

        package_info = lookup_dataset_package(dataset)
        if package_info:

            # The dataset has been found in the registry - 
            # Print installation information:

            package_name = package_info['name']
            installation = package_info['installation']

            print("")
            print("ERROR")
            print("")
            print("  The dataset '{}' has not been installed yet.".format(dataset))
            print("")
            print("  It is defined in the package '{}'".format(package_name))
            print("  and can be installed with:")
            print("")
            print("  {}".format(installation))
            print("")
        
        else:

            print("")
            print("ERROR Unknown dataset: {}".format(dataset))
            print("")

        sys.exit()

    # Load the dataset
    # and return it
    return dataset_module

def load_dataset(dataset, subset):
    """Load the specified SUBSET of the given DATASET in the given
    format.

    """

    # Load the corresponding dataset module
    dataset_module = import_dataset_module(dataset)
    
    # Load the dataset subset
    # and return it
    return dataset_module.load_subset(subset)

def load_dataset_dictionary(dataset, subset):
    """Load the specified SUBSET of the given DATASET 
    as a dictionary with the labels as keys.

    """

    # Load the corresponding dataset module
    dataset_module = import_dataset_module(dataset)
    
    # Load the dataset subset
    # and return it
    return dataset_module.load_subset_dictionary(subset)

## =========================================================
## =========================================================

## fin.
