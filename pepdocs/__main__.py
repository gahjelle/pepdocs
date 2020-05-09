"""PepDocs, read PEPs in your console

Given a PEP_NUMBER, the PEP will be downloaded and printed to your screen. PEPs
are cached, so that they are only downloaded once.

See {url} for more information.

\b
Current maintainers:
--------------------

\b
{maintainers}

Version: v0.1.1
"""

# Standard library imports
import builtins

# Third party imports
import typer

# PepDocs imports
import pepdocs


def main() -> None:
    """Dispatch to typer"""
    get_pep_cli.__doc__ = pepdocs._update_doc(__doc__)
    typer.run(get_pep_cli)


def get_pep_cli(
    pep_number: int,
    cache: bool = typer.Option(True, help="Read from cache if it's already downloaded"),
    print: bool = typer.Option(True, help="Print PEP to console"),
) -> None:
    """Get one PEP and print it to the console"""
    try:
        pep_text = pepdocs.get(pep_number, use_cache=cache)
    except FileNotFoundError as err:
        raise SystemExit(err)

    if print:
        builtins.print(pep_text)
