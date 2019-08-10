"""tests/collagen/utils/conversion.py:

Tests for collagen/utils/conversion.py

Usage:

pytest tests/collagen/utils/test_conversion.py 

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/20"

import pytest
import numpy as np
from numpy.testing import assert_array_equal, assert_allclose

## =========================================================
## Test fixtures
## ---------------------------------------------------------

@pytest.fixture
def datasets():
    """Set up test datasets"""

    return {
        
        'letter_uint8': np.array([
            [  0, 50],
            [100,150],
            [200,255]
        ]),
        
        'dataset_uint8': np.array([ [ [0], [255] ], [ [55], [200] ] ])
    }

## =========================================================
## Tests
## ---------------------------------------------------------

from newskylabs.collagen.utils.conversion import convert_mnist2collagen

def test_convert_mnist2collagen(datasets):

    letter_uint8 = datasets['letter_uint8']
    rtol = 1e-3
    atol = 0

    assert_allclose(
        convert_mnist2collagen(letter_uint8, debug=True),
        np.array([
            [1.0,    0.8039],
            [0.6078, 0.4118],
            [0.2157, 0.0   ]
        ]),
        rtol=rtol, 
        atol=atol)

    dataset_uint8 = datasets['dataset_uint8']
    
    assert_allclose(
        convert_mnist2collagen(dataset_uint8, debug=True),
        np.array([ [ [1.0], [0.0] ], [ [0.7843], [0.2157] ] ]),
        rtol=rtol, 
        atol=atol)
    
## =========================================================
## =========================================================

## fin.
