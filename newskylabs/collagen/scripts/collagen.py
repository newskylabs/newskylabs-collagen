"""newskylabs/collagen/scripts/collagen.py:

Definition of the `collagen` script.

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/23"

import os
import click

from newskylabs.collagen.commands.grid import collagen_grid
from newskylabs.collagen.commands.sequence import collagen_sequence
from newskylabs.collagen.commands.dataset import collagen_dataset
from newskylabs.collagen.utils.generic import get_version_long

## =========================================================
## Group:
## ---------------------------------------------------------

@click.group(context_settings={'help_option_names': ['-h', '--help']})
# Version options: -V, --version
@click.version_option(get_version_long(), '-V', '--version')
def cli():
    """
    Collagen - Collaborative image generator.
    """
    
## =========================================================
## Command: sequence
## ---------------------------------------------------------

# Help texts
image_spacing_range_help = "Min:max spacing between digits."
image_width_help = "Width of generated image in pixels."
sequence_dataset_help = "Dataset of digit samples."
sequence_subset_help = "Subset of the dataset."
sequence_spec_help = "A file with a dataset specification."
sequence_scale_help = "Integer scale factor to enlarge the images."
sequence_dont_show_help = "Do not show the generated image."

@cli.command(name="sequence")
@click.argument('sequence', type=str)
@click.option('--spacing-range', default=(0, 3), type=(int, int),
              help=image_spacing_range_help)
@click.option('--image-width', default=0, help=image_width_help)
@click.option('--dataset', default='mnist', help=sequence_dataset_help)
@click.option('--subset', default='train', type=click.Choice(['train', 'test']), 
              help=sequence_subset_help)
@click.option('--spec', type=click.File('rb'), help=sequence_spec_help)
@click.option('--scale', default=1, help=sequence_scale_help)
@click.option('--dont-show', is_flag=True, help=sequence_dont_show_help)

def command_sequence(sequence, spacing_range, image_width, dataset, subset, spec, scale, dont_show):
    """Generate an image that contains the sequence of given numbers,
    spaced randomly using an uniform distribution.

    """
    collagen_sequence(sequence, 
                      spacing_range=spacing_range, image_width=image_width, 
                      dataset=dataset, subset=subset,
                      spec=spec, scale=scale, show=(not dont_show))

## =========================================================
## Command: grid
## ---------------------------------------------------------

# Help texts
grid_width_help = "The width of the grid."
grid_height_help = "The height of the grid."
grid_dataset_help = "Dataset of digit samples."
grid_subset_help = "Subset of the dataset."
grid_spec_help = "A file with a dataset specification."
grid_scale_help = "Integer scale factor to enlarge the images."
grid_dont_show_help = "Do not show the generated image."

@cli.command(name="grid")
@click.argument('digit')
@click.option('--width', default=25, help=grid_width_help)
@click.option('--height', default=5, help=grid_height_help)
@click.option('--dataset', default='mnist', help=grid_dataset_help)
@click.option('--subset', default='train', type=click.Choice(['train', 'test']), 
              help=grid_subset_help)
@click.option('--spec', type=click.File('rb'), help=grid_spec_help)
@click.option('--scale', default=1, help=grid_scale_help)
@click.option('--dont-show', is_flag=True, help=grid_dont_show_help)

def command_grid(digit, height, width, dataset, subset, spec, scale, dont_show):
    """Generate an image displaying a grid of randomly selected shapes for
    DIGIT.

    """

    collagen_grid(digit, 
                  height=height, width=width, 
                  dataset=dataset, subset=subset,
                  spec=spec, scale=scale, show=(not dont_show))

## =========================================================
## Command: dataset
## ---------------------------------------------------------

@cli.command(name="dataset")
@click.argument('dataset_spec')

def command_dataset(dataset_spec):
    """Generate a dataset conformimg to the given dataset specification
    DATASET_SPEC.

    """

    collagen_dataset(dataset_spec)

## =========================================================
## Main
## ---------------------------------------------------------
 
if __name__ == '__main__':
    cli()

## =========================================================
## =========================================================

## fin.
