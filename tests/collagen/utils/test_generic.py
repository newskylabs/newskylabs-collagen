"""tests/collagen/utils/test_generic.py: 

Tests for collagen/utils/generic.py

Usage:

pytest tests/collagen/utils/test_generic.py
"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/21"

import pytest

## =========================================================
## Tests
## ---------------------------------------------------------

from newskylabs.collagen.utils.generic import set_recursively

def test_set_recursively():

    structure = {}
    assert structure == {}

    set_recursively(structure, 'foo.bar.baz', 123)
    assert structure == {'foo': {'bar': {'baz': 123}}}

    set_recursively(structure, 'foo.bar.baz', 321)
    assert structure == {'foo': {'bar': {'baz': 321}}}

    set_recursively(structure, 'one', 1)
    assert structure == {'foo': {'bar': {'baz': 321}}, 'one': 1}

    set_recursively(structure, 'one.two', 2)
    assert structure == {'foo': {'bar': {'baz': 321}}, 'one': {'two': 2}}

from newskylabs.collagen.utils.generic import get_recursively

def test_get_recursively():

    structure = {'foo': {'bar': {'baz': 321}}, 'one': {'two': 2}, 'three': 3}

    assert get_recursively(structure, 'undefined') == None
    assert get_recursively(structure, 'one.two.three') == None

    assert get_recursively(structure, 'three') == 3
    assert get_recursively(structure, 'foo') == {'bar': {'baz': 321}}
    assert get_recursively(structure, 'foo.bar') == {'baz': 321}
    assert get_recursively(structure, 'foo.bar.baz') == 321
    assert get_recursively(structure, 'one') == {'two': 2}
    assert get_recursively(structure, 'one.two') == 2

## =========================================================
## =========================================================

## fin.
