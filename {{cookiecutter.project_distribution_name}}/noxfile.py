"""Nox file for automation."""

from typing import Iterable, Optional

import nox

python_versions = ["3.8", "3.9", "3.10", "3.11"]


def install(
    session: nox.Session,
    *,
    groups: Iterable[str],
    root: bool = True,
    only: Optional[bool] = None,
    extras: bool = False,
) -> None:
    """Install the dependency groups using Poetry."""
    if only is None:
        only = not root

    command = [
        "poetry",
        "install",
        "--sync",
        f'--{"only" if only else "with"}={",".join(groups)}',
    ]
    if not root:
        command.append("--no-root")
    if extras:
        command.append("--all-extras")

    session.run_always(*command, external=True)


@nox.session(python=python_versions[-1])
def fix_files(session: nox.Session) -> None:
    """Fix files."""
    install(session, groups=["linting"], root=False)
    session.run("ruff", "check", "--fix-only", ".")
    session.run("black", ".")


@nox.session(python=python_versions)
def lint_files(session: nox.Session) -> None:
    """Lint files."""
    install(session, groups=["linting"], root=False)
    session.run("ruff", "check", ".")
    session.run("black", "--check", ".")


@nox.session(python=python_versions)
def type_check_code(session: nox.Session) -> None:
    """Type-check code."""
    install(
        session,
        groups=["main", "typing", "stubs"],
        root=True,
        only=True,
        extras=True,
    )
    # mypy --install-types
    session.run("mypy")


@nox.session(python=python_versions)
def test_code(session: nox.Session) -> None:
    """Test code."""
    install(session, groups=["main", "tests"], root=True, only=True, extras=True)
    session.run("pytest")
