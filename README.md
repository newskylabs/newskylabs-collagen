# README

# Collagen - COLlaborative LAbs' dataset GENerator

Collagen is a tool to load, generate, augment, and process data sets
for my personal deep learning experiments.

It is work in progress - constantly changing - and the documentation
is often outdated and incomplete if existing at all.

Beside a python package Collagen contains a command line tool for
generating, saving and visualizing data points.  It is helpful for
experimenting with image augmentation pipelines and for inspecting the
characteristics of the generated images.

# Installation

## Preliminaries

Some premliminary information is helpful to know before installing the
Collagen Python package:

### Required packages

The following packages are required:

  - click >= 6.7
  - numpy >= 1.12.1
  - idx2numpy >= 1.2.1
  - Pillow >= 4.2.1
  - pathlib >= 1.0.1
  - progressbar2 >= 3.35.2
  - pyyaml >= 3.12
  - mkdocs >= 0.17.2

### Collagen settings and data cache dir

Collagen can be customized via the user settings file
`~/.collagen/settings.yaml`.  In my case it looks as follows:

```
documentation:
  server:
    host: newskylabs.net
```

A more complete version would look like this:

```
datasets:
  mnist:
    train:
      images: http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
      labels: http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
    test:
      images: http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
      labels: http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
        
data-dir: ~/.collagen/data

documentation:
  server:
    netrc: ~/.netrc
    host: newskylabs.net
    dir: /html/deep-learning/tools/collagen
```

See also the default setting file which is located at
`collagen.git/collagen/utils/default_settings.yaml`.

When the command line tool `collagen` is used for the first time with
the MNIST dataset, it will download the MNIST data from the URLs
specified in the `dataset` sections of the settings:

```
datasets:
  mnist:
    train:
      images: http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
      labels: http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
    test:
      images: http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
      labels: http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
```

The data will be stored in the Collagen data directory, which by
default is `~/.collagen/data`.  The location of the data cache
can, however, be customized in the settings file as follows:

```
data-dir: ~/some/other/data/directory
```

For more information concerning the MNIST dataset see its home page
[THE MNIST DATABASE of handwritten
digits](http://yann.lecun.com/exdb/mnist).


## Installation 

The easiest way to install Collagen is to first install some
scientific Python distribution - for example
[Anaconda](https://anaconda.org/) - and to proceed with installing the
Collagen package with `pip` as follows:


### Download

Collagen package archives can be downloaded from the following URLs:

The source distribution as generated with the setup tools:

- [http://newskylabs.net/deep-learning/tools/collagen/download/collagen.0.0.1.dev1.tar.gz](http://newskylabs.net/deep-learning/tools/collagen/download/collagen-tarball.0.0.1.dev1.tar.gz).

The whole development tree:

- [http://newskylabs.net/deep-learning/tools/collagen/download/collagen-tarball.0.0.1.dev1.tar.gz](http://newskylabs.net/deep-learning/tools/collagen/download/collagen-tarball.0.0.1.dev1.tar.gz).

We proceed using the second archive file containing the whole
development tree.  The steps, however, are the same for both
distribution archives.


### Unpacking

Unpack the sources:

```shell
tar zxvf collagen-tarball.0.0.1.dev1.tar.gz
```

It is convenient to set the environment variable `COLLAGEN`
to the base directory found in the unpacked sources:

```shell
COLLAGEN=/<some>/<parh>/collagen.git
```

A number of tools as well as the future explanations refer to this
environment variable.


### Testing

Collagen comes with a set of unit tests.  The installation can be
verified by running them from the command line as follows:

```bash
cd $COLLAGEN
pytest 
```


### Installation

Collagen can be installed with `pip` from the directory in which
Collagen has been unpacked as follows:

```shell
cd $COLLAGEN/..
pip install ./collagen.git
```


## Deinstallation

The deinstallation of Collagen is even simpler:

```shell
pip uninstall collagen 
```


# User documentation

The user documentation can be found in the subfolder
`$COLLAGEN/collagen/docs/docs/docs` or, in a published version, on the
homepage of [Collagen](http://newskylabs.net/deep-learning/tools/collagen):
[http://newskylabs.net/deep-learning/tools/collagen](http://newskylabs.net/deep-learning/tools/collagen).

The images referenced to in the following text can be found in the
directory `$COLLAGEN/collagen/docs/docs/docs/user-guide/img`.

## Getting started with Collagen


#### A simple example

Let us start with a very simple example:

```python
collagen sequence 123
```

An image representing the digit sequence `123` is generated, saved and
shown:

![collagen sequence 123](../user-guide/img/sequence.123.000.png "collagen sequence 123")

Executing the command several times results in three different images:

![collagen sequence 123](../user-guide/img/sequence.123.001.png "collagen sequence 123")<br/>
![collagen sequence 123](../user-guide/img/sequence.123.002.png "collagen sequence 123")<br/>
![collagen sequence 123](../user-guide/img/sequence.123.003.png "collagen sequence 123")

We can variate the spacing between the digits following a uniform
distribution over a range determined by two limits using the parameter
`--spacing-range <INTEGER INTEGER>`. The inteter specify the minimal
and maximal allowed space between the digits:

```python
collagen sequence 123 --spacing-range 10 100
```

![collagen sequence 123 --spacing-range 10 100](../user-guide/img/sequence.123.sr:10-100.000.png "collagen sequence 123 --spacing-range 10 100")<br/>
![collagen sequence 123 --spacing-range 10 100](../user-guide/img/sequence.123.sr:10-100.001.png "collagen sequence 123 --spacing-range 10 100")<br/>
![collagen sequence 123 --spacing-range 10 100](../user-guide/img/sequence.123.sr:10-100.002.png "collagen sequence 123 --spacing-range 10 100")

With different spaces different image width result.  If a fixed width
is required, it can be specified on the command line using the option
`--image-width Integer`:

```python
collagen sequence 123 --spacing-range 10 100 --image-width 400
```

![collagen sequence 123 --spacing-range 10 100 --image-width 400](../user-guide/img/sequence.123.sr:10-100.w:400.000.png "collagen sequence 123 --spacing-range 10 100 --image-width 400")<br/>
![collagen sequence 123 --spacing-range 10 100 --image-width 400](../user-guide/img/sequence.123.sr:10-100.w:400.001.png "collagen sequence 123 --spacing-range 10 100 --image-width 400")<br/>
![collagen sequence 123 --spacing-range 10 100 --image-width 400](../user-guide/img/sequence.123.sr:10-100.w:400.002.png "collagen sequence 123 --spacing-range 10 100 --image-width 400")

The given width, however, has to be large enough for the given number
of digits and maximal spacing.


#### Scaling the generated image

Sometimes a larger image size is desirable to make the evaluation of a
generated sequence easier.  For this purpose we can use the `--scale
INTEGER` option, which allows to specify an integer scale factor for
the image:

```python
collagen sequence 123 --scale 8
```

![collagen sequence 123 --scale 8](../user-guide/img/sequence.123.x:8.000.png "collagen sequence 123 --scale 8")


#### Specifying datasets

Beside MNIST other datasets can be used.  For testing the generation
of the sequence images the `digits5x3` dataset for example might be
helpful.  It only contains one 5x3 pixel large shape per digit and has
a grey background which makes it easy to see the spaces.  Let's
experiment with spaces between 1 and 3 pixel wide. As a size of 5
pixel is pretty small, we use a scaling factor of 10:

```python
collagen sequence 123 --dataset digits5x3 --spacing-range 1 3 --scale 10
```

![collagen sequence 123 --dataset digits5x3 --spacing-range 1 3 --scale 10](../user-guide/img/sequence.123.digits5x3.sr:1-3.x:10.000.png "collagen sequence 123 --dataset digits5x3 --spacing-range 1 3 --scale 10")

The minimal width for this kind of sequence would be `3 * 3 + 2 * 3 =
15`. What happens when we try to use a smaller image width, lets say 14?

```python
collagen sequence 123 --dataset digits5x3 --spacing-range 1 3 --image-width 14 --scale 10 

Generating an image of digit sequence 123

ERROR The given image width of 14 is too small!

  The minimum width is (3 + 3) * 3 = 15.

```

An error is thrown. 

A Width of 15, however, should be enough:


```python
collagen sequence 123 --dataset digits5x3 --spacing-range 1 3 --image-width 15 --scale 10
```

![collagen sequence 123 --dataset digits5x3 --spacing-range 1 3 --image-width 15 --scale 10](../user-guide/img/sequence.123.digits5x3.sr:1-3.w:15.x:10.001.png "collagen sequence 123 --dataset digits5x3 --spacing-range 1 3 --image-width 15 --scale 10")

The first randomly sized space is one, the second three pixel wide.
The right side of the image therefore is filled with a two pixel wide
empty space.


#### Selecting the subset of the datasets

To evaluate machine learning algorithms they are trained and evaluated
on different subsets of the datasets.  In most cases there are at
least two subsets.  MNIST, for example, is divided into a `train` and
a `test` set.  In order to select one of the two subsets the option
`--subset [train|test]` can be used:

```python
collagen sequence 0123456789 --subset test
```

![collagen sequence 0123456789 --subset test](../user-guide/img/sequence.0123456789.test.000.png "collagen sequence 0123456789 --subset test")

Of course, both subsets of MNIST consist out of a very large number of
similar shapes, so that the difference between the subsets is not
really observable for a human user, who already learned to categorize
digits.


#### The data format

Internally Collagen uses unsigned 32-bit floating point numpy arrays
to represent images.


#### Image augmentation

Finally there is a parameter for image augmentation.  This, however,
is beyond the scope of the *getting started* section and will be
explained on the [next page](../user-guide/image-augmentation.md).


#### Help

To have an overview over all possible parameter and options, use
`collagen sequence --help`:

```python
collagen sequence --help
Usage: collagen sequence [OPTIONS] SEQUENCE

  Generate an image that contains the sequence of given numbers, spaced
  randomly using an uniform distribution.

Options:
  --spacing-range <INTEGER INTEGER>...
                                  Min:max spacing between digits.
  --image-width INTEGER           Width of generated image in pixels.
  --dataset TEXT                  Dataset of digit samples.
  --subset [train|test]           Subset of the dataset.
  --spec FILENAME                 A file with a dataset specification.
  --scale INTEGER                 Integer scale factor to enlarge the images.
  --dont-show                     Do not show the generated image.
  -h, --help                      Show this message and exit.
```

# Comments etc.

If you have any comments, [please drop me a message](http://dietrich.newskylabs.net/email)!

*Copyright (c) 2019 [Dietrich Bollmann](http://dietrich.newskylabs.net/)*
