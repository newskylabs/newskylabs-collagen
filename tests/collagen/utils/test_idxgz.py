"""tests/collagen/utils/test_idx_tools.py:

Tests for collagen/utils/idx_tools.py.
"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/20"

## =========================================================
## Tests
## ---------------------------------------------------------

import numpy as np
from numpy.testing import assert_array_equal

from newskylabs.collagen.utils import idxgz

def test_idxgz_load_and_save(tmpdir):
    """Create idxgz.load() and idxgz.save()"""
    
    archive = tmpdir.join("idx.gz")
    
    # Test data
    data = np.array([1, 2, 3]).astype('uint8')

    print("Before packing:")
    print("data:", data)
    print("type(data):", type(data))
    print("data.dtype:", data.dtype)
    print("data.shape:", data.shape)

    # Save to file
    idxgz.save(archive, data)

    # Load from file
    data2 = idxgz.load(archive)

    print("After unpacking:")
    print("data2:", data2)
    print("type(data2):", type(data2))
    print("data2.dtype:", data2.dtype)
    print("data2.shape:", data2.shape)

    assert_array_equal(data, data2)
    assert type(data) == type(data2)
    assert data.dtype == data2.dtype
    assert data.shape == data2.shape

## =========================================================
## =========================================================

## fin.
