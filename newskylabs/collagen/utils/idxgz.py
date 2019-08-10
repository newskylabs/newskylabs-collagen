"""newskylabs/collagen/utils/idx_tools.py:

Tools to read and write idx encoded files.

See:

  - The MNIST database of handwritten digits
    http://yann.lecun.com/exdb/mnist/

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/20"

import idx2numpy
import gzip

def load(archive):
    """Uncompress `archive` and convert its content from idx format to a numpy
    array.

    """
    with gzip.open(archive, 'rb') as infp:
        data = idx2numpy.convert_from_file(infp)
        return data

def save(archive, data):
    """Convert `data` to idx format and save it as gz compressed `archive`
    file.

    """
    with gzip.open(archive, 'wb') as outfp:
        idx2numpy.convert_to_file(outfp, data)

## =========================================================
## =========================================================

## fin.
