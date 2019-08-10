"""tests/collagen/datasets/test_mnist.py:

Tests for collagen/datasets/mnist.py

Usage:

pytest tests/collagen/datasets/test_mnist.py

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/21"

import pytest
import numpy as np
from numpy.testing import assert_array_equal, assert_allclose

from newskylabs.collagen.utils.settings import get_setting
from newskylabs.collagen.utils.test import generate_test_environment, get_test_dataset
from newskylabs.collagen.utils import idxgz

## =========================================================
## Test utilities
## ---------------------------------------------------------

def generate_environment(dataset, tmpdir):
    """Set up a test environment."""

    print(">>> Test environment:")
    print("dataset:", dataset)
    print("tmpdir:", tmpdir)

    generate_test_environment(tmpdir, dataset)

    return { 'dataset': dataset, 'tmpdir': tmpdir }

def test_data():
    """
    Test data: {0: [[[0]]], 1: [[[1]]], 2: [[[2]]], ... 9: [[[9]]]}
    The values are numpy uint8 arrays.
    """

    data = {}
    for i in range(10):
        data[i] = np.array([[[i]]]).astype('uint8')

    # For testing the tests :)
    #| data[5] = np.array([[[55]]]).astype('uint8')
        
    return data

def test_data_train():

    data = test_data()
    
    for i in range(10):
        data[i] = 245 - data[i]

    for i in range(10):
        data[i] = data[i].astype(np.float32) / 255.0

    return data

def test_data_test():

    data = test_data()

    for i in range(10):
        data[i] = 235 - data[i]

    for i in range(10):
        data[i] = data[i].astype(np.float32) / 255.0

    return data

def assert_digit_dict_allclose(digits1, digits2):
    """
    Assert that the digit dictionaries are equal to a 
    relative tollerance of 1e-3.

    NOTE that this currently does only work if the corresponding lists
    of digit shapes are in the same order!
    """

    rtol = 1e-3
    atol = 0
    allclose = True
    for i in range(10):
        allclose = allclose and assert_allclose(digits1[i], digits2[i], rtol=rtol, atol=atol)

    return allclose

## =========================================================
## Test fixtures
## ---------------------------------------------------------

@pytest.fixture
def environment_min1(tmpdir):
    """Set up a test environment using test dataset 'min1'."""
    return generate_environment('min1', tmpdir)
    
@pytest.fixture
def environment_min3(tmpdir):
    """Set up a test environment using test dataset 'min3'."""
    return generate_environment('min3', tmpdir)

## =========================================================
## Tests
## ---------------------------------------------------------

def test_generate_test_environment(environment_min3):
    """
    Test for: generate_test_environment(tmpdir, dataset)
    """

    # Test environment
    environment = environment_min3
    dataset = environment['dataset']
    tmpdir  = environment['tmpdir']
    
    print(">>> Test environment:")
    print("dataset:", dataset)
    print("tmpdir:", tmpdir)

    # Generate the archive files
    for usage in ['train', 'test']:
        for dstype in ['images', 'labels']:
        
            dataset_type = usage + '.' + dstype
        
            # Unpack the corresponding archive file
            # 
            # mnist_dataset 
            # 
            # Examples: 
            # 
            #   - datasets.mnist.train.images
            #   - datasets.mnist.train.labels
            #   - datasets.mnist.test.images
            #   - datasets.mnist.test.labels
            # 
            mnist_dataset = 'datasets.mnist.' + dataset_type
            filepath = get_setting(mnist_dataset)
        
            # 'file:///some/path' to '/some/path'
            if filepath[:7] == 'file://':
                filepath = filepath[7:]
                
            # Unpack the archive
            data = idxgz.load(filepath)

            # DEBUG
            print(">>> Data loaded from archive:")
            print("type:", type(data))
            print("dtype:", data.dtype)
            print("shape:", data.shape)            
            #| print("data:", data)

            # Get the corresponding test data
            # 
            # test_dataset
            # 
            # Examples: 
            # 
            #   - min.train.images
            #   - min.train.labels
            #   - min.test.images
            #   - min.test.labels
            # 
            test_dataset = dataset + '.' + dataset_type
            test_data = get_test_dataset(test_dataset)

            # DEBUG
            print(">>> Test data:")
            print("type:", type(test_data))
            print("dtype:", test_data.dtype)
            print("shape:", test_data.shape)
            #| print("test_data:", test_data)

            # Assert that the unpacked data
            # and the test data are the same
            assert_array_equal(data, test_data)

def test_ensure_downloaded_TODO(environment_min3):
    assert True

    #| from newskylabs.collagen.utils.test import generate_test_environment
    #| generate_test_environment('/tmp', '123')
    #| from newskylabs.collagen.datasets.mnist import ensure_downloaded
    #| ensure_downloaded('datasets.mnist.train.labels')

def test_ensure_dataset_archive_TODO(environment_min3):
    assert True

    #| from newskylabs.collagen.utils.test import generate_test_environment
    #| generate_test_environment('/tmp', '123')
    #| from newskylabs.collagen.datasets.mnist import ensure_dataset_archive
    #| ensure_dataset_archive('datasets.mnist.train.labels', debug=True)
    #| ensure_dataset_archive('datasets.mnist.train.images', debug=True)

def test_test_load_dataset_TODO(environment_min3):
    assert True

    #| from newskylabs.collagen.utils.test import generate_test_environment
    #| generate_test_environment('/tmp', '123')
    #| from newskylabs.collagen.datasets.mnist import load_dataset
    #| def test_load_dataset(dataset):
    #|     print("load_dataset('{}', debug=True):".format(dataset))
    #|     print(load_dataset(dataset, debug=True))
    #| test_load_dataset('datasets.mnist.train.labels')
    #| test_load_dataset('datasets.mnist.train.images')

def test_load_data_TODO(environment_min3):
    assert True

    #| from newskylabs.collagen.utils.test import generate_test_environment
    #| generate_test_environment('/tmp', '123')
    #| from newskylabs.collagen.datasets.mnist import load_data
    #| (x_train, y_train), (x_test, y_test) = load_data()
    #| print(">>> x_train:", x_train)
    #| print(">>> y_train:", y_train)
    #| print(">>> x_test:", x_test)
    #| print(">>> y_test:", y_test)

def test_ensure_digit_database_TODO(environment_min3):
    assert True

    #| from newskylabs.collagen.utils.test import generate_test_environment
    #| generate_test_environment('/tmp', '123')
    #| from newskylabs.collagen.datasets.mnist import ensure_digit_database
    #| ensure_digit_database('train')
    #| ensure_digit_database('test')

## TODO: This function is not defined anymore - how should this be done now?
## from newskylabs.collagen.datasets.mnist import load_digit_database
##

def test_load_digit_database__train(environment_min1):

    # ======================================
    # set: train
    # --------------------------------------
    
    data = load_digit_database('train')
    print("data:     ", data)
    
    test_data = test_data_train()
    print("test_data:", test_data)
    
    # Assert that the loaded data
    # and the expected data are the same
    assert_array_equal(data, test_data)
    
def test_load_digit_database__test(environment_min1):

    # ======================================
    # set: test
    # --------------------------------------
    
    data = load_digit_database('test')
    print("data:     ", data)
    
    test_data = test_data_test()
    print("test_data:", test_data)
    
    # Assert that the loaded data
    # and the expected data are the same
    assert_array_equal(data, test_data)
    
## =========================================================
## =========================================================

## fin.
