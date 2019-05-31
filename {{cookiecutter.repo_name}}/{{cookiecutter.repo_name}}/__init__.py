"""{{ cookiecutter.project_name }} - {{ cookiecutter.project_short_description }}

See `{exe} --help` for information about how to use the program.


Current maintainers:
--------------------

{maintainers}

Version: {version}
"""

# Standard library imports
from collections import namedtuple as _namedtuple
from datetime import date as _date
import re as _re

# Version of {{ cookiecutter.project_name }}
__version__ = "{{ cookiecutter.version }}"  # This is automatically set using the bumpversion tool


# Authors of Midgard.
_Author = _namedtuple("_Author", ["name", "email", "start", "end"])
_AUTHORS = [
    # Add list of maintainers, change _date.max if they leave the project
    _Author(
        "{{ cookiecutter.your_name }}",
        "{{ cookiecutter.your_email }}",
        _date(2019, 6, 1),
        _date.max,
    ),
    # Hall of fame
]

__author__ = ", ".join(a.name for a in _AUTHORS if a.start < _date.today() < a.end)
__contact__ = ", ".join(a.email for a in _AUTHORS if a.start < _date.today() < a.end)


# Name of executable
__exe__ = "{{ cookiecutter.exe_name }}"


# Update doc with info about maintainers and version
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
    return _incomplete_format(doc, maintainers=maintainers, version=__version__, exe=__exe__)

{% raw %}
def _incomplete_format(text: str, **replace_args: str) -> str:
    """Replace some, but possibly not all format specifiers in text

    Regular format raises an error if not all {params} are supplied. However,
    want to be able to iteratively replace more arguments. This function only
    replaces arguments given, leaving the other {params} untouched.

    Args:
        text:          Original text
        replace_args:  Replacement arguments passed on to format
    """
    for word, replacement in replace_args.items():
        pattern = rf"({{{word}(?:|:[^}}]*)}})"  # {word} or {word:...}
        for match in _re.findall(pattern, text):
            replacer = match.format(**{word: replacement})
            text = text.replace(match, replacer)

    return text
{% endraw %}

__doc__ = _update_doc(__doc__)
