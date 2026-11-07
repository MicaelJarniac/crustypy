# CrustyPy
Bake your Python projects to perfection.

A basic Python project template for [Cookiecutter][cookiecutter].

To see what a project generated with this template looks like, check out [crustypy-instance](https://github.com/MicaelJarniac/crustypy-instance).

## Usage

### With cruft (recommended)
Requires [cruft][cruft].
> [!NOTE]
> Install cruft with the optional `pyproject` extra, e.g. `uv tool install 'cruft[pyproject]'`.

```bash
cruft create https://github.com/MicaelJarniac/crustypy
```

Or without installing it:

```bash
uvx --from 'cruft[pyproject]' cruft create https://github.com/MicaelJarniac/crustypy
```

### With Cookiecutter
[Cookiecutter][cookiecutter] can also be used, but it'll result in fewer features.

```bash
uvx cookiecutter gh:MicaelJarniac/crustypy
```

### After generating
Before the first push, create the lockfile and commit it:

```bash
uv lock
git add uv.lock
```

To publish to PyPI, add a [trusted publisher](https://docs.pypi.org/trusted-publishers/) for workflow `ci.yml` and environment `pypi`.

> [!IMPORTANT]
> Fill in the environment. PyPI marks it optional, but without it every job in `ci.yml` could publish, not just the release job.
> Then, under *Settings → Environments → pypi*, limit deployment branches to `main` (and `rc` if you use it).

## Updating an existing project
With cruft, run `cruft update` and review the diff. Some updates need manual steps on GitHub or PyPI; they're listed below, newest first.

### cruft updates `tests/test_changelog.py` (November 2026)
`[tool.cruft] skip` used to list all of `tests`, so template changes to `tests/test_changelog.py` never reached existing projects. It now lists only the example test. cruft reads the skip list from your project before updating, so the first `cruft update` after this one is the first to touch `tests/test_changelog.py`.

### Releases moved into `ci.yml` (November 2026)
`semantic-release.yml` and `codecov_action.yml` are gone. Releasing and the Codecov upload are now jobs in `ci.yml`, and publishing runs in a `pypi` environment. Before the first release after updating:

1. On PyPI, edit the project's trusted publisher (*Manage → Publishing*): set the workflow to `ci.yml` and the environment to `pypi`.
2. On GitHub, create the `pypi` environment (*Settings → Environments*) and limit its deployment branches to the release branches.
3. Delete `.python-versions` (Nox now reads the versions from the classifiers) and `docs/wordlist.txt` (replaced by typos) if cruft left them behind.
4. If `docs/CHANGELOG.md` conflicts, keep your release history and put `<!-- version list -->` on the line right under the title.
5. Run `uv lock --upgrade`. A plain `uv lock` keeps old pins that predate Python 3.15 (an old `typing_extensions` breaks pytest there).

Until step 1 is done, the release job tags and creates the GitHub release, but the PyPI upload fails.

[cruft]: https://github.com/cruft/cruft/
[cookiecutter]: https://github.com/cookiecutter/cookiecutter
