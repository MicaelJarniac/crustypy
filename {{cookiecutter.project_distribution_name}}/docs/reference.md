# Reference

- Tools
  - Formatting
    - [Ruff][ruff] <sup>[config][pyproject_toml]</sup>
  - Linting
    - [Ruff][ruff] <sup>[config][pyproject_toml]</sup>
  - Automating
    - [pre-commit][pre-commit] <sup>[config][_pre-commit-config_yaml]</sup>
      <details>
        <summary>Hooks</summary>

        - [`pre-commit-hooks`][pre-commit-hooks]
          - `check-toml`
          - `check-yaml`
          - `check-json`
          - `end-of-file-fixer`
          - `trailing-whitespace`
        - Local, from `uv.lock`
          - `ruff-check`
          - `ruff-format`
        - [`uv-pre-commit`][uv-pre-commit]
          - `uv-lock`
        - [`typos`][typos]
        - [`zizmor`][zizmor]
      </details>
    - [Python Semantic Release][python-semantic-release] <sup>[config][pyproject_toml]</sup>
    - [Dependabot][dependabot] <sup>[config][_github_dependabot_yml]</sup>
    - [zizmor][zizmor]
    - [Codecov][codecov]
      - [Action][codecov-action]
      - [{{ cookiecutter.project_distribution_name }}][codecov-project]
    - [Nox][nox] <sup>[config][noxfile_py]</sup>
    - [Cookiecutter][cookiecutter]
    - [cruft][cruft] <sup>[config][pyproject_toml]</sup>
  - Type checking
    - [ty][ty] <sup>[config][pyproject_toml]</sup>
  - Testing
    - [pytest][pytest] <sup>[config][pyproject_toml]</sup>
      - Plugins
        - [pytest-cov][pytest-cov]
        - [pytest-benchmark][pytest-benchmark]
      - [Hypothesis][hypothesis]
      - [inline-snapshot][inline-snapshot]
    - [airspeed velocity (`asv`)][asv]
    - [Coverage.py][coveragepy] <sup>[config][pyproject_toml]</sup>
  - Documenting
    - [MkDocs][mkdocs] <sup>[config][docs_mkdocs_yml]</sup>
      - [Material for MkDocs][mkdocs-material]
      - [mkdocstrings][mkdocstrings]
    - [Google style docstrings][docstring_google]
  - Building
    - [uv][uv]
      - [`uv_build`][uv_build] <sup>[config][pyproject_toml]</sup>
  - Spell checking
    - [typos][typos] <sup>[config][pyproject_toml]</sup>
  - Logging
    - [Loguru][loguru]
  - Configuration Files
    - [`pyproject.toml`][pyproject_toml]
    - [`.pre-commit-config.yaml`][_pre-commit-config_yaml]
    - [`.editorconfig`][_editorconfig]
    - [`mkdocs.yml`][docs_mkdocs_yml]
    - [`.readthedocs.yaml`][_readthedocs_yaml]
    - [`.github/dependabot.yml`][_github_dependabot_yml]
    - [`noxfile.py`][noxfile_py]
- Standards
  - Commits
    - [Conventional Commits][conventionalcommits]
  - Versioning
    - [Semantic Versioning][semver]
  - Contributing
    - [All Contributors][allcontributors]
  - [.gitignore][gitignore_python]
- Editor
  - [EditorConfig][editorconfig] <sup>[config][_editorconfig]</sup>
- Guidelines
  - [Angular `CONTRIBUTING.md`][angular-contributing]
  - [Contributor Covenant][contributor-covenant]
- Workflows
  - [Gitflow workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
  - [A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model)
  - [Syncing a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)
- Articles
  - [Don't commit `.vscode`][no-editor-config-gitignore]

[codecov-project]: https://app.codecov.io/gh/{{ cookiecutter.__github_path }}

[_pre-commit-config_yaml]: {{ cookiecutter.__github_url }}/blob/{{ cookiecutter.main_branch }}/.pre-commit-config.yaml
[pyproject_toml]: {{ cookiecutter.__github_url }}/blob/{{ cookiecutter.main_branch }}/pyproject.toml
[_editorconfig]: {{ cookiecutter.__github_url }}/blob/{{ cookiecutter.main_branch }}/.editorconfig
[docs_mkdocs_yml]: {{ cookiecutter.__github_url }}/blob/{{ cookiecutter.main_branch }}/mkdocs.yml
[_readthedocs_yaml]: {{ cookiecutter.__github_url }}/blob/{{ cookiecutter.main_branch }}/.readthedocs.yaml
[_github_dependabot_yml]: {{ cookiecutter.__github_url }}/blob/{{ cookiecutter.main_branch }}/.github/dependabot.yml
[noxfile_py]: {{ cookiecutter.__github_url }}/blob/{{ cookiecutter.main_branch }}/noxfile.py

[ruff]: https://github.com/astral-sh/ruff
[pre-commit]: https://github.com/pre-commit/pre-commit
[pre-commit-hooks]: https://github.com/pre-commit/pre-commit-hooks
[python-semantic-release]: https://github.com/python-semantic-release/python-semantic-release
[dependabot]: https://docs.github.com/en/code-security/dependabot
[zizmor]: https://docs.zizmor.sh
[codecov]: https://codecov.io
[codecov-action]: https://github.com/codecov/codecov-action
[ty]: https://github.com/astral-sh/ty
[pytest]: https://github.com/pytest-dev/pytest
[pytest-cov]: https://github.com/pytest-dev/pytest-cov
[pytest-benchmark]: https://github.com/ionelmc/pytest-benchmark
[hypothesis]: https://hypothesis.readthedocs.io
[inline-snapshot]: https://15r10nk.github.io/inline-snapshot
[uv-pre-commit]: https://github.com/astral-sh/uv-pre-commit
[uv_build]: https://docs.astral.sh/uv/concepts/build-backend/
[typos]: https://github.com/crate-ci/typos
[loguru]: https://github.com/Delgan/loguru
[asv]: https://github.com/airspeed-velocity/asv
[coveragepy]: https://github.com/nedbat/coveragepy
[nox]: https://github.com/wntrblm/nox
[cruft]: https://github.com/cruft/cruft/
[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[mkdocs]: https://www.mkdocs.org
[mkdocs-material]: https://squidfunk.github.io/mkdocs-material
[mkdocstrings]: https://mkdocstrings.github.io
[docstring_google]: https://mkdocstrings.github.io/griffe/reference/docstrings/#google-style
[uv]: https://docs.astral.sh/uv
[conventionalcommits]: https://www.conventionalcommits.org
[semver]: https://semver.org
[allcontributors]: https://github.com/all-contributors/all-contributors
[no-editor-config-gitignore]: https://blog.martinhujer.cz/dont-put-idea-vscode-directories-to-projects-gitignore
[editorconfig]: https://editorconfig.org
[angular-contributing]: https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit
[contributor-covenant]: https://contributor-covenant.org
[gitignore_python]: https://github.com/github/gitignore/blob/main/Python.gitignore
