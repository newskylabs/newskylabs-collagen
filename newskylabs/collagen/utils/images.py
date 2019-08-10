"""newskylabs/collagen/utils/images.py:

Example images.

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/03/13"

import numpy as np

def checkerboard(size=5, scale=5, colour=255):
    """
    Generate a checkerboare image.
    """
    m = scale
    s = size * scale

    rows = [
        [((i // m + 1) % 2) for i in range(s)],
        [((i // m) % 2) for i in range(s)]
    ]

    image = []
    for i in range(s):
        j = (i // m + 1) % 2
        image.append(rows[j])

    return np.array(image).astype('uint8') * colour

def checkerboard2(size=(3, 4), scale=5, colour=255):
    """
    Generate a checkerboare image.
    """
    m = scale
    sy, sx = size
    sy *= scale
    sx *= scale

    rows = [
        [((i // m + 1) % 2) for i in range(sx)],
        [((i // m) % 2) for i in range(sx)]
    ]

    image = []
    for i in range(sy):
        j = (i // m + 1) % 2
        image.append(rows[j])

    return np.array(image).astype('uint8') * colour

## =========================================================
## =========================================================

## fin.
