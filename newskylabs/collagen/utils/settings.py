"""newskylabs/collagen/utils/settings.py:

Project settings.

When a user settings file '~/.collagen/settings.yaml' exists and it a
setting is defined in this file, the setting is read from the user
settings file; when no user settings file exists or the setting is not
found in the user's settings file it is retrived from the default
settings file 'default_settings.yaml' in the current directory; when
the setting is not found there either, 'None' is returned.

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/18"

import os
import yaml

from newskylabs.collagen.utils.generic import set_recursively, get_recursively

# Setting file names
_settings_file = os.path.join(os.path.expanduser('~'), '.collagen/settings.yaml')
_default_settings_file = os.path.join(os.path.dirname(__file__), 'default_settings.yaml')

# The settings are cached in varables so that the setting files only
# have to be read once
_settings = None
_default_settings = None

def load_settings_file(settings_file):
    """Load a yaml settings file"""
    
    if os.path.isfile(settings_file):
        with open(settings_file, 'r') as ymlfile:
            return yaml.load(ymlfile, Loader=yaml.SafeLoader)

    else:
        return None

def ensure_settings_loaded():
    """Ensure that the settings files have been loaded"""
    
    global _settings
    if _settings == None:
        _settings = load_settings_file(_settings_file)
        
    global _default_settings
    if _default_settings == None:
        _default_settings = load_settings_file(_default_settings_file)

def overwrite_settings(settings):
    """Overwrite the settings for testing."""

    global _settings

    _settings = settings

def set_setting(keychain, value):
    """Define a setting."""

    global _settings

    set_recursively(_settings, keychain, value)

def get_setting(keychain):
    """Retrive a setting"""

    # Ensure that the setting files have been loaded
    ensure_settings_loaded()

    # When defined use the user settings
    value = get_recursively(_settings, keychain)
    if value != None:
        return value

    # When the user has not overwritten a setting use the default
    # settings
    value = get_recursively(_default_settings, keychain)
    if value != None:
        return value

    # When a setting has neither been defined in the user settings nor
    # in the default settings return None
    else:
        return None

## =========================================================
## =========================================================

## fin.
