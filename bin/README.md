# README - Development tools

## Environment variable ```COLLAGEN```

The environment variable ```COLLAGEN``` has to be set to the `collagen.git` directory.


## Create a source distribution and uploade it

```shell
cd $COLLAGEN

bin/cdt-clean
bin/cdt-make-source-distribution 
bin/cdt-check-source-distribution
bin/cdt-upload-source-distribution
```


## Create a source directory tarball and uploade it

```shell
cd $COLLAGEN

bin/cdt-clean
bin/cdt-make-tarball
bin/cdt-check-tarball
bin/cdt-upload-tarball
```


## Generate the website and upload it

See: cdt --help

```shell
cd $COLLAGEN

cdt clean      # Clean the collagen sources.
cdt build      # Build the collagen documentation.
bin/cdt-clean-server # Clean the collagen dir on the server.
cdt deploy     # Deploy the documentation on the server.
```


## Start a local documentation preview server

See: cdt --help

```shell
cdt docs       # Run the local collagen documentation.
```


## Install / Reinstall collagen for development

See: cdt --help

```shell
cdt install    # Install collagen.
cdt reinstall  # Reinstall collagen.
```


## Get a default / overwritten collagen setting

As specified in:

  - Defaults:            $COLLAGEN/collagen/utils/default_settings.yaml
  - Overwritten values:  ~/.collagen/settings.yaml

```shell
cd $COLLAGEN

bin/cdt-get-setting SETTING-PATH
```

