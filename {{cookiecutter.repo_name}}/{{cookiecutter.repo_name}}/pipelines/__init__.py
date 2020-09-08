"""Define pipelines for {{ cookiecutter.project_name }}

A pipeline defines one set of behaviors for the `{{ cookiecutter.exe_name }}` script.

Each pipeline is defined as a PyPlugs plug-in
"""

# Third party imports
import munch
import pyplugs
from codetiming import Timer

# {{ cookiecutter.project_name }} imports
import {{ cookiecutter.repo_name }}.__main__
from {{ cookiecutter.repo_name }} import config
from {{ cookiecutter.repo_name }}.utils.log import logger


# Set up plug-in functions
call = pyplugs.call_factory(__package__)
funcs = pyplugs.funcs_factory(__package__)


@logger.catch(reraise=True)  # Log exceptions with more details
@Timer("pipeline", "Finished pipeline in {:.2f} seconds", logger=logger.time)
def run(pipeline: str) -> None:
    """Run one pipeline

    Args:
        pipeline:  Name of pipeline
    """

    # Run pipeline
    stages = config.{{ cookiecutter.repo_name }}.pipelines[pipeline].stages or funcs(pipeline)
    logger.opt(colors=True).info(
        f"Start pipeline <red>{pipeline!r}</red> with stages: {', '.join(stages)}"
    )

    data, meta = munch.Munch(), munch.Munch()
    for stage in stages:
        logger.opt(colors=True).info(f"Start stage <cyan>{stage!r}</cyan>")
        {% raw %}with Timer(f"stage_{stage}", f"Finished {stage!r} in {{:.2f}} seconds", logger=logger.time):{% endraw %}
            call(pipeline, func=stage, data=data, meta=meta)
