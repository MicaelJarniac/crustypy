# Reference

- Tools
  - Formatting
    - [Black][black] <sup>[config][pyproject_toml]</sup>
      - [Compatible configs][black_cc]
    - [isort][isort] <sup>[config][setup_cfg]</sup>
  - Linting
    - [pydocstyle][pydocstyle] <sup>[config][setup_cfg]</sup>
    - [Flake8][flake8] <sup>[config][setup_cfg]</sup>
      - Plugins
        - [flake8-black][flake8-black]
        - [flake8-isort][flake8-isort]
        - [flake8-docstrings][flake8-docstrings]
  - Automating
    - [pre-commit][pre-commit] <sup>[config][_pre-commit-config_yaml]</sup>
      <details>
        <summary>Hooks</summary>

        - [`isort`][isort]
        - [`black`][black]
        - [`pydocstyle`][pydocstyle]
        - [`flake8`][flake8]
          - [`flake8-black`][flake8-black]
          - [`flake8-isort`][flake8-isort]
          - [`flake8-docstrings`][flake8-docstrings]
        - [`pre-commit-hooks`][pre-commit-hooks]
          - `check-toml`
          - `check-yaml`
          - `end-of-file-fixer`
          - `trailing-whitespace`
          - `requirements-txt-fixer`
      </details>
    - [Semantic Pull Requests][semantic-pull-requests]
    - [semantic-release][semantic-release] (used indirectly)
      - [python-semantic-release][python-semantic-release] <sup>[config][setup_cfg]</sup>
    - [Codecov][codecov]
      - [Action][codecov-action]
      - [{{ cookiecutter.project_slug }}][codecov-project]
    - [Nox][nox] <sup>[config][noxfile_py]</sup>
    - [Cookiecutter][cookiecutter]
    - [cruft][cruft] <sup>[config][pyproject_toml]</sup>
  - Type checking
    - [Mypy][mypy]
      - [Mypy Extensions][mypy-extensions]
  - Testing
    - [pytest][pytest] <sup>[config][setup_cfg]</sup>
      - Plugins
        - [pytest-cov][pytest-cov]
    - [Coverage.py][coveragepy] <sup>[config][setup_cfg]</sup>
  - Documenting
    - [Sphinx][sphinx] <sup>[config][docs_conf_py]</sup>
      - [Furo][furo]
      - [sphinxcontrib-spelling][sphinxcontrib-spelling]
      - [MyST][myst]
    - [Google style docstrings][docstring_google]
  - Building
    - [Setuptools][setuptools]
      - [`setup.py`][setup_py]
      - [`setup.cfg`][setup_cfg]
  - Configuration Files
    - [`setup.cfg`][setup_cfg]
    - [`pyproject.toml`][pyproject_toml]
    - [`.pre-commit-config.yaml`][_pre-commit-config_yaml]
    - [`.editorconfig`][_editorconfig]
    - [`docs/conf.py`][docs_conf_py]
    - [`docs/wordlist.txt`][docs_wordlist_txt]
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
  - https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
  - https://nvie.com/posts/a-successful-git-branching-model
  - https://github.community/t/syncing-a-fork-leaves-me-one-commit-ahead-of-upstream-master/1435/5
- Articles
  - [Don't commit `.vscode`][no-editor-config-gitignore]
  - <https://towardsdatascience.com/state-of-the-art-python-project-setup-82a046fc1f20> (pretty bad article, but useful)

[codecov-project]: https://app.codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

[_pre-commit-config_yaml]: ../.pre-commit-config.yaml
[pyproject_toml]: ../pyproject.toml
[setup_cfg]: ../setup.cfg
[_editorconfig]: ../.editorconfig
[docs_conf_py]: ./conf.py
[docs_wordlist_txt]: ./wordlist.txt
[noxfile_py]: ../noxfile.py

[setup_py]: ../setup.py

[black]: https://github.com/psf/black
[black_cc]: https://black.readthedocs.io/en/stable/compatible_configs.html
[isort]: https://github.com/PyCQA/isort
[pydocstyle]: https://github.com/PyCQA/pydocstyle
[flake8]: https://github.com/PyCQA/flake8
[flake8-black]: https://github.com/peterjc/flake8-black
[flake8-isort]: https://github.com/gforcada/flake8-isort
[flake8-docstrings]: https://gitlab.com/pycqa/flake8-docstrings
[pre-commit]: https://github.com/pre-commit/pre-commit
[pre-commit-hooks]: https://github.com/pre-commit/pre-commit-hooks
[rstcheck]: https://github.com/myint/rstcheck
[semantic-pull-requests]: https://github.com/zeke/semantic-pull-requests
[semantic-release]: https://github.com/semantic-release/semantic-release
[python-semantic-release]: https://github.com/relekang/python-semantic-release
[codecov]: https://codecov.io
[codecov-action]: https://github.com/marketplace/actions/codecov
[mypy]: https://github.com/python/mypy
[mypy-extensions]: https://github.com/python/mypy_extensions
[pytest]: https://github.com/pytest-dev/pytest
[pytest-cov]: https://github.com/pytest-dev/pytest-cov
[coveragepy]: https://github.com/nedbat/coveragepy
[nox]: https://github.com/theacodes/nox
[cruft]: https://github.com/cruft/cruft/
[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[sphinx]: https://www.sphinx-doc.org
[furo]: https://github.com/pradyunsg/furo
[sphinxcontrib-spelling]: https://github.com/sphinx-contrib/spelling
[myst]: https://github.com/executablebooks/myst-parser
[docstring_google]: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
[setuptools]: https://github.com/pypa/setuptools
[conventionalcommits]: https://www.conventionalcommits.org
[semver]: https://semver.org
[allcontributors]: https://github.com/all-contributors/all-contributors
[no-editor-config-gitignore]: https://blog.martinhujer.cz/dont-put-idea-vscode-directories-to-projects-gitignore
[editorconfig]: https://editorconfig.org
[angular-contributing]: https://github.com/angular/angular/blob/master/CONTRIBUTING.md#commit
[contributor-covenant]: https://contributor-covenant.org
[gitignore_python]: https://github.com/github/gitignore/blob/master/Python.gitignore
