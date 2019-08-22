"""Example of how to use a plugin

Usage:
------

    $ {exe} {command} [options] ...

The following options are supported:

Furthermore, the following global options are available:

{global_options}


Current maintainers:
--------------------

{maintainers}

Version: {version}
"""

# Third party imports
import pyplugs


@pyplugs.register
def dump(args, opts):
    """Dump all the data to a file"""
    print("Hurra!")
