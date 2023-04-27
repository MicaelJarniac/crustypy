"""Nox file for automation."""

import nox

python_versions = ["3.7", "3.8", "3.9", "3.10"]


@nox.session(python=python_versions[-1], reuse_venv=True)
def format_files(session: nox.Session) -> None:
    """Format files."""
    session.install("-r", "requirements-dev.txt")
    session.run("ruff", "check", "--fix-only", ".")
    session.run("black", ".")


@nox.session(python=python_versions[-1], reuse_venv=True)
def lint_files(session: nox.Session) -> None:
    """Lint files."""
    session.install("-r", "requirements-dev.txt")
    session.run("ruff", "check", ".")


@nox.session(python=python_versions, reuse_venv=True)
def typecheck_code(session: nox.Session) -> None:
    """Typecheck code."""
    session.install("-r", "requirements-dev.txt")
    session.install(".")
    session.run("mypy")


@nox.session(python=python_versions)
def test_code(session: nox.Session) -> None:
    """Test code."""
    session.install(".")
    session.install("pytest")
    session.run("pytest")
