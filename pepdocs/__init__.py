"""PepDocs, read PEPs in your console

See {url} for more information.

Current maintainers:
--------------------

{maintainers}

Version: v0.1.1
"""

# Standard library imports
from collections import namedtuple as _namedtuple
from datetime import date as _date

# PepDocs imports
from pepdocs._pepdocs import get  # noqa

# Version of PepDocs
#
# This is automatically set using the bumpversion tool
__version__ = "0.1.1"


# Homepage for PepDocs
__url__ = "https://pypi.org/project/pepdocs/"


# Authors/maintainers of PepDocs
_Author = _namedtuple("_Author", ["name", "email", "start", "end"])
_AUTHORS = [
    _Author("Geir Arne Hjelle", "geirarne@gmail.com", _date(2019, 4, 1), _date.max)
]

__author__ = ", ".join(a.name for a in _AUTHORS if a.start < _date.today() < a.end)
__contact__ = ", ".join(a.email for a in _AUTHORS if a.start < _date.today() < a.end)


# Update doc with info about maintainers
def _update_doc(doc: str) -> str:
    """Add information to doc-string

    Args:
        doc:  The doc-string to update.

    Returns:
        The updated doc-string.
    """
    # Maintainers
    maintainer_list = [
        f"+ {a.name} <{a.email}>" for a in _AUTHORS if a.start < _date.today() < a.end
    ]
    maintainers = "\n".join(maintainer_list)

    # Add to doc-string
    return doc.format(maintainers=maintainers, url=__url__)


__doc__ = _update_doc(__doc__)
