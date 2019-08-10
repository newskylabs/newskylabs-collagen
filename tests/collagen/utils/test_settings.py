"""tests/collagen/utils/test_settings.py: 

Tests for collagen/utils/settings.py
"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/18"

import pytest
import os
import yaml

from newskylabs.collagen.utils.settings import get_setting

## =========================================================
## Test utilities
## ---------------------------------------------------------

def write_settings(dic, settings_file):
    with open(settings_file, 'w') as stream:
        yaml.dump(dic, stream)

def cat_settings(header, settings_file):
    print(">>> default_settings.yaml:")
    with open(settings_file, 'r') as stream:
        print(stream.read())

## =========================================================
## Test fixtures
## ---------------------------------------------------------

@pytest.fixture
def settings(tmpdir):
    """Create test settings"""
    import collagen.utils.settings as settings

    # Test default settings
    default_settings_dic = { 
        'default_setting': 'default',
        'overwritten_setting': 'not_overwritten',
        'a': 1,
        'b': {
            'c': 2,
            'd': [
                3, 
                4, 
                { 
                    'e': 5
                }, 
                7
            ],
        },
        'h': 9
    }

    # Test settings
    settings_dic = {
        'overwritten_setting': 'overwritten',
        'b': {
            'c': 22,
            'd': [
                3, 
                4, 
                { 
                    'f': 6
                }, 
                77
            ],
            'g': 8
        }
    }

    # Create a settings directory
    setting_dir = tmpdir.mkdir(".collagen")

    # Write the test default settings to the test default settings file
    settings._default_settings = None
    settings._default_settings_file = setting_dir.join("default_settings.yaml")
    write_settings(default_settings_dic, settings._default_settings_file)

    print("settings._default_settings:", settings._default_settings)
    print("settings._default_settings_file:", settings._default_settings_file)
    cat_settings(">>> default_settings.yaml:", settings._default_settings_file)
    
    # Write the test settings to the test settings file
    settings._settings = None
    settings._settings_file = setting_dir.join("settings.yaml")
    write_settings(settings_dic, settings._settings_file)

    print("settings._settings:", settings._settings)
    print("settings._settings_file:", settings._settings_file)
    cat_settings(">>> settings.yaml:        ", settings._settings_file)

## =========================================================
## Tests
## ---------------------------------------------------------

def test_settings1(settings):

    print(">>> Settings:")
    print("get_setting('default_setting'):    ", get_setting('default_setting'))
    print("get_setting('overwritten_setting'):", get_setting('overwritten_setting'))
    print("get_setting('undefined_setting'):  ", get_setting('undefined_setting'))

    assert get_setting('default_setting')     == "default"
    assert get_setting('overwritten_setting') == "overwritten"
    assert get_setting('undefined_setting')   == None

def test_settings2(settings):

    for keychain, expected_value in [
            ('a', 1),
            ('b.c', 22),
            ('b.d.0', 3),
            ('b.d.1', 4),
            ('b.d.2.e', 5),
            ('b.d.2.f', 6),
            ('b.d.3', 77),
            ('b.g', 8),
            ('h', 9),
            ('z', None),
            ('a.b.c', None),
            ('b.d.4', None),
            ('b.d.2.g', None),
    ]:
        assert get_setting(keychain) == expected_value

## =========================================================
## =========================================================

## fin.
