"""PepDocs, read PEPs in your console

Given a PEP_NUMBER, the PEP will be downloaded and printed to your screen. PEPs
are cached, so that they are only downloaded once.

See {url} for more information.

\b
Current maintainers:
--------------------

\b
{maintainers}

Version: v0.3.0
"""

# Third party imports
import typer

# PepDocs imports
import pepdocs
from pepdocs.config import pepdocs as CFG


def main() -> None:
    """Dispatch to typer"""
    get_pep_cli.__doc__ = pepdocs._update_doc(__doc__)
    typer.run(get_pep_cli)


def get_pep_cli(
    pep_numbers: list[int],
    print: bool = typer.Option(True, help="Print PEP to console"),
    cache: bool = typer.Option(
        True, help="Read PEP from cache if it's already downloaded"
    ),
    markdown: bool = typer.Option(
        False, "--markdown", "-m", help="Convert PEP to Markdown"
    ),
    browser: bool = typer.Option(
        False, "--web-browser", "-w", help="Open PEP in web browser"
    ),
    save: bool = typer.Option(False, "--save-to-file", "-s", help="Save PEP to file"),
    show_cache_location: bool = typer.Option(
        False, "--locate-cache", help="Show location of cache"
    ),
) -> None:
    """Get one PEP and print it to the console"""
    if show_cache_location:
        cache_dir = CFG.path.replace("cache", pep_number=0, converter="path").parent
        typer.secho(str(cache_dir), fg=typer.colors.GREEN)
        raise typer.Exit()

    for pep_number in pep_numbers:
        try:
            pep_text = pepdocs.get(pep_number, use_cache=cache, as_markdown=markdown)
        except FileNotFoundError as err:
            typer.secho(str(err), fg=typer.colors.RED)
        else:
            if browser:
                pepdocs.open_browser(pep_number)
            elif save:
                path = CFG.path.save.replace(
                    "markdown" if markdown else "rst",
                    pep_number=pep_number,
                    converter="path",
                )
                path.write_text(pep_text)
                typer.secho(f"Wrote to {path}", fg=typer.colors.GREEN)
            elif print:
                typer.echo(pep_text)
