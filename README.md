# PepDocs

_Read PEPs in your console_

[![v0.1.2](https://img.shields.io/pypi/v/pepdocs.svg)](https://pypi.org/project/pepdocs/)
[![Python versions](https://img.shields.io/pypi/pyversions/pepdocs.svg)](https://pypi.org/project/pepdocs/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Interrogate](https://raw.githubusercontent.com/gahjelle/pepdocs/master/interrogate_badge.svg)](https://interrogate.readthedocs.io/)
[![CircleCI](https://circleci.com/gh/gahjelle/pepdocs.svg?style=shield)](https://circleci.com/gh/gahjelle/pepdocs)


## Installing PepDocs

PepDocs is available at [PyPI](https://pypi.org/project/pepdocs/). You can install it using Pip:

    $ python -m pip install pepdocs


## Using PepDocs

To read a PEP in your console, use the `pep` command line command:

    $ pep 8

Use `pep --help` to see available options.

You can also call PepDocs from your own scripts. In that case, use `pepdocs.get()`:

    import pepdocs
    pep8 = pepdocs.get(8)


## Installing From Source

You can always download the [latest version of PepDocs from GitHub](https://github.com/gahjelle/pepdocs). PepDocs uses [Flit](https://flit.readthedocs.io/) as a setup tool.

To install PepDocs from the downloaded source, run Flit:

    $ python -m flit install --deps production

If you want to change and play with the PepDocs source code, you should install it in editable mode:

    $ python -m flit install --symlink
