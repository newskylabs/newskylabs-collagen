"""newskylabs/collagen/graphics/image.py:

An Image class to be helpful for sequence generation and image
augmenation.

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/21"

import numpy as np
import warnings
from PIL import Image as PImage
from skimage import img_as_ubyte

## =========================================================
## Utilities
## ---------------------------------------------------------
        
def _make_pil_image(image, scale=1):
    """
    Convert the image to a PIL image.

    PIL is used to display and save images.

    Parameters
    ----------
    image:
	A numpy uint8 array encoding an image.
        0 corresponds to black; 255 to white.
    scale:
	A scaling factor to control the size of the image.

    Returns
    -------
    The image converted to a PIL image.
    """

    # DEBUG
    #| print("DEBUG image.dtype:", image.dtype)
    #| print("DEBUG image.shape:", image.shape)

    # Converting the image to PIL
    if image.dtype == np.uint8:
        pimage = PImage.fromarray(image, mode='L')

    elif image.dtype == np.float64:

        # Ensure that the values are in the range 0 - 1
        image = np.clip(image, 0.0, 1.0)

        # Convert from floag to ubyte
        # while suppressing the warning:
        #   UserWarning: Possible precision loss when converting from float64 to uint8
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            image = img_as_ubyte(image)
        
        l = len(image.shape)

        if l == 2:
            pimage = PImage.fromarray(image, mode='L')

        elif l == 3 and image.shape[2] == 3:
            pimage = PImage.fromarray(image, mode='RGB')

        else:
            # Invalid image type
            msg = 'Invalid combination of image dtype {} and image shape {}!'.format(image.dtype, image.shape)
            raise TypeError(msg)

    else:
        # Invalid image type
        msg = 'Invalid image dtype: {}!'.format(image.dtype)
        raise TypeError(msg)


    # Scale the image:
    newsize = pimage.size[0] * scale, pimage.size[1] * scale
    pimage = pimage.resize(newsize)

    # and finally return it
    return pimage

def image_grid(img_generator, height, width):
    """
    Generate a grid of images.
    
    The images are generated by img_generator()
    and must be of the same size.
    """

    # Getting the size of the generated images
    image = img_generator()
    dtype     = image.data.dtype
    imgheight = image.data.shape[0]
    imgwidth  = image.data.shape[1]

    # Calculating the size of the image grid
    mheight = height * imgheight
    mwidth  = width  * imgwidth

    # Creating the result image
    l = len(image.data.shape)
    if l == 2:
        image = Image((mheight, mwidth))

    elif l == 3:
        imgdepth = image.data.shape[2]
        image = Image((mheight, mwidth, imgdepth))

    else:
        # Invalid image dimensions
        msg = 'Invalid image dimensions: {}!'.format(image.data.shape)
        raise TypeError(msg)

    # Filling the grid with the generated images
    y = 0
    for i in range(height):
        x = 0
        for j in range(width):
            # print("DEBUG ({}, {}) : ({}, {})".format(i, j, y, x))
            subimage = img_generator()
            image.set_subimage(y, x, subimage)
            x += imgwidth
        y += imgheight
        
    return image

## =========================================================
## class Image
## ---------------------------------------------------------

class Image:

    def __init__(self, *args):
        self._set(args)
        
        self._name = 'image'

    def set(self, *args):
        self._set(args)
        
    def _set(self, args):

        ok = False

        nargs = len(args)
        if nargs == 1:

            arg = args[0]

            if isinstance(arg, (list, np.ndarray)):
                # image([[1, 2, 3, 4], ...])         # greyvalues
                # image([[[r1, g1, b1], ...], ...])  # rgb colours

                array = arg
                if isinstance(array, list):
                    array = np.array(array)
                self.shape = array.shape
                self.data = array
                ok = True

            elif isinstance(arg, tuple):

                l = len(arg)

                if l == 2 \
                   and np.issubdtype(type(arg[0]), np.integer) \
                   and np.issubdtype(type(arg[1]), np.integer):

                    # arg: (height, width)
                    self.shape = arg
                    self.data = np.zeros(arg)
                    ok = True
            
                elif l == 3 \
                   and np.issubdtype(type(arg[0]), np.integer) \
                   and np.issubdtype(type(arg[1]), np.integer) \
                   and np.issubdtype(type(arg[2]), np.integer):

                    # arg: (height, width, depth)
                    self.shape = arg
                    self.data = np.zeros(arg)
                    ok = True
            
        if not ok:
            
            # Invalid parameter list
            msg = 'Invalid argument: {}. '.format(args) \
                  + 'Either the image size or a numpy array has to be provided.'
            raise TypeError(msg)

    def fill(self, value):
        """
        Fill an image with a scalar value.
        """
        self.data.fill(value)

    def __str__(self):
        return 'image{self.shape}'.format(self=self)

    def set_subimage(self, y, x, subimage):

        # subimage has to be an image
        if not isinstance(subimage, Image):
            msg = 'Invalid argument: {}. '.format(args) \
                  + 'subimage has to be of type image!'
            raise TypeError(msg)

        self.data[y:y+subimage.shape[0], x:x+subimage.shape[1]] = subimage.data

    def set_name(self, name):
        """
        Set the name of the image.
        """
        self._name = name
            
    def get_name(self):
        """
        Return the name of the image.
        """
        return self._name

    def get_data(self):
        """
        Return the image data.
        """

        data = self.data

        return data

    def show(self, scale=1):
        """
        Show an image.
    
        PIL is used to display images.
    
        Parameters
        ----------
        scale:
    	    An integer scaling factor to control the size of the image.
    
        Returns
        -------
        The image converted to PIL.
        """
        
        # Convert the image to a PIL image
        pimage = _make_pil_image(self.data, scale=scale)
    
        # and finally display it
        pimage.show()
        
        # Return the PIL image
        return pimage
        
    def save(self, name='image', scale=1):
        """
        Save an image.
    
        PIL is used to save images.
    
        Parameters
        ----------
        name:
    	    Name used to save the image
        scale:
      	    An integer scaling factor to control the size of the image.
    
        Returns
        -------
        The image converted to PIL.
        """

        # The name
        if name == 'image':
            name = '{}.png'.format(self._name)
        
        # Convert the image to a PIL image
        pimage = _make_pil_image(self.data, scale=scale)
    
        # And finally save it
        print("Saving image as: {}".format(name))
        pimage.save(name)

        # Return the PIL image
        return pimage
        
    def save_and_show(self, name='image', scale=1):
        """
        Save and show an image.
    
        PIL is used to display images.
    
        Parameters
        ----------
        name:
    	    Name used to save the image
        scale:
      	    A scaling factor to control the size of the image.
    
        Returns
        -------
        The image converted to PIL.
        """
        
        # The name
        if name == 'image':
            name = '{}.png'.format(self._name)
        
        # Convert the image to a PIL image
        pimage = _make_pil_image(self.data, scale=scale)
    
        # Save it
        print("Saving image as: {}".format(name))
        pimage.save(name)
        
        # And finally display it
        pimage.show()

        # Return the PIL image
        return pimage
        
    def dump(self):
        """
        Dump the image data.
        """
        print(self.data)

## =========================================================
## =========================================================

## fin.
