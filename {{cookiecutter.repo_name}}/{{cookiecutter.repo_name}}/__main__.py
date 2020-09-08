"""{{ cookiecutter.project_name }} - {{ cookiecutter.project_short_description }}

Run PIPELINE. Change this text to update the --help text.


\b
Current maintainers:
--------------------

\b
{maintainers}

Version: {version}
"""

# Standard library imports
from datetime import datetime
import sys

# Third party imports
import typer

# {{ cookiecutter.project_name }} imports
import {{ cookiecutter.repo_name }}
from {{ cookiecutter.repo_name }} import config
from {{ cookiecutter.repo_name }}.utils import log
from {{ cookiecutter.repo_name }}.utils.log import logger
from {{ cookiecutter.repo_name }} import pipelines

def main():
    """Dispatch to typer"""
    run_model.__doc__ = {{ cookiecutter.repo_name }}._update_doc(__doc__)
    typer.run(run_model)


def run_model(
    pipeline: str = typer.Argument("{{ cookiecutter.default_pipeline }}"),
    log_level: str = typer.Option(
        config.{{ cookiecutter.repo_name }}.log.console.level,
        help = "Level for log messages",
        show_default=True
    ),
    show_log_levels: bool = typer.Option(
        False, "--show-log-levels", help="Show all possible log levels"
    ),
) -> None:
    """Parse command line and run {{ cookiecutter.project_name }}"""
    # Set up logging
    log.init(level=log_level)
    if show_log_levels:
        log.show_log_levels()
        raise SystemExit()

    # Start logging
    logger.opt(colors=True).info(f"Start <red>'{{ cookiecutter.exe_name }}'</red> at {datetime.now()}")

    # Run pipeline
    pipelines.run(pipeline)


if __name__ == "__main__":
    main()
