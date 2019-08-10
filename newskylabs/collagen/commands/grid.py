"""newskylabs/collagen/commands/grid.py:

Grid command: Generate an image displaying a grid of randomly selected
shapes for the digit given as parameter.

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/24"

from newskylabs.collagen.generators.digit_generator import DigitGenerator

## =========================================================
## Grid command
## ---------------------------------------------------------

def collagen_grid(digit, 
                  height=10, width=10, 
                  dataset='mnist', subset='train',
                  spec=None, scale=1, show=True):
    """Grid command."""

    print("Generating a {}x{} grid of random shapes of digit {}".format(height, width, digit))
    
    gen = DigitGenerator(dataset=dataset, subset=subset)

    image = gen.grid(digit, 
                     height=height, width=width, 
                     spec=spec)
    
    if show:
        image.save_and_show(scale=scale)
    else:
        image.save(scale=scale)

## =========================================================
## =========================================================

## fin.
