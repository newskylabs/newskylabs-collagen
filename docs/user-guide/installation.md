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

The first points to the source distribution as generated with the
setup tools - which will be called *sdist* from now on:

- [http://newskylabs.net/deep-learning/tools/collagen/download/collagen-0.0.1.dev1.tar.gz](http://newskylabs.net/deep-learning/tools/collagen/download/collagen-tarball-0.0.1.dev1.tar.gz)

The second points to a tar archive containing the whole development
tree:

- [http://newskylabs.net/deep-learning/tools/collagen/download/collagen-tarball.0.0.1.dev1.tar.gz](http://newskylabs.net/deep-learning/tools/collagen/download/collagen-tarball.0.0.1.dev1.tar.gz)

We proceed using the second archive file containing the whole
development tree.  The steps, however, are the same for both
distribution archives.


### Unpacking

Unpack the sources:

```shell
tar zxvf collagen-tarball.0.0.1.dev1.tar.gz
```

(When installing from the setup distribution / sdist
`collagen-0.0.1.dev1.tar.gz` the command would be 
`tar zxvf collagen-0.0.1.dev1.tar.gz`)

It is necessary to set the environment variable `COLLAGEN`
to the base directory found in the unpacked sources:

```shell
COLLAGEN=/<some>/<path>/collagen.git
```

(In case of the setup distribution the base dir is named after the
current versio `collagen-0.0.1.dev1` and we would have to use
`COLLAGEN=/<some>/<path>/collagen-0.0.1.dev1`)

A number of tools as well as the future explanations refer to this
environment variable.


### Installation

Collagen can be installed with `pip` from the directory in which
Collagen has been unpacked as follows:

```shell
cd $COLLAGEN/..
pip install ./collagen.git
```

(Or `pip install ./collagen-0.0.1.dev1` in case of the sdist)


### Testing

Collagen comes with a set of unit tests.  The installation can be
verified by running them from the command line as follows:

```bash
cd $COLLAGEN
pytest
```


## Deinstallation

The deinstallation of Collagen is even simpler:

```shell
pip uninstall collagen 
```


