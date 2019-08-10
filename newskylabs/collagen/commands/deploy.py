"""newskylabs/collagen/commands/deploy.py:

Command deploy: Deploy the Collagen documentation via ftp on the host
specified in the settings file.

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/24"

import os
from os.path import isfile, isdir, join
from newskylabs.collagen.utils.settings import get_setting
from newskylabs.collagen.utils.generic import get_package_dir
from newskylabs.collagen.utils.ftp import FTP

## =========================================================
## Utilities
## ---------------------------------------------------------

def _listdir():
    """List files and directories in the current directory."""

    allf  = [a for a in os.listdir('.')]
    files = [f for f in allf if isfile(f)]
    dirs  = [d for d in allf if isdir(d)]

    return files, dirs

## =========================================================
## Main entry points
## ---------------------------------------------------------

class FTP_upload(object):
    """
    A class to recursivly upload files to an FTP server.
    """
    
    def __init__(self, host, netrc_file, local_dir, remote_dir, verbose=False, debug=False):
        """
        """

        self._verbose = verbose
        self._debug = debug

        self.msg("")
        self.msg("Upload settings:")
        self.msg("")
        self.msg("  - netrc_file:" + netrc_file)
        self.msg("  - host:      " + host)
        self.msg("  - local_dir: " + local_dir)
        self.msg("  - remote_dir:" + remote_dir)
        self.msg("")
        
        # Open FTP session
        self.msg("Opening connection to " + host)
        self._session = FTP(host, netrc_file, verbose=self._debug)
        self._session.login()
    
        # Change to the local and remote directories
        os.chdir(local_dir)
        self._session.ensure_cd_dir(remote_dir)
        
        lpath     = local_dir
        rpath     = remote_dir
        relpath   = ''
        directory = ''
        self._upload_recursively(lpath, rpath, relpath, directory)

        # Close FTP session
        self._bye()

    def msg(self, text):
        """
        """
        if self._debug:
            print('FTP_upload: ' + text)
        elif self._verbose:
            print(text)

    def debug(self, text):
        """
        """
        if self._debug:
            print('FTP_upload: ' + text)

    def _upload_recursively(self, lpath, rpath, relpath, directory):
        """Recursively upload the given directory."""

        lpath = os.path.join(lpath, directory)     # local path
        rpath = os.path.join(rpath, directory)     # remote path
        relpath = os.path.join(relpath, directory) # relative path

        os.chdir(lpath)
        self._session.ensure_cd_dir(rpath)

        self.debug('local dir: ' + os.getcwd())
        self.debug('remote dir:' + self._session.pwd())

        files, dirs = _listdir()

        for f in files:
            self.msg("upload " + os.path.join(relpath, f))
            self._session.put(f)

        for directory in dirs:
            self._upload_recursively(lpath, rpath, relpath, directory)

    def _bye(self):
        """
        """
        self._session.bye()
        self.msg("done.")

## =========================================================
## Command: deploy
## ---------------------------------------------------------

def command():

    # Get the mkdocs collagen documentation directory
    docs_package_dir = get_package_dir('collagen.docs')
    mkdocs_site_dir = os.path.join(docs_package_dir, 'docs/site')

    # Upload settings
    netrc_file = os.path.expanduser(get_setting('documentation.server.netrc'))
    host       = os.path.expanduser(get_setting('documentation.server.host'))
    local_dir  = mkdocs_site_dir
    remote_dir = os.path.expanduser(get_setting('documentation.server.dir'))
    
    # Upload
    verbose = True
    debug   = False
    FTP_upload(host, netrc_file, local_dir, remote_dir, verbose=verbose, debug=debug)

## =========================================================
## =========================================================

## fin.
