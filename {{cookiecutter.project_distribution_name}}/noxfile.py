"""Nox file for automation."""

__all__: tuple[str, ...] = ()

import os
from pathlib import Path
from typing import TYPE_CHECKING, Final

import nox

if TYPE_CHECKING:
    from collections.abc import Iterable

nox.options.default_venv_backend = "uv"

ROOT: Final = Path(__file__).parent
PYPROJECT: Final = nox.project.load_toml(ROOT / "pyproject.toml")
# Every supported version comes from the `Programming Language :: Python :: 3.x`
# classifiers, and the default one from `.python-version`.
PYTHON_VERSIONS: Final = nox.project.python_versions(PYPROJECT)
PYTHON_VERSION: Final = (ROOT / ".python-version").read_text().strip()
# CI checks instead of fixing, so a run never passes by rewriting files nobody
# commits. Locally, sessions fix in place.
CI: Final = os.environ.get("CI", "").lower() not in {"", "0", "false", "no"}
# pre-commit hooks that duplicate a dedicated session (lint_files,
# format_files, lock_dependencies), skipped when nox runs pre-commit.
DEDICATED_SESSION_HOOKS: Final = ("ruff-check", "ruff-format", "uv-lock")


def install(
    session: nox.Session,
    *,
    groups: Iterable[str],
    root: bool = True,
    extras: bool = False,
) -> None:
    """Install the dependency groups using uv."""
    command = [
        "uv",
        "sync",
        "--frozen",
        "--no-default-groups",
        f"--python={session.virtualenv.location}",
        *(f"--{'group' if root else 'only-group'}={group}" for group in groups),
    ]
    if extras:
        command.append("--all-extras")

    session.run_install(
        *command, env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location}
    )


@nox.session(python=PYTHON_VERSION)
def pre_commit(session: nox.Session) -> None:
    """Run pre-commit."""
    install(session, groups=["pre-commit"], root=False)
    session.run(
        "pre-commit",
        "run",
        "--all-files",
        "--show-diff-on-failure",
        "--hook-stage=manual",
        # Their own sessions already run these.
        env={"SKIP": ",".join(DEDICATED_SESSION_HOOKS)},
    )


@nox.session(python=False)
def lock_dependencies(session: nox.Session) -> None:
    """Lock the dependencies, or check the lockfile is up to date in CI."""
    session.run("uv", "lock", *(["--check"] if CI else []), external=True)


@nox.session(python=PYTHON_VERSION)
def lint_files(session: nox.Session) -> None:
    """Lint files, fixing what can be fixed outside CI."""
    install(session, groups=["linting"], root=False)
    # In CI, report as GitHub annotations so errors show inline on the PR.
    session.run(
        "ruff", "check", ".", *(["--output-format=github"] if CI else ["--fix"])
    )


@nox.session(python=PYTHON_VERSION)
def format_files(session: nox.Session) -> None:
    """Format files, or check their formatting in CI."""
    install(session, groups=["linting"], root=False)
    session.run("ruff", "format", *(["--check", "--diff"] if CI else []))


@nox.session(python=PYTHON_VERSIONS)
def type_check_code(session: nox.Session) -> None:
    """Type-check code."""
    install(session, groups=["typing"], root=True, extras=True)
    session.run("ty", "check")


@nox.session(python=PYTHON_VERSIONS)
def test_code(session: nox.Session) -> None:
    """Test code, with coverage."""
    install(session, groups=["tests"], root=True, extras=True)
    session.run("pytest", "--cov", "--cov-report=term", "--cov-report=xml")


@nox.session(python=PYTHON_VERSION)
def docs(session: nox.Session) -> None:
    """Build documentation with MkDocs."""
    install(session, groups=["docs"], root=True)
    session.run("mkdocs", "build", "--strict")


@nox.session(python=PYTHON_VERSION, default=False)
def docs_serve(session: nox.Session) -> None:
    """Serve documentation locally with live reload."""
    install(session, groups=["docs"], root=True)
    session.run("mkdocs", "serve")
