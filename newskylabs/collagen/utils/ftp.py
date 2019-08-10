"""newskylabs/collagen/utils/ftp.py:

FTP tools.

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/02/24"

import os
import netrc
import ftplib

## =========================================================
## Class ftp
## ---------------------------------------------------------

class FTP(object):
    """
    An FTP class adapted to collagen's needs.
    """

    def __init__(self, host, netrc_file='~/.netrc', verbose=False):
        """
        """
        self.host = host
        self.netrc_file = os.path.expanduser(netrc_file)
        self._verbose = verbose

    def msg(self, text):
        """
        Print TEXT to stdout when in verbose mode.
        """
        if self._verbose:
            print('FTP: ' + text)

    def login(self):
        """
        """
        self.netrc = netrc.netrc(self.netrc_file)

        login, account, password = self.netrc.authenticators(self.host)
        self.msg("Logging into {} as {}".format(self.host, login))
        self._session = ftplib.FTP(self.host, login, password)

    def pwd(self):
        """
        """
        pwd = self._session.pwd()
        self.msg("pwd: " + pwd)
        return pwd

    def cd(self, directory):
        """
        """
        self.msg("cd " + directory)
        self._session.cwd(directory)

    def ls(self, directory):
        """
        """
        self.msg("ls " + directory)
        self._session.nlst(directory)

    def mkdir(self, directory):
        """
        """
        self.msg("mkdir " + directory)
        self._session.mkd(directory)

    def ensure_dir(self, directory):
        """
        """
        self.msg("ensure_dir " + directory)
        self._ensure_dir(directory)

    def _ensure_dir(self, directory):
        """
        """
        try:
            self._session.nlst(directory)

        except ftplib.error_temp:

            # First ensure the parent dir
            parentdir = os.path.dirname(directory)
            self._ensure_dir(parentdir)

            # Then make the dir itself
            self._session.mkd(directory)

    def ensure_cd_dir(self, directory):
        """
        """
        self.msg("ensure_cd_dir " + directory)
        self._ensure_dir(directory)
        self.cd(directory)

    def put(self, filename):
        """Upload FILE."""
        self.msg("put " + filename)
        self._session.storbinary('STOR ' + filename, open(filename, 'rb'))

    def bye(self):
        """Logout."""
        self.msg("quit")
        self._session.quit()

## =========================================================
## =========================================================

## fin.
