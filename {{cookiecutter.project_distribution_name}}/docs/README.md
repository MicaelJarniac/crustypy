<div align="center">
{%- if cookiecutter.use_discord_community == "yes" %}

  [![Discord][badge-chat]][chat]
  <br>
  <br>
{%- endif %}

  | | ![Badges][label-badges] |
  |:-|:-|
  | ![Build][label-build] | [![Nox][badge-actions]][actions] [![semantic-release][badge-semantic-release]][semantic-release] [![PyPI][badge-pypi]][pypi] [![Read the Docs][badge-docs]][docs] |
  | ![Tests][label-tests] | [![coverage][badge-coverage]][coverage] [![pre-commit][badge-pre-commit]][pre-commit] |
  | ![Standards][label-standards] | [![SemVer 2.0.0][badge-semver]][semver] [![Conventional Commits][badge-conventional-commits]][conventional-commits] |
  | ![Code][label-code] | [![Code style: black][badge-black]][Black] [![Ruff][badge-ruff]][ruff] [![Checked with mypy][badge-mypy]][mypy] |
  | ![Repo][label-repo] | [![GitHub issues][badge-issues]][issues] [![GitHub stars][badge-stars]][stars] [![GitHub license][badge-license]][license] [![All Contributors][badge-all-contributors]][contributors] [![Contributor Covenant][badge-code-of-conduct]][code-of-conduct] |
</div>

<!-- Badges -->
{%- if cookiecutter.use_discord_community == "yes" %}
[badge-chat]: {{ cookiecutter.shields_url }}/discord/{{ cookiecutter.discord_id }}?label=chat&logo=discord&style=flat-square
[chat]: https://discord.gg/{{ cookiecutter.discord_invite }}
{%- endif %}

<!-- Labels -->
[label-badges]: {{ cookiecutter.shields_url }}/badge/%F0%9F%94%96-badges-purple?style=for-the-badge
[label-build]: {{ cookiecutter.shields_url }}/badge/%F0%9F%94%A7-build-darkblue?style=flat-square
[label-tests]: {{ cookiecutter.shields_url }}/badge/%F0%9F%A7%AA-tests-darkblue?style=flat-square
[label-standards]: {{ cookiecutter.shields_url }}/badge/%F0%9F%93%91-standards-darkblue?style=flat-square
[label-code]: {{ cookiecutter.shields_url }}/badge/%F0%9F%92%BB-code-darkblue?style=flat-square
[label-repo]: {{ cookiecutter.shields_url }}/badge/%F0%9F%93%81-repo-darkblue?style=flat-square

<!-- Build -->
[badge-actions]: {{ cookiecutter.shields_url }}/github/actions/workflow/status/{{ cookiecutter.__github_path }}/nox.yml?branch=main&style=flat-square
[actions]: {{ cookiecutter.__github_url }}/actions
[badge-semantic-release]: {{ cookiecutter.shields_url }}/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079?style=flat-square
[semantic-release]: https://github.com/semantic-release/semantic-release
[badge-pypi]: {{ cookiecutter.shields_url }}/pypi/v/{{ cookiecutter.project_distribution_name }}?style=flat-square
[pypi]: https://pypi.org/project/{{ cookiecutter.project_distribution_name }}
[badge-docs]: {{ cookiecutter.shields_url }}/readthedocs/{{ cookiecutter.__readthedocs_name }}?style=flat-square
[docs]: https://{{ cookiecutter.__readthedocs_name }}.readthedocs.io

<!-- Tests -->
[badge-coverage]: {{ cookiecutter.shields_url }}/codecov/c/gh/{{ cookiecutter.__github_path }}?logo=codecov&style=flat-square
[coverage]: https://codecov.io/gh/{{ cookiecutter.__github_path }}
[badge-pre-commit]: {{ cookiecutter.shields_url }}/badge/pre--commit-enabled-brightgreen?style=flat-square&logo=pre-commit&logoColor=white
[pre-commit]: https://github.com/pre-commit/pre-commit

<!-- Standards -->
[badge-semver]: {{ cookiecutter.shields_url }}/badge/SemVer-2.0.0-blue?style=flat-square&logo=semver
[semver]: https://semver.org/spec/v2.0.0.html
[badge-conventional-commits]: {{ cookiecutter.shields_url }}/badge/Conventional%20Commits-1.0.0-yellow?style=flat-square
[conventional-commits]: https://conventionalcommits.org

<!-- Code -->
[badge-black]: {{ cookiecutter.shields_url }}/badge/code%20style-black-black?style=flat-square
[Black]: https://github.com/psf/black
[badge-ruff]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&style=flat-square
[ruff]: https://github.com/astral-sh/ruff
[badge-mypy]: {{ cookiecutter.shields_url }}/badge/mypy-checked-2A6DB2?style=flat-square
[mypy]: http://mypy-lang.org

<!-- Repo -->
[badge-issues]: {{ cookiecutter.shields_url }}/github/issues/{{ cookiecutter.__github_path }}?style=flat-square
[issues]: {{ cookiecutter.__github_url }}/issues
[badge-stars]: {{ cookiecutter.shields_url }}/github/stars/{{ cookiecutter.__github_path }}?style=flat-square
[stars]: {{ cookiecutter.__github_url }}/stargazers
[badge-license]: {{ cookiecutter.shields_url }}/github/license/{{ cookiecutter.__github_path }}?style=flat-square
[license]: {{ cookiecutter.__github_url }}/blob/main/LICENSE
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[badge-all-contributors]: {{ cookiecutter.shields_url }}/badge/all_contributors-0-orange.svg?style=flat-square
<!-- ALL-CONTRIBUTORS-BADGE:END -->
[contributors]: #Contributors-✨
[badge-code-of-conduct]: {{ cookiecutter.shields_url }}/badge/Contributor%20Covenant-2.1-4baaaa?style=flat-square
[code-of-conduct]: CODE_OF_CONDUCT.md
<!---->

# {{ cookiecutter.project_name }}
{{ cookiecutter.project_short_description }}

[Read the Docs][docs]

## Installation

### pip
[*{{ cookiecutter.project_distribution_name }}*][pypi] is available on [pip](https://pip.pypa.io/en/stable/):

```bash
pip install {{ cookiecutter.project_distribution_name }}
```

### GitHub
You can also install the latest version of the code directly from GitHub:
```bash
pip install git+git://github.com/{{ cookiecutter.__github_path }}
```

## Usage
For more examples, see the [full documentation][docs].

```python
from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

More details can be found in [CONTRIBUTING](CONTRIBUTING.md).

## Contributors ✨
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

## License
[MIT](../LICENSE)

This project was created with the [MicaelJarniac/cookiecutter-python-project](https://github.com/MicaelJarniac/cookiecutter-python-project) template.
