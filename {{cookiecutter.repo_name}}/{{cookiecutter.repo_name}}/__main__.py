"""{{ cookiecutter.project_name }} - {{ cookiecutter.project_short_description }}

Usage:
------

    $ {exe} command [options] ...

The following options are supported:

{global_options}


Current maintainers:
--------------------

{maintainers}

Version: {version}
"""

# Standard library imports
from datetime import datetime
import sys

# Hub imports
import {{ cookiecutter.repo_name }}
from {{ cookiecutter.repo_name }} import commands
from {{ cookiecutter.repo_name }}.utils import log
from {{ cookiecutter.repo_name }}.utils.log import logger


# Global options, used mainly for documentation
_GLOBAL_OPTIONS = {
    ("-h", "--help"): "Show this help message",
    ("--log_to_file",): "Log to file, as well as console",
    ("--info", "..."): (
        "Change log level for the console.\n"
        "                       Choose between --trace, --debug, --store, --dev, --info,\n"
        "                       --time, --success, --warning, --error, --critical"
    ),
    ("--test_log",): "Show a test message at different log levels",
}


def main():
    """Parse command line and run The Hub"""
    opts = [o for o in sys.argv[1:] if o.startswith("-")]
    args = [a for a in sys.argv[1:] if not a.startswith("-")]

    # Set up logging
    log.init(opts)
    if "--test_log" in opts:
        log.test_log_levels()

    # Show help
    if not args:
        _show_help()
        raise SystemExit()

    # Start logging
    exe = {{ cookiecutter.repo_name }}.__exe__
    logger.opt(ansi=True).info(f"<underline>Start {exe!r}</underline> at {datetime.now()}")

    # Choose command
    command = args[0]

    # Perform command
    commands.run(command, args=args[1:], opts=opts)


def _show_help(doc=None, **replace_args):
    """Show a help message

    Args:
        doc:           Text of help documentation
        replace_args:  Additional {args} that should be replaced
    """
    # Add extra args that can be replaced
    replace_args["global_options"] = "\n".join(
        f"  {', '.join(o):<18} {d}" for o, d in _GLOBAL_OPTIONS.items()
    )

    # Update the doc and print it
    doc = __doc__ if doc is None else doc
    doc = {{ cookiecutter.repo_name }}._update_doc(doc).format(**replace_args)
    print(doc)
