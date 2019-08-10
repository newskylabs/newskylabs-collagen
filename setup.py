## =========================================================
## Copyright 2019 Dietrich Bollmann
## 
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
## 
##      http://www.apache.org/licenses/LICENSE-2.0
## 
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
## ---------------------------------------------------------

"""setup.py:

Setup file for the NewSkyLabs Python project collagen.

"""

import setuptools 
import codecs
import os

## =========================================================
## Setup utilities
## ---------------------------------------------------------

def read_file(*parts):
    """
    Read a file and return its content
    """
    package_dir = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(package_dir, *parts), 'r') as fp:
        return fp.read()

def find_packages(namespace):
    """
    Return a list of all Python packages defined in the 'namespace'
    directory
    """
    return [
        '{}.{}'.format(namespace, package) 
        for package in setuptools.PackageFinder.find(where=namespace)
    ]

## =========================================================
## Setup
## ---------------------------------------------------------

namespace    = 'newskylabs'
subnamespace = 'collagen'

# Load the package metadata 
exec(read_file(namespace, subnamespace, '__about__.py'))

# Read the long description
long_description = read_file('README.md')

# Find the list of packages
packages = find_packages(namespace)

# Setup package
setuptools.setup(
    name=__package_name__,
    version=__version__,
    description=__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=__author__,
    author_email=__email__,
    license=__license__,
    url=__url__,
    keywords='deep learning, data augmentation, data generation.',
    packages=packages,
    entry_points={
        'console_scripts': [
            'collagen = newskylabs.collagen.__main__:cli',
            'cdt = newskylabs.collagen.scripts.cdt:cli',
        ]
    },
    package_data={
        'newskylabs.collagen.settings': ['default_settings.yaml'],
    },
    include_package_data=True,
    scripts=[
        # TODO: Generate this list dynamically
        'bin/cdt-check-source-distribution',
        'bin/cdt-check-tarball',
        'bin/cdt-clean',
        'bin/cdt-collagen',
        'bin/cdt-get-setting',
        'bin/cdt-install',
        'bin/cdt-make-source-distribution',
        'bin/cdt-make-tarball',
        'bin/cdt-reinstall',
        'bin/cdt-clean-server',
        'bin/cdt-upload-source-distribution',
        'bin/cdt-upload-tarball',
    ],
    install_requires=[
        'click>=6.7',
        'numpy>=1.12.1',
        'idx2numpy>=1.2.1',
        'mkdocs>=0.17.2',
        'matplotlib>=2.2.0',
        'Pillow>=5.0.0',
        'pathlib>=1.0.1',
        'progressbar2>=3.39.2',
        'pyyaml>=3.12',
        'scikit-image>=0.13.0',
        'scipy>=1.0.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
        'Operating System :: OS Independent',
    ],
    platforms=['Posix', 'Unix', 'Linux', 'MacOS X', 'Windows'],
    setup_requires=['setuptools-markdown'],
    # Install unzipped to be able to use the .md and .yaml files
    zip_safe=False
)

## =========================================================
## =========================================================

## fin.
