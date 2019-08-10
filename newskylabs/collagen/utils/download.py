"""newskylabs/collagen/utils/download.py:

Utility to download files from the internet and store them locally.

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/18"

import progressbar
import urllib.request
import os

from newskylabs.collagen.utils.generic import ensure_dir

# The process bar
_pbar = None

def _show_progress(block_num, block_size, total_size):
    """Show a process bar"""

    global _pbar

    if _pbar is None:
        _pbar = progressbar.ProgressBar(maxval=total_size)

    downloaded = block_num * block_size
    if downloaded < total_size:
        _pbar.update(downloaded)
    else:
        _pbar.finish()
        _pbar = None

def download_file(url, directory):
    """Download a file and store it in directory"""

    ensure_dir(directory)

    filename = os.path.basename(url)
    filepath = os.path.join(directory, filename)

    print("Downloading file", url)
    print("and storing it as", filepath)
    urllib.request.urlretrieve(url, filepath, _show_progress)
    
## =========================================================
## =========================================================

## fin.
