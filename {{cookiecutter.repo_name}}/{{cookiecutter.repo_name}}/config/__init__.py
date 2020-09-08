"""Handle configuration settings in {{ cookiecutter.project_name }}

"""
# Standard library imports
import pathlib
from importlib import resources

# Third party imports
from pyconfs import Configuration

# Base directory for the {{ cookiecutter.repo_name }} package
_BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

# Marker representing {{ cookiecutter.repo_name }}/config
_PACKAGE_CONFIG_DIR = object()

# Prioritized list of possible locations for all {{ cookiecutter.project_name }} config files
_CONFIG_DIRECTORIES = (
    pathlib.Path.cwd(),
    pathlib.Path.home() / ".{{ cookiecutter.repo_name }}",
    _BASE_DIR / "config",
)


def read_config(cfg_name: str) -> Configuration:
    """Read one configuration from file

    Args:
        cfg_name:  Name of configuration, used for documentation

    Returns:
        A configuration object
    """
    cfg = Configuration(cfg_name)
    for file_path in config_paths(cfg_name):
        cfg.update_from_file(file_path)

    return cfg


def config_paths(cfg_name: str) -> pathlib.Path:
    """Yield all files that contain the given configuration"""
    file_names = (f"{cfg_name}.toml", f"{cfg_name}_local.toml")

    for file_name in file_names:
        for file_dir in _CONFIG_DIRECTORIES:
            file_path = file_dir / file_name
            if file_path.exists():
                yield file_path
                break


# Read configurations from file
{{ cookiecutter.repo_name }} = read_config("{{ cookiecutter.repo_name }}")
{{ cookiecutter.repo_name }}.vars.update(
    {
        "path_home": str(pathlib.Path.home()),
        "path_{{ cookiecutter.repo_name }}": str(_BASE_DIR),
    }
)
