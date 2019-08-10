"""newskylabs/collagen/generators/sequencegenerator.py:

Utility function to generate an image that contains the sequence of
given numbers, spaced randomly using an uniform distribution.

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/23"

from newskylabs.collagen.generators.digit_generator import DigitGenerator

## =========================================================
## Sequence command
## ---------------------------------------------------------

def collagen_sequence(digits, 
                      spacing_range=(0, 3), image_width=0, 
                      dataset='mnist', subset='train',
                      spec=None, scale=1, show=True, debug=False):
    """Sequence command.


    Generate an image that contains the sequence of given numbers, spaced
    randomly using an uniform distribution.

    Parameters
    ----------
    digits:
	A list-like containing the numerical values of the digits from which
        the sequence will be generated (for example [3, 5, 0]).
    spacing_range:
	a (minimum, maximum) pair (tuple), representing the min and max spacing
        between digits. Unit should be pixel.
    image_width:
        specifies the width of the image in pixels.

    Returns
    -------
    The image containing the sequence of numbers. Images should be represented
    as floating point 32bits numpy arrays with a scale ranging from 0 (black) to
    1 (white), the first dimension corresponding to the height and the second
    dimension to the width.
    """

    print("Generating an image of digit sequence {}".format(digits))
    
    gen = DigitGenerator(dataset=dataset, subset=subset)

    image = gen.sequence(digits, 
                         spacing_range=spacing_range, image_width=image_width,
                         spec=spec)
    
    if show:
        image.save_and_show(scale=scale)
    else:
        image.save(scale=scale)

    image_data = image.get_data()

    # DEBUG
    if debug:
        print("Image data:\n" +
              "  - dtype: {}\n".format(image_data.dtype) +
              "  - shape: {}\n".format(image_data.shape) +
              "  - data:  {}".format(image_data))

    return image_data

## =========================================================
## =========================================================

## fin.
