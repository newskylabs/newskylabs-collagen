"""newskylabs/collagen/utils/test.py:

Test utilities.

Utilities and data used to test collagen's functionality
"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/20"

import os, py
import numpy as np

from newskylabs.collagen.utils.settings import overwrite_settings, get_setting
from newskylabs.collagen.utils.generic import ensure_dir
from newskylabs.collagen.utils import idxgz
from newskylabs.collagen.utils.test_datasets import get_test_dataset

## =========================================================
## Test utility functions
## ---------------------------------------------------------

def generate_test_settings(tmpdir, dataset):
    """
    Temporarily overwrite the settings with test settings.

    This allows to use test datasets for testing.
    """

    # When `tmpdir` is a path convert it to a string
    if isinstance(tmpdir, py._path.local.LocalPath):
        tmpdir = str(tmpdir)
        
    test_settings = {
        
        'datasets': {
            'mnist': {
                'train': {
                    'images': "file://" + tmpdir + "/" + dataset + "/server/train-images-idx3-ubyte.gz",
                    'labels': "file://" + tmpdir + "/" + dataset + "/server/train-labels-idx1-ubyte.gz"
                },
                'test': {
                    'images': "file://" + tmpdir + "/" + dataset + "/server/t10k-images-idx3-ubyte.gz",
                    'labels': "file://" + tmpdir + "/" + dataset + "/server/t10k-labels-idx1-ubyte.gz"
                },
            },
        },
        'data-dir': tmpdir + "/" + dataset + "/data"
    }
    overwrite_settings(test_settings)

## =====================================
## Using my own datasets for testing
## -------------------------------------

def generate_test_dataset_archive(filepath, dataset):
    """Generate archive files for the given test dataset in tmpdir
    """

    # 'file:///some/path' to '/some/path'
    if filepath[:7] == 'file://':
        filepath = filepath[7:]

    # Check if the dataset exists.
    # When not been generate it.
    if not os.path.isfile(filepath):

        print("Generating", filepath)
        data = get_test_dataset(dataset)
        
        ensure_dir(os.path.dirname(filepath))
        idxgz.save(filepath, data)

    
def generate_test_environment(tmpdir, dataset):
    """
    Generate a test environment using the given dataset.
    The settings are temporarily overwritten to use the test data.
    """

    # Overwrite settings with test settings
    generate_test_settings(tmpdir, dataset)

    # Generate the archive files
    for usage in ['train', 'test']:
        
        for dstype in ['images', 'labels']:
            
            dataset_type = usage + '.' + dstype
            
            mnist_dataset = 'datasets.mnist.' + dataset_type
            filepath = get_setting(mnist_dataset)

            test_dataset = dataset + '.' + dataset_type
            generate_test_dataset_archive(filepath, test_dataset)

def test_generate_test_environment(dataset):
    """
    For debugging test environments

    Usage examples:

    test_generate_test_environment('123')
    test_generate_test_environment('2x2')
    """

    print("## =========================================================")
    print("## Dataset:", dataset)
    print("## ---------------------------------------------------------")
    print("")

    tmpdir = "/tmp/collagen"

    generate_test_environment(tmpdir, dataset)

    # Generate the archive files
    for usage in ['train', 'test']:
        for dstype in ['images', 'labels']:
        
            dataset_type = usage + '.' + dstype
        
            mnist_dataset = 'datasets.mnist.' + dataset_type
            filepath = get_setting(mnist_dataset)
        
            # 'file:///some/path' to '/some/path'
            if filepath[:7] == 'file://':
                filepath = filepath[7:]

            # Unpack
            print("")
            print("{}: {}".format(mnist_dataset, filepath))
            print("")
            data = idxgz.load(filepath)
            print("data:", data)
            print("type:", type(data))
            print("dtype:", data.dtype)
            print("shape:", data.shape)

    print("")

## =========================================================
## =========================================================

## fin.
