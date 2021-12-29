"""{{ cookiecutter.project_short_description }}"""

__version__ = "{{ cookiecutter.version }}"

from ._{{ cookiecutter.project_slug }} import make_greeting

__all__ = ["make_greeting"]
