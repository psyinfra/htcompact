#!/usr/bin/env python

# Todo: test

from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()


setup(name='htcompact',
      version_format='{tag}.dev{commitcount}+{gitsha}',
      setup_requires=['setuptools-git-version'],
      description='HTCondor summariser script',
      long_description=long_description,
      author='Mathis Loevenich',
      author_email='m.loevenich@fz-juelich.de',
      packages=find_packages(),
      license='LICENSE.txt',
      python_requires='>=3.7',
      install_requires=[
            "numpy",
            "datetime",
            "configparser",
            "pandas",
            "tabulate",
            "plotille >= 3.7",
            "setuptools-git-version"
      ],
      dependency_links=[
            'https://github.com/astanin/python-tabulate.git'
      ],
      scripts=[
            'script/htcompact'
      ],
      data_files=[
            ('config', ['script/htcsetup.conf']),
            ('share/man/man1', ['man/man1/htcompact.1'])
      ],
      )
