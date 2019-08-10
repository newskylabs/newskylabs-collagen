# Collagen Development Tools

A list of tools which have been helpful during the development of
Collagen:


#### Environment variable `COLLAGEN`

Most of the tools rely on the environment variable `COLLAGEN` to point
to the `collagen.git` directory.

```shell
printenv COLLAGEN

/Users/dietrich/collagen.git
```


#### The `cdt` command

The `cdt` command (short for: Collagen Development Tool) is helpful
for a number of developing tasks.  See `cdt --help` for more
information concerning the tool `cdt`:

```shell
cdt --help

Usage: cdt [OPTIONS] COMMAND [ARGS]...

  cdt - Collagen development tools.

Options:
  -V, --version  Show the version and exit.
  -h, --help     Show this message and exit.

Commands:
  build      Build the collagen documentation.
  clean      Clean the collagen sources.
  deploy     Deploy the documentation on the server.
  docs       Run the local collagen documentation...
  install    Install collagen.
  reinstall  Reinstall collagen.
```

More detailled information concerning the subcommands can be obtained
like this:

```shell
cdt deploy --help

Usage: cdt deploy [OPTIONS]

  Deploy the documentation on the server.

Options:
  -h, --help  Show this message and exit.
```


#### Install / Reinstall collagen for development

Installation:

```shell
cdt install
```

Reinstallation:

```shell
cdt reinstall
```

Using these commands Collagen is installed in development / editable
mode (`pip install --verbose -e ./collagen.git`), that is by linking
to the development tree rather than copying it.

See `cdt install --help` and `cdt reinstall --help` for more
information concerning these commands.


#### Collagen settings

To check the current value of a Collagen setting use `cdt-get-setting`.

Example:

```shell
cdt-get-setting datasets.mnist.train.images

http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
```


#### Cleanup the development tree

The development tree can be cleaned up with:

```shell
cdt clean
```

See `cdt clean --help` for more information.


#### Distribution tarballs

A source distribution tarball can be generated with the aid of `python
setup.py sdist` using the following command:

```shell
cdt-make-source-distribution
```

The command 

```shell
cdt-make-tarball
```

uses `tar zcvf` to create a tarball of the whole Collagen development
tree.


#### Creating and uploading tarballs

To create a source distribution and upload it the following sequence
of commands is helpful:

```shell
cd $COLLAGEN

bin/cdt-clean
bin/cdt-make-source-distribution 
bin/cdt-check-source-distribution
bin/cdt-upload-source-distribution
```

When the source tree should be packed with `tar` use the following sequence:

```shell
cd $COLLAGEN

bin/cdt-clean
bin/cdt-make-tarball
bin/cdt-check-tarball
bin/cdt-upload-tarball
```

