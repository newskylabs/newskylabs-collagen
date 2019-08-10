# Implementation

In the following remarks I refer to the base directory found in the
distribution archives either as `collagen.git` or as $COLLAGEN.

### Possible parameters

```python

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

```

Beyond `digits` I made the other two required arguments optional:

- `spacing_range` has the default range `(0, 3)`;
- `image_width` is by default `0`.

When `image_width` is `0` the minimal reqired width is calculated and
applied automatically; when a fixed image width is given, it is
compared with the minimal width necessary to display the digit
sequence and separated by spaces of maximal width.  When the given
width is smaller than the minimal necessary one an error is thrown.
This is done as images in a general machine learning context only make
sense when given in a very large number, all of them the same size.
So there has to be enough place for images only using maximal spaces.
A width which is smaller therefore is not useful.

The following other optional arguments have been added:

- `dataset` - The datset to be used (default: `mnist`).
- `subset` - The subset of the dataset. Two values are possible: `train` and `test` (default: `train`).
- `augment` - A file specifying an augmentation pipeline.
- `scale` - An integer scale which can be used to enlarge generated images.
- `show` - When this flag is `False`, the generated image is not shown.
- `debug` - When `True` is passed, debug inormation is printed.

Concerning the datasets, the following are defined for the time being
(see the files in the directory `collagen.git/collagen/datasets`):

- `mnist` - The MNIST dataset from [MNIST database](http://yann.lecun.com/exdb/mnist/).
- `mnist1` - Only the first digit shapes as found in the MNIST dataset.
- `digits5x3` - A simple dataset with shapes of size 5x3 and only one shape per digit.
- `digits5x3_3` - A similar to `digits5x3`, but with three shapes per digit.

The MNIST dataset is divided into two subsets, one for training, the
other for testing.  The parameter `subset` allowes the selection of
one of the two subsets.

The function returns the calculated image encoded as an numpy array of numbers.

Internally collagen uses 32-bit floating point numpy arrays in a
domain between 0 and 1 to represent the images; 0 represents black; 1
corresponds to white. The first dimension corresponds to the height of
the image, while the second dimension represents its width.

The function can be used for image augmentation.  To augment an image
the name of a file specifying a pipeline of image augmentation
commands has to be passed via the `augment` parameter.

When very small datasets are used - for example one of `digits5x3` and
`digits5x3_3` - the generated images would be very small.  Therefore
the `scale` parameter allows to speciby an integer scaling factor.

Sometimes it is not desirable to show the generated image.  In this
case `False` can be passed for the parameter `show`.

Finally a `debug` parameter can be used to display information
concerning the returned image data: its type, shape and the data
itself.


### The implementation

First a simple message concerning the generated digit sequence is
printed to stdout:

```python
    print("Generating an image of digit sequence {}".format(digits))
```

After the class `DigitGenerator` is instantiated.  This class is
implements the main functionality of the image generator:
   
```python
    gen = DigitGenerator(dataset=dataset, subset=subset)
```

The `DigitGenerator` is implemented in the file
`collagen.git/collagen/generators/digit_generator.py`. Its instance
allows the genration of the image sequences as follows:

```python
    image = gen.sequence(digits, 
                         spacing_range=spacing_range, image_width=image_width,
                         augment=augment)
```

After the image has been generated, it is saved and shown:

```python

    image.save_and_show(scale=scale)

```

As the data should be returned by `collagen_sequence()`, it is then
retrived from the image instance. 

```python
    image_data = image.get_data()
```

When `True` is passed for the debug parameter, information about this data is 
printed to stdout:  its data type, shape and finally the data itself:

```python

    # DEBUG
    if debug:
        print("Image data:\n" +
              "  - dtype: {}\n".format(image_data.dtype) +
              "  - shape: {}\n".format(image_data.shape) +
              "  - data:  {}".format(image_data))

```

Finally the image data is returned.

```python
    return image_data
```

