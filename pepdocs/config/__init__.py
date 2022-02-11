"""Handle configuration settings in PepDocs"""

# Standard library imports
from importlib import resources

# Third party imports
from pyconfs import Configuration


def read_config(cfg_file: str) -> Configuration:
    """Read one configuration from file"""
    with resources.path(__package__, cfg_file) as cfg_path:
        return Configuration.from_file(cfg_path, name=cfg_path.stem)


#
# PepDocs configuration
#
pepdocs = read_config("pepdocs.toml")
pepdocs.vars.update(**dict(pepdocs.url.entries))
