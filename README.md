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

[cruft]: https://github.com/cruft/cruft/
[cookiecutter]: https://github.com/cookiecutter/cookiecutter
