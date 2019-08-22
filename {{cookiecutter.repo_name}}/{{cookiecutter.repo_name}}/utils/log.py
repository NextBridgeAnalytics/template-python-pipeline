"""Set up logging for {{ cookiecutter.project_name }}

Logging is based on the Loguru library: https://github.com/Delgan/loguru/
"""

# Standard library imports
import functools
import sys
from typing import List, NamedTuple

# Third party imports
from loguru import logger

# {{ cookiecutter.project_name }} imports
from {{ cookiecutter.repo_name }}.utils import config


# Custom log levels
class LogLevel(NamedTuple):
    name: str
    no: int
    color: str
    icon: str


# List additional levels
_ADDITIONAL_LEVELS = [
    LogLevel("STORE", no=8, color="<light-magenta>", icon="•"),  # Store output files
    LogLevel("DEV", no=15, color="<blue>", icon="☣"),  # Developer info, todos etc
    LogLevel("TIME", no=23, color="<yellow>", icon="⏱"),  # Timings of code
]


def init(opts: List[str]) -> None:
    """Initialize a logger based on configuration settings and options"""
    # Remove the default logger
    logger.remove()

    # Add file logger if asked for in options
    if "--log_to_file" in opts:
        file_args = config.{{ cookiecutter.repo_name }}.log_file.as_dict()
        del file_args["file_path"]
        logger.add(config.{{ cookiecutter.repo_name }}.log_file.file_path.path, **file_args)

    # Set log level
    all_levels = set(logger._levels)
    opt_levels = {o[2:].upper() for o in opts if o.startswith("--")}
    level = (all_levels & opt_levels) or {config.{{ cookiecutter.repo_name }}.log_console.level.str.upper()}
    logger.add(sys.stderr, level=level.pop(), format=config.{{ cookiecutter.repo_name }}.log_console.format.str)


def _add_levels(additional_levels: List[LogLevel]) -> None:
    """Add custom log levels"""
    for level in additional_levels:
        logger.level(**level._asdict())
        setattr(logger, level.name.lower(), functools.partial(logger.log, level.name))


def test_log_levels():
    """Log to each level for a simple visual test"""

    # Add a new logger that logs all levels
    logger.remove()
    logger.add(sys.stderr, level=0, format=config.{{ cookiecutter.repo_name }}.log_console.format.str)

    # Log to each level
    for name, level in sorted(logger._levels.items(), key=lambda lvl: lvl[1].no):
        log_func = getattr(logger, name.lower())
        log_func(f"Use logger.{name.lower()}() to write to {name} ({level.no})")

    # Quit the program
    raise SystemExit()


# Add custom levels at import
_add_levels(_ADDITIONAL_LEVELS)
