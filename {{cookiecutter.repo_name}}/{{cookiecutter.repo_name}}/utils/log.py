"""Set up logging for {{ cookiecutter.project_name }}

Logging is based on the Loguru library: https://github.com/Delgan/loguru/
"""

# Standard library imports
import functools
import sys
from typing import List
from typing import NamedTuple

# Third party imports
from loguru import logger

# {{ cookiecutter.project_name }} imports
from {{ cookiecutter.repo_name }} import config


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


def init(level: str) -> None:
    """Initialize a logger based on configuration settings and options"""
    # Remove the default logger
    logger.remove()

    # Set log level
    logger.add(sys.stderr, level=level.upper(), format=config.{{ cookiecutter.repo_name }}.log.console.format)


def _add_levels(additional_levels: List[LogLevel]) -> None:
    """Add custom log levels"""
    for level in additional_levels:
        logger.level(**level._asdict())
        setattr(logger.__class__, level.name.lower(), functools.partial(logger.log, level.name))

    def blank(self):
        """Write a blank line to the logger"""
        for handler in self._core.handlers.values():
            handler._sink.write("\n")

    setattr(logger.__class__, "blank", functools.partial(blank, logger))


def show_log_levels():
    """Log to each level for a simple visual test"""

    # Add a new logger that logs all levels
    logger.remove()
    logger.add(sys.stderr, level=0, format=config.{{ cookiecutter.repo_name }}.log.console.format)

    # Log to each level
    for name, level in sorted(logger._core.levels.items(), key=lambda lvl: lvl[1].no):
        log_func = getattr(logger, name.lower())
        log_func(f"Use logger.{name.lower()}() to write to {name} ({level.no})")


# Add custom levels at import
_add_levels(_ADDITIONAL_LEVELS)
