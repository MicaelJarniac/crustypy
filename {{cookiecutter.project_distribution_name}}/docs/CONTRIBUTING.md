# Contributing to {{ cookiecutter.project_name }}

✨ Thanks for contributing to **{{ cookiecutter.project_name }}**! ✨

As a contributor, here are the guidelines we would like you to follow:
- [Code of conduct](#code-of-conduct)
- [How can I contribute?](#how-can-i-contribute)
- [Using the issue tracker](#using-the-issue-tracker)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Coding rules](#coding-rules)
- [Working with the code](#working-with-the-code)

Read the [reference](reference.md).

We also recommend that you read [How to Contribute to Open Source](https://opensource.guide/how-to-contribute).

## Code of conduct

Help us keep **{{ cookiecutter.project_name }}** open and inclusive. Please read and follow our [Code of conduct](CODE_OF_CONDUCT.md).

## How can I contribute?

### Improve documentation

As a **{{ cookiecutter.project_name }}** user, you are the perfect candidate to help us improve our documentation: typo corrections, clarifications, more examples, etc. Take a look at the [documentation issues that need help]({{ cookiecutter.__github_url }}/issues?q=is%3Aopen+label%3Adocumentation+label%3A"help+wanted").

Please follow the [Documentation guidelines](#documentation).

### Give feedback on issues

Some issues are created without information requested in the [Bug report guideline](#bug-report). Help make them easier to resolve by adding any relevant information.

### Fix bugs and implement features

Confirmed bugs and ready-to-implement features are marked with the [help wanted label]({{ cookiecutter.__github_url }}/labels/help+wanted). Post a comment on an issue to indicate you would like to work on it and to request help from the community.

## Using the issue tracker

The issue tracker is the channel for [bug reports](#bug-report), [features requests](#feature-request) and [submitting pull requests](#submitting-a-pull-request) only. <!-- Please use the [Support](docs/support/README.md) and [Get help](README.md#get-help) sections for support, troubleshooting and questions. -->

Before opening an issue or a Pull Request, please use the [GitHub issue search]({{ cookiecutter.__github_url }}/issues) to make sure the bug or feature request hasn't been already reported or fixed.

### Bug report

A good bug report shouldn't leave others needing to chase you for more information. Please try to be as detailed as possible in your report and fill the information requested in the [Bug report template]({{ cookiecutter.__github_url }}/issues/new?template=bug_report.md).

### Feature request

Feature requests are welcome, but take a moment to find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature. Please provide as much detail and context as possible and fill the information requested in the [Feature request template]({{ cookiecutter.__github_url }}/issues/new?template=feature_request.md).

## Submitting a Pull Request

Good pull requests, whether patches, improvements, or new features, are a fantastic help. They should remain focused in scope and avoid containing unrelated commits.

**Please ask first** before embarking on any significant pull requests (e.g. implementing features, refactoring code), otherwise you risk spending a lot of time working on something that the project's developers might not want to merge into the project.

If you have never created a pull request before, welcome 🎉 😄. [Here is a great tutorial](https://opensource.guide/how-to-contribute/#opening-a-pull-request) on how to send one :)

Here is a summary of the steps to follow:

1. [Set up the workspace](#set-up-the-workspace)
2. If you cloned a while ago, get the latest changes from upstream and update dependencies:
```bash
$ git checkout {{ cookiecutter.main_branch }}
$ git pull upstream {{ cookiecutter.main_branch }}
$ uv sync --all-extras --all-groups
```
3. Create a new topic branch (off the main project development branch) to contain your feature, change, or fix:
```bash
$ git checkout -b <topic-branch-name>
```
4. Make your code changes, following the [Coding rules](#coding-rules)
5. Push your topic branch up to your fork:
```bash
$ git push origin <topic-branch-name>
```
6. [Open a Pull Request](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request) with a clear title and description.

**Tips**:
- For ambitious tasks, open a [draft Pull Request](https://docs.github.com/en/pull-requests/reference/pull-requests#draft-pull-requests) as soon as possible, in order to get feedback and help from the community.
- [Allow {{ cookiecutter.project_distribution_name }} maintainers to make changes to your Pull Request branch](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/allowing-changes-to-a-pull-request-branch-created-from-a-fork). This way, we can rebase it and make some minor changes if necessary. All changes we make will be done in new commit and we'll ask for your approval before merging them.

## Coding rules

### Source code

To ensure consistency and quality throughout the source code, all code modifications must have:
- No [linting](#lint) errors
- A [test](#tests) for every possible case introduced by your code change
- **100%** test coverage
- [Valid commit message(s)](#commit-message-guidelines)
- Documentation for new features
- Updated documentation for modified features

### Documentation

To ensure consistency and quality, all documentation modifications must:
- Refer to brand in [bold](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#styling-text) with proper capitalization, i.e. **GitHub**, **{{ cookiecutter.project_name }}**
- Prefer [tables](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables) over [lists](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#lists) when listing key values, i.e. List of options with their description
- Use [links](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#links) when you are referring to:
  - a **{{ cookiecutter.project_name }}** concept described somewhere else in the documentation, i.e. How to [contribute](CONTRIBUTING.md)
  - a third-party product/brand/service, i.e. Integrate with [GitHub](https://github.com)
  - an external concept or feature, i.e. Create a [GitHub release](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
  - a package or module, i.e. The [`@{{ cookiecutter.__github_path }}`]({{ cookiecutter.__github_url }}) module
- Use the [single backtick `code` quoting](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#quoting-code) for:
  - commands inside sentences, i.e. the `uv` command
  - programming language keywords, i.e. `for`, `with`, `dict`
  - packages or modules, i.e. The [`@{{ cookiecutter.__github_path }}`]({{ cookiecutter.__github_url }}) module
- Use the [triple backtick `code` formatting](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks) for:
  - code examples
  - configuration examples
  - sequence of command lines

### Commit message guidelines

#### Atomic commits

If possible, make [atomic commits](https://en.wikipedia.org/wiki/Atomic_commit), which means:
- a commit should contain exactly one self-contained functional change
- a functional change should be contained in exactly one commit
- a commit should not create an inconsistent state (such as test errors, linting errors, partial fix, feature with documentation etc...)

A complex feature can be broken down into multiple commits as long as each one maintains a consistent state and consists of a self-contained change.

#### Commit message format

Each commit message consists of a **header**, a **body** and a **footer**. The header has a special format that includes a **type**, a **scope** and a **subject**:

```commit
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

The **header** is mandatory and the **scope** of the header is optional.

The **footer** can contain a [closing reference to an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue).

#### Revert

If the commit reverts a previous commit, it should begin with `revert: `, followed by the header of the reverted commit. In the body it should say: `This reverts commit <hash>.`, where the hash is the SHA of the commit being reverted.

#### Type

The type must be one of the following:

| Type         | Description                                                                        |
|--------------|------------------------------------------------------------------------------------|
| **build**    | Changes that affect the build system or external dependencies                      |
| **chore**    | Other changes that don't modify source or test files                               |
| **ci**       | Changes to our CI configuration files and scripts (example scopes: GitHub Actions) |
| **docs**     | Documentation only changes                                                         |
| **feat**     | A new feature                                                                      |
| **fix**      | A bug fix                                                                          |
| **perf**     | A code change that improves performance                                            |
| **refactor** | A code change that neither fixes a bug nor adds a feature                          |
| **revert**   | Reverts a previous commit (see [Revert](#revert))                                  |
| **style**    | Changes that do not affect the meaning of the code (white-space, formatting, etc)  |
| **test**     | Adding missing tests or correcting existing tests                                  |

#### Subject

The subject contains succinct description of the change:

- use the imperative, present tense: "change" not "changed" nor "changes"
- don't capitalize first letter
- no dot (.) at the end

#### Body
Just as in the **subject**, use the imperative, present tense: "change" not "changed" nor "changes".
The body should include the motivation for the change and contrast this with previous behavior.

#### Footer
The footer should contain any information about **Breaking Changes** and is also the place to reference GitHub issues that this commit **Closes**.

**Breaking Changes** should start with the word `BREAKING CHANGE:` with a space or two newlines. The rest of the commit message is then used for this.

#### Examples

```commit
fix(pencil): stop graphite breaking when too much pressure applied
```

```commit
feat(pencil): add 'graphiteWidth' option

Fix #42
```

```commit
perf(pencil): remove graphiteWidth option

BREAKING CHANGE: The graphiteWidth option has been removed.

The default graphite width of 10mm is always used for performance reasons.
```

## Working with the code

### Set up the workspace

[Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the project, configure the remotes and install the dependencies:

```bash
# Clone the repo into the current directory
git clone {{ cookiecutter.__github_url }}

# Navigate to the newly cloned directory
cd {{ cookiecutter.project_distribution_name }}

# Set up the environment. Dev tooling lives in dependency *groups*, which
# `--all-extras` alone does not install, so ask for both.
uv sync --all-extras --all-groups

# Set up pre-commit hooks
uv run pre-commit install
```

Every command below runs through `uv run`, so it uses the project's locked tools; activate `.venv` instead if you prefer to drop the prefix.

### Set up your editor

First of all, don't commit editor-specific configuration. That's personal, and each developer should have it locally ignored, as those files also shouldn't be on the project's `.gitignore`.

Here's a great article on how to do that: [Don't put .idea and .vscode directories to project's .gitignore](https://blog.martinhujer.cz/dont-put-idea-vscode-directories-to-projects-gitignore)

### pre-commit

This repository uses [pre-commit](https://pre-commit.com) to automatically check the changes prior to committing.

It can be run on demand with `uv run pre-commit run`, and optionally on all files with `uv run pre-commit run --all-files`.

Besides the generic file checks, the hooks run Ruff, check `uv.lock` is up to date, spell check with [typos](https://github.com/crate-ci/typos) (add false positives to `[tool.typos]` in `pyproject.toml`) and audit the GitHub workflows with [zizmor](https://docs.zizmor.sh).

### Lint

This repository uses [Ruff](https://docs.astral.sh/ruff) for linting and formatting:

```bash
uv run ruff check --fix
uv run ruff format
```

**Tips**:
- [Set up your editor](#set-up-your-editor) to see linting errors directly in your editor and automatically fix them on save.

### Tests

This repository uses [pytest](https://docs.pytest.org) for writing and running tests.

Before pushing your code changes make sure all **tests pass** and the **coverage is 100%** (line and branch). Docstring examples run as doctests too:

```bash
uv run pytest --cov
```

### Type checking

This repository uses [ty](https://docs.astral.sh/ty) for type checking:

```bash
uv run ty check
```

### Benchmarks

This repository uses [airspeed velocity (`asv`)](https://asv.readthedocs.io) for benchmarks, in `benchmarks/`. Nox runs each benchmark once to check it works; to measure, compare two commits:

```bash
uv run asv machine --yes  # Once per machine
uv run asv continuous {{ cookiecutter.main_branch }} HEAD
```

### Running every check

[Nox](https://nox.thea.codes) runs every check exactly as CI does, on every supported Python version:

```bash
uv run nox
```

Locally, the lint and format sessions fix what they can; in CI (when `CI` is set) they only check, as does the lockfile session.

### Docs

MkDocs Material is used to build the documentation, with mkdocstrings to automatically generate API documentation from docstrings.

```bash
# Build documentation
uv run nox -s docs

# Serve documentation locally with live reload
uv run nox -s docs_serve

# Or use mkdocs directly, from the repository root -- `mkdocs.yml` lives
# there, not in `docs/`.
uv run mkdocs build --strict  # Build HTML docs
uv run mkdocs serve           # Serve with live reload at http://127.0.0.1:8000
```

### Requirements

Read the uv docs [here](https://docs.astral.sh/uv/).

All requirements should be listed in the `pyproject.toml` file, under their respective sections.

To add a new requirement, run `uv add <package name>`.

To see which installed packages are outdated, run `uv tree --outdated`.

To update installed packages, run `uv lock --upgrade-package <package name>`.

Always lock the dependencies after updating them, by running `uv lock`.

uv only resolves releases at least a week old (`exclude-newer` in `pyproject.toml`), so a freshly published version, possibly a compromised one, cannot reach `uv.lock` before it has had time to be caught. Version floors must name releases older than a week. To take an urgent fix sooner, exempt just that package, e.g. `exclude-newer-package = { <package name> = false }` under `[tool.uv]`, and remove the exemption once the release is a week old.

[Dependabot](https://docs.github.com/en/code-security/dependabot) opens weekly grouped updates for the dependencies, the pre-commit hooks and the GitHub Actions. The Ruff pre-commit hooks run the version locked in `uv.lock`, so there is nothing else to keep in step.

### Updating template

[cruft](https://github.com/cruft/cruft/) can be used to update the project with the latest version of the template.

```bash
cruft update
```

After updating, the versions of dependencies might change, so use `uv sync --all-extras --all-groups`.

## Add yourself as a contributor

To add yourself as a contributor, follow the [bot usage instructions](https://allcontributors.org/docs/en/bot/usage).
