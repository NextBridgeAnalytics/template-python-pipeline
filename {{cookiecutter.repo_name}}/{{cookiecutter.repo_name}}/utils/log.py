"""Set up logging for The Hub

Logging is based on the Loguru library: https://github.com/Delgan/loguru/

"""

# Standard library imports
import functools
import sys
from typing import List, NamedTuple

# Third party imports
from loguru import logger

# Hub imports
from the_hub.utils import config


# Custom log levels
class LogLevel(NamedTuple):
    name: str
    no: int
    color: str
    icon: str


_ADDITIONAL_LEVELS = [
    LogLevel("STORE", no=12, color="<light-magenta>", icon="•"),  # Store all output files
    LogLevel("DEV", no=15, color="<blue>", icon="☣"),  # Developer info, todos etc
    LogLevel("TIME", no=23, color="<yellow>", icon="⏱"),  # Timings of code
]


def init(opts: List[str]) -> None:
    """Initialize a logger based on configuration settings and options"""
    # Remove the default logger
    logger.remove()

    # Add file logger if asked for in options
    if "--log_to_file" in opts:
        file_args = config.hub.log_file.as_dict()
        del file_args["file_path"]
        logger.add(config.hub.log_file.file_path.path, **file_args)

    # Set log level
    all_levels = set(logger._levels)
    opt_levels = {o[2:].upper() for o in opts if o.startswith("--")}
    level = (all_levels & opt_levels) or {config.hub.log_console.level.str.upper()}
    logger.add(sys.stderr, level=level.pop(), format=config.hub.log_console.format.str)


def _add_levels(additional_levels: List[LogLevel]) -> None:
    """Add custom log levels"""
    for level in additional_levels:
        logger.level(**level._asdict())
        setattr(logger, level.name.lower(), functools.partial(logger.log, level.name))


def test_log_levels():
    """Log to each level for a simple visual test"""
    for name, level in sorted(logger._levels.items(), key=lambda lvl: lvl[1].no):
        log_func = getattr(logger, name.lower())
        log_func(f"Testing {name} logger at severity {level.no}")


# Add custom levels at import
_add_levels(_ADDITIONAL_LEVELS)
