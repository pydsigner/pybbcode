#! /usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import sys

#############################################################################
### Main setup stuff
#############################################################################

def main():
    
    # perform the setup action
    import pybbcode
    setup_args = {
        'script_args': sys.argv[1:] if len(sys.argv) > 1 else ['install'],
        'name': "pybbcode",
        'version': pybbcode.__version__,
        'description': 'PyBBCode -- A light yet powerful BB Code parser.',
        'long_description': 'PyBBCode -- A light yet powerful BB Code parser.',
        'author': "Daniel Foerster/pydsigner",
        'author_email': "pydsigner@gmail.com",
        'packages': ['pybbcode'],
        'license': 'LGPLv3',
        'url': "http://github.com/pydsigner/pybbcode",
        'classifiers': [
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Programming Language :: Python',
        ]}
    setup(**setup_args)

if __name__ == '__main__':
    main()
