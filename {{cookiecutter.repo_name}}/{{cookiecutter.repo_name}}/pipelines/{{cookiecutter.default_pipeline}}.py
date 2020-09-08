"""Example of how to use a plugin"""

# Third party imports
import pyplugs


@pyplugs.register
def read(data, meta):
    """Add information to data"""
    data.name = "{{ cookiecutter.project_name }}"
    data.path = __file__


@pyplugs.register
def dump_to_screen(data, meta):
    """Dump infomation to screen"""
    for key, value in data.items():
        print(f"{key:<10} = {value}")
