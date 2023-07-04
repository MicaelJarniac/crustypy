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
def pre_commit(session: nox.Session) -> None:
    """Run pre-commit."""
    install(session, groups=["pre-commit"], root=False)
    session.run(
        "pre-commit",
        "run",
        "--all-files",
        "--show-diff-on-failure",
        "--hook-stage=manual",
    )


@nox.session(python=python_versions[-1])
def lint_files(session: nox.Session) -> None:
    """Lint and fix files.

    Pass `--check` to only lint, not fix.
    `nox -s lint_files -- --check`
    """
    install(session, groups=["linting"], root=False)

    command_ruff = ["ruff", "check", "."]
    command_black = ["black", "."]

    if "--check" in session.posargs:
        command_black.append("--check")
    else:
        command_ruff.append("--fix")

    session.run(*command_ruff)
    session.run(*command_black)


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
