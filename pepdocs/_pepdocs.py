"""Download and read PEPs"""

# Standard library imports
import pathlib

# Third party imports
import requests

# PepDocs imports
from pepdocs.config import pepdocs as CFG


def get(pep_number: int, use_cache: bool = True) -> str:
    """Get the text of one PEP"""
    pep_path = download_pep(pep_number, use_cache=use_cache)
    return pep_path.read_text()


def download_pep(pep_number: int, use_cache: bool = True) -> pathlib.Path:
    """Download a PEP to cache"""

    # Return immediately if PEP exists in cache
    pep_path = CFG.path.replace("cache", pep_number=pep_number, converter="path")
    if use_cache and pep_path.exists():
        return pep_path

    # Download PEP from available URLs
    for format in CFG.url.pep.entry_keys:
        pep_url = CFG.url.pep.replace(format, pep_number=pep_number)
        print(f"Downloading {pep_url}")
        pep_request = requests.get(pep_url)

        if pep_request:
            pep_path.parent.mkdir(parents=True, exist_ok=True)
            pep_path.write_text(pep_request.text)
            return pep_path

    # PEP was not found
    raise FileNotFoundError(f"PEP {pep_number} was not found")
