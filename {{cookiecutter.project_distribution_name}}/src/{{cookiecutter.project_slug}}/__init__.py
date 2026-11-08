"""Public API.

{{ cookiecutter.project_short_description | wordwrap(79) }}
"""

__all__: tuple[str, ...] = ("make_greeting",)

from loguru import logger

from ._{{ cookiecutter.project_slug }} import make_greeting

# Libraries stay quiet unless the application opts in, as Loguru recommends:
# https://loguru.readthedocs.io/en/stable/resources/recipes.html#configuring-loguru-to-be-used-by-a-library-or-an-application
logger.disable(__name__)
