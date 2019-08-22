"""Define pipelines for {{ cookiecutter.project_name }}

A pipeline defines one set of behaviors for the `{{ cookiecutter.exe_name }}` script.

Each pipeline is defined as a PyPlugs plug-in
"""

# Standard library imports
from typing import List

# Third party imports
import pyplugs

# Hub imports
import {{ cookiecutter.repo_name }}.__main__
from {{ cookiecutter.repo_name }}.utils.log import logger


# Set up plug-in functions
call = pyplugs.call_factory(__package__)
funcs = pyplugs.funcs_factory(__package__)
info = pyplugs.info_factory(__package__)
names = pyplugs.names_factory(__package__)


@logger.catch
def run(pipeline: str, args: List[str], opts: List[str]) -> None:
    """Run one pipeline

    Args:
        pipeline:  Name of pipeline
        args:     List of arguments passed on to the pipeline
        opts:     List of options passed on to the pipeline
    """
    # Show help for the given pipeline
    if "-h" in opts or "--help" in opts:
        {{ cookiecutter.repo_name }}.__main__._show_help(info(pipeline).module_doc, pipeline=pipeline)
        raise SystemExit()

    # Run pipeline
    description = info(pipeline).description
    logger.opt(ansi=True).info(f"<underline>Start pipeline {pipeline!r}:</underline> {description}")
    logger.info(f"Arguments: {', '.join(args)}")
    logger.info(f"Options:   {', '.join(opts)}")
    call(pipeline, args=args, opts=opts)
