"""Define commands for The Hub

A command defines one set of behaviors for the `hub` script.

Each command is defined as a PyPlugs plug-in
"""

# Standard library imports
from typing import List

# Third party imports
from midgard.dev.timer import Timer
import pyplugs

# Hub imports
import the_hub.__main__
from the_hub.utils.log import logger


# Set up plug-in functions
call = pyplugs.call_factory(__package__)
funcs = pyplugs.funcs_factory(__package__)
info = pyplugs.info_factory(__package__)
names = pyplugs.names_factory(__package__)


@logger.catch
@Timer(f"Finish command in", logger=logger.time)
def run(command: str, args: List[str], opts: List[str]) -> None:
    """Run one command

    Args:
        command:  Name of command
        args:     List of arguments passed on to the command
        opts:     List of options passed on to the command
    """
    # Show help for the given command
    if "-h" in opts or "--help" in opts:
        the_hub.__main__._show_help(info(command).module_doc, command=command)
        raise SystemExit()

    # Run command
    description = info(command).description
    logger.opt(ansi=True).info(f"<underline>Start command {command!r}:</underline> {description}")
    logger.info(f"Arguments: {', '.join(args)}")
    logger.info(f"Options:   {', '.join(opts)}")
    call(command, args=args, opts=opts)
