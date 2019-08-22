"""{{ cookiecutter.project_name }} - {{ cookiecutter.project_short_description }}

Usage:
------

    $ {exe} <pipeline> [options] ...

Pipeline can be any of the following:

{pipelines}

The default pipeline is {{ cookiecutter.default_pipeline }}.

The following options are supported:

  -h, --help         Show this help message
      --info, ...    Change log level for the console.
                       Choose between --trace, --store, --debug, --dev, --info,
                       --time, --success, --warning, --error, --critical
      --log_to_file  Log to file as well as console
      --test_log     Show a test message at different log levels


Current maintainers:
--------------------

{maintainers}

Version: {version}
"""

# Standard library imports
from datetime import datetime
import sys

# {{ cookiecutter.project_name }} imports
import {{ cookiecutter.repo_name }}
from {{ cookiecutter.repo_name }} import pipelines
from {{ cookiecutter.repo_name }}.utils import log
from {{ cookiecutter.repo_name }}.utils.log import logger


def main():
    """Parse command line and run {{ cookiecutter.project_name }}"""
    opts = [o for o in sys.argv[1:] if o.startswith("-")]
    args = [a for a in sys.argv[1:] if not a.startswith("-")]

    # Set up logging
    log.init(opts)
    if "--test_log" in opts:
        log.test_log_levels()

    # Show help
    if "-h" in opts or "--help" in opts:
        help_pipelines = "\n".join(
            f"  {p:<18} {pipelines.info(p).description}" for p in pipelines.names()
        )
        _show_help(pipelines=help_pipelines)
        raise SystemExit()

    # Start logging
    exe = {{ cookiecutter.repo_name }}.__exe__
    logger.opt(ansi=True).info(f"<underline>Start {exe!r}</underline> at {datetime.now()}")

    # Choose pipeline
    pipeline = args[0] if args else "{{ cookiecutter.default_pipeline }}"

    # Perform pipeline
    pipelines.run(pipeline, args=args[1:], opts=opts)


def _show_help(doc=None, **replace_args):
    """Show a help message

    Args:
        doc:           Text of help documentation
        replace_args:  Additional {args} that should be replaced
    """
    # Update the doc and print it
    doc = __doc__ if doc is None else doc
    doc = {{ cookiecutter.repo_name }}._update_doc(doc).format(**replace_args)
    print(doc)


if __name__ == "__main__":
    main()
