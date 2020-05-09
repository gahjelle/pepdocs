"""Handle configuration settings in PepDocs"""

# Third party imports
from pyconfs import Configuration

# Import resources, be compatible with Python 3.6
try:
    from importlib import resources
except ImportError:
    import importlib_resources as resources


def read_config(cfg_file: str) -> Configuration:
    """Read one configuration from file"""
    with resources.path(__package__, cfg_file) as cfg_path:
        return Configuration.from_file(cfg_path, name=cfg_path.stem)


#
# PepDocs configuration
#
pepdocs = read_config("pepdocs.toml")
pepdocs.vars.update(**dict(pepdocs.url.entries))
