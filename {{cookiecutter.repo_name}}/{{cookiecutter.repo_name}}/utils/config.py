"""Handle configuration settings in {{ cookiecutter.project_name }}

"""
# Standard library imports
import pathlib

# Import resources, be compatible with Python 3.6
try:
    from importlib import resources
except ImportError:
    import importlib_resources as resources

# Third party imports
from midgard.config.config import Configuration

# Base directory for the {{ cookiecutter.repo_name }} package
_BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent

# Prioritized list of possible names of {{ cookiecutter.project_name }} config files
_CONFIG_FILENAMES = dict(
    {{ cookiecutter.repo_name }}=("{{ cookiecutter.repo_name }}_local.ini", "{{ cookiecutter.repo_name }}.ini")
)

# Prioritized list of possible locations for all {{ cookiecutter.project_name }} config files
_PACKAGE_CONFIG_DIR = object()  # Marker representing {{ cookiecutter.repo_name }}/config
_CONFIG_DIRECTORIES = (
    pathlib.Path.cwd(),
    pathlib.Path.home() / ".{{ cookiecutter.repo_name }}",
    _PACKAGE_CONFIG_DIR,
)


def read_config(cfg_name: str, use_options: bool = False) -> Configuration:
    """Read one configuration from file

    Args:
        cfg_name:     Name of configuration, used for documentation
        use_options:  Allow command line options to overwrite config file

    Returns:
        A configuration object
    """
    cfg = Configuration(cfg_name)
    for file_path in config_paths(cfg_name):
        cfg.update_from_file(file_path)

    if use_options:
        cfg.update_from_options()

    return cfg


def config_paths(cfg_name: str) -> pathlib.Path:
    """Yield all files that contain the given configuration"""
    for file_name in file_names(cfg_name):
        for file_dir in _CONFIG_DIRECTORIES:
            if file_dir is _PACKAGE_CONFIG_DIR:
                try:
                    with resources.path(
                        "{{ cookiecutter.repo_name }}.config", file_name
                    ) as file_path:
                        yield file_path
                        break
                except FileNotFoundError:
                    continue
            else:
                file_path = file_dir / file_name
                if file_path.exists():
                    yield file_path
                    break


def file_names(cfg_name: str) -> str:
    """Return all possible file names for a given configuration"""
    default_filenames = f"{cfg_name}.ini", f"{cfg_name}_local.ini"
    return _CONFIG_FILENAMES.get(cfg_name, default_filenames)


# Read configurations from file and command line options
{{ cookiecutter.repo_name }} = read_config("{{ cookiecutter.repo_name }}", use_options=True)
{{ cookiecutter.repo_name }}.vars["path_{{ cookiecutter.repo_name }}"] = str(_BASE_DIR)
