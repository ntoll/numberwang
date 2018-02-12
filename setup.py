#!/usr/bin/env python3
from setuptools import setup
from numberwang import __version__


with open('README.rst') as f:
    readme = f.read()
with open('CHANGES.rst') as f:
    changes = f.read()


setup(
    name='numberwang',  # The name of the package
    version=__version__,  # The version number for the package
    # A short description of the package
    description='A module / utility to determine if something is numberwang.',
    # A long description (displayed on PyPi's page for the package)
    long_description=readme + '\n\n' + changes,
    author='Nicholas H.Tollervey',  # The maintainer
    author_email='ntoll@ntoll.org',  # Their email
    url='https://github.com/ntoll/numberwang',  # The package's website
    py_modules=['numberwang', ],  # The Python modules to include
    license='MIT',  # The license type
    include_package_data=True,
    classifiers=[  # Helpful classifications / metadata
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Education',
    ],
    entry_points={  # Links the "numberwang" command with a function to call
        'console_scripts': ['numberwang=numberwang:main'],
    }
)
