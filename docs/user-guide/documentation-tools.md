# Collagen Documentation Tools


The Collagen documenation can be found in the following directory:

- `$COLLAGEN/collagen/docs/docs/docs`

A list of tools are helpful when working on the documentation:


## Generate a local documentation preview server

When editing the documentation a local documentation server is very
helpull as it updates the rendered pages automatically after their
sources have been edited:

```shell
cdt docs
```

See `cdt docs --help` for more information.


## The `documenation` section in the user settings

The documentation of Collagen can be automatically uploaded to a
server via FTP.  The necessary information is specified in the
`documenation` section of the settings:

```
documentation:
  server:
    netrc: ~/.netrc
    host: newskylabs.net
    dir: /html/deep-learning/tools/collagen
```

The credentials for the server FTP account have to be stored in the
`netrc` file, whoms location is stored in the settings under the path
`documentation.server.netrc`.

The command for uploading the documentation is as follows:

```shell
cdt deploy
```

See `cdt deploy --help` for more information.


## Generate the website and upload it

The following sequence of commands is helpful for generating a static
version of the documentation and for uploading it to the documentation
server:

```shell
cdt clean             # Clean the collagen sources.
cdt build             # Build the collagen documentation.
bin/cdt-clean-server  # Clean the collagen dir on the server.
cdt deploy            # Deploy the documentation on the server.
```

See `cdt SUBCOMMAND --help` for more information concerning these
commands.


## Erasing the remote documentation

The uploaded Collagen documentation can be deleted again with the
following command:

```shell
cdt-clean-server
```


## A wrapper for collagen for documentation purpose

This wrapper helps to generate images and markdown code for the
documentation.

```shell
cdt-collagen
```

#### Example:

Preparation:

```shell
alias clg=cdt-collagen
export COLLAGEN_IMG_DIR=/some/path/img
```

Now shorted commands can be used.  The command `clg s 123` is
translated to `collagen sequence 123`.  It automatically generates an
unused name for the image which encodes the used parameters and copies
them to the `COLLAGEN_IMG_DIR` directory. When, for example, images
with the names `sequence.123.000.png` and `sequence.123.001.png`
already exists in the image directory, the name `sequence.123.002.png`
is used. Further markdown code is generated which can be copy-pasted
directly into the documentation:

    clg s 123
    
    >>> Generating image: collagen sequence 123
    >>> generated image name: sequence.123.2018-02-28.17-51-44.png
    >>> open sequence.123.2018-02-28.17-51-44.png
    >>> next image name: sequence.123.002.png
    >>> cp sequence.123.2018-02-28.17-51-44.png /some/path/img/sequence.123.002.png
    
    ```shell
    collagen sequence 123
    ```
    
    ![collagen sequence 123](img/sequence.123.002.png "collagen sequence 123")

The generated markdown code results in the following formatting:

```python
collagen sequence 123
```

![collagen sequence 123](img/sequence.123.004.png "collagen sequence 123")

