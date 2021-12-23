<div align="center">
{%- if cookiecutter.use_discord_community == "yes" %}

  [![Discord][badge-chat]][chat]
  <br>
  <br>
{%- endif %}

  | | ![Badges][label-badges] |
  |--|--|
  | ![Build][label-build] | [![Nox][badge-actions]][actions] [![semantic-release][badge-semantic-release]][semantic-release] [![PyPI][badge-pypi]][pypi] [![Read the Docs][badge-docs]][docs] |
  | ![Tests][label-tests] | [![coverage][badge-coverage]][coverage] [![pre-commit][badge-pre-commit]][pre-commit] |
  | ![Standards][label-standards] | [![SemVer 2.0.0][badge-semver]][semver] [![Conventional Commits][badge-conventional-commits]][conventional-commits] |
  | ![Code][label-code] | [![Code style: black][badge-black]][Black] [![Imports: isort][badge-isort]][isort] [![Checked with mypy][badge-mypy]][mypy] |
  | ![Repo][label-repo] | [![GitHub issues][badge-issues]][issues] [![GitHub stars][badge-stars]][stars] [![GitHub license][badge-license]][license] [![All Contributors][badge-all-contributors]][contributors] [![Contributor Covenant][badge-code-of-conduct]][code-of-conduct] |
</div>

<!-- Badges -->
{%- if cookiecutter.use_discord_community == "yes" %}
[badge-chat]: https://img.shields.io/discord/{{ cookiecutter.discord_id }}?label=chat&logo=discord&style=flat-square
[chat]: https://discord.gg/{{ cookiecutter.discord_invite }}
{%- endif %}

<!-- Labels -->
[label-badges]: https://img.shields.io/badge/%F0%9F%94%96-badges-purple?style=for-the-badge
[label-build]: https://img.shields.io/badge/%F0%9F%94%A7-build-darkblue?style=flat-square
[label-tests]: https://img.shields.io/badge/%F0%9F%A7%AA-tests-darkblue?style=flat-square
[label-standards]: https://img.shields.io/badge/%F0%9F%93%91-standards-darkblue?style=flat-square
[label-code]: https://img.shields.io/badge/%F0%9F%92%BB-code-darkblue?style=flat-square
[label-repo]: https://img.shields.io/badge/%F0%9F%93%81-repo-darkblue?style=flat-square

<!-- Build -->
[badge-actions]: https://img.shields.io/github/workflow/status/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/Test%20with%20Nox/main?style=flat-square
[actions]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/actions
[badge-semantic-release]: https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079?style=flat-square
[semantic-release]: https://github.com/semantic-release/semantic-release
[badge-pypi]: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}?style=flat-square
[pypi]: https://pypi.org/project/{{ cookiecutter.project_slug }}
[badge-docs]: https://img.shields.io/readthedocs/{{ cookiecutter.project_slug }}?style=flat-square
[docs]: https://{{ cookiecutter.project_slug }}.readthedocs.io

<!-- Tests -->
[badge-coverage]: https://img.shields.io/codecov/c/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}?logo=codecov&style=flat-square&token=yqKa1DPwPC
[coverage]: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}
[badge-pre-commit]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=flat-square&logo=pre-commit&logoColor=white
[pre-commit]: https://github.com/pre-commit/pre-commit

<!-- Standards -->
[badge-semver]: https://img.shields.io/badge/SemVer-2.0.0-blue?style=flat-square&logo=semver
[semver]: https://semver.org/spec/v2.0.0.html
[badge-conventional-commits]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow?style=flat-square
[conventional-commits]: https://conventionalcommits.org

<!-- Code -->
[badge-black]: https://img.shields.io/badge/code%20style-black-black?style=flat-square
[Black]: https://github.com/psf/black
[badge-isort]: https://img.shields.io/badge/imports-isort-%231674b1?style=flat-square&labelColor=ef8336
[isort]: https://pycqa.github.io/isort
[badge-mypy]: https://img.shields.io/badge/mypy-checked-2A6DB2?style=flat-square
[mypy]: http://mypy-lang.org

<!-- Repo -->
[badge-issues]: https://img.shields.io/github/issues/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}?style=flat-square
[issues]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/issues
[badge-stars]: https://img.shields.io/github/stars/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}?style=flat-square
[stars]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/stargazers
[badge-license]: https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}?style=flat-square
[license]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/blob/main/LICENSE
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[badge-all-contributors]: https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square
<!-- ALL-CONTRIBUTORS-BADGE:END -->
[contributors]: #Contributors-✨
[badge-code-of-conduct]: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa?style=flat-square
[code-of-conduct]: CODE_OF_CONDUCT.md
<!---->

# {{ cookiecutter.project_name }}
{{ cookiecutter.project_short_description }}

[Read the Docs][docs]

## Installation

### pip
[*{{ cookiecutter.project_slug }}*][pypi] is available on [pip](https://pip.pypa.io/en/stable/):

```bash
pip install {{ cookiecutter.project_slug }}
```

### GitHub
You can also install the latest version of the code directly from GitHub:
```bash
pip install git+git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}
```

## Usage
For more examples, see the [full documentation][docs].

```python
from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_name }}
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
[MIT](LICENSE)

This project was created with the [MicaelJarniac/cookiecutter-python-project](https://github.com/MicaelJarniac/cookiecutter-python-project) template.
