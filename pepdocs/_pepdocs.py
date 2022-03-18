"""Download and read PEPs"""

# Standard library imports
import pathlib
import re
import webbrowser

# Third party imports
import requests
import rst_to_myst

# PepDocs imports
from pepdocs.config import pepdocs as CFG


def get(pep_number: int, use_cache: bool = True, as_markdown: bool = False) -> str:
    """Get the text of one PEP"""
    pep_rst = download_pep(pep_number, use_cache=use_cache).read_text()
    return convert_to_markdown(pep_rst) if as_markdown else pep_rst


def open_browser(pep_number: int) -> None:
    """Open the PEP in the default web browser"""
    pep_url = CFG.url.replace("pep_web", pep_number=pep_number)
    webbrowser.open_new_tab(pep_url)


def download_pep(pep_number: int, use_cache: bool = True) -> pathlib.Path:
    """Download a PEP to cache"""

    # Return immediately if PEP exists in cache
    pep_path = CFG.path.replace("cache", pep_number=pep_number, converter="path")
    if use_cache and pep_path.exists():
        return pep_path

    # Download PEP from available URLs
    for format in CFG.url.pep.entry_keys:
        pep_url = CFG.url.pep.replace(format, pep_number=pep_number)
        if pep_request := requests.get(pep_url):
            pep_path.parent.mkdir(parents=True, exist_ok=True)
            pep_path.write_text(pep_request.text)
            return pep_path

    # PEP was not found
    raise FileNotFoundError(f"PEP {pep_number} was not found")


def convert_to_markdown(pep_rst: str) -> str:
    """Convert a PEP text from ReStructuredText to Markdown

    Assume the top of the PEP consists of meta information
    """
    header, _, text_rst = pep_rst.partition("\n\n")
    headers = {
        k: v.strip()
        for line in re.sub(r"\n +", " ", header).split("\n")
        for (k, _, v) in [line.partition(":")]
    }
    title_md = f"# PEP {headers.pop('PEP', 'X')} - {headers.pop('Title', 'Untitled')}"
    headers_md = "\n".join(f"- {k}: {v}" for k, v in headers.items())
    text_md = rst_to_myst.mdformat_render.rst_to_myst(text_rst, use_sphinx=False).text

    return "\n\n".join((title_md, headers_md, text_md))
