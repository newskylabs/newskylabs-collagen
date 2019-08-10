"""newskylabs/collagen/utils/conversion.py:

Data conversion utilities.

Formats:

    MNIST format:

    - uint8 numpy arrays
    - domain between 0 and 255
    - 0 represents white (background), 255 represents black (foreground)
    - the first dimension corresponding to the height
    - the second dimension to the width
    
    Collagen internal format:
    
    - floating point 32bits numpy arrays 
    - domain between 0.0 and 1.0
    - 0.0 represents black; 1.0 corresponds to white
    - the first dimension corresponding to the height
    - the second dimension to the width
"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/20"

import numpy as np

def convert_mnist2collagen(data, debug=False):
    """Convert the data from MNIST format to Collagen internal format.

    MNIST format:

    - uint8 numpy arrays
    - domain between 0 and 255
    - 0 represents white (background), 255 represents black (foreground)
    - the first dimension corresponding to the height
    - the second dimension to the width
    
    Collagen internal format:
    
    - floating point 32bits numpy arrays 
    - domain between 0.0 and 1.0
    - 0.0 represents black; 1.0 corresponds to white
    - the first dimension corresponding to the height
    - the second dimension to the width
    """

    # DEBUG
    if debug:
        print(">>> Before conversion (mnist format):")
        print("data:", data)
        print("type(data):", type(data))
        print("data.dtype:", data.dtype)
        print("data.shape:", data.shape)
    
    # Convert 255-0 to 0-255
    data = 255 - data

    # Convert 0-255 to 0-1
    data = data / 255.0

    # Convert to float32
    data = data.astype(np.float32)
        
    # DEBUG
    if debug:
        print(">>> After conversion (collagen format):")
        print("data:", data)
        print("type(data):", type(data))
        print("data.dtype:", data.dtype)
        print("data.shape:", data.shape)
    
    return data

# fin.
