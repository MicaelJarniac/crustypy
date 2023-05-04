"""Nox file for automation."""

import nox

python_versions = ["3.8", "3.9", "3.10", "3.11"]
constraints = ("-c", "constraints.txt")


@nox.session(python=python_versions[-1])
def format_files(session: nox.Session) -> None:
    """Format files."""
    session.install(*constraints, "ruff", "black")
    session.run("ruff", "check", "--fix-only", ".")
    session.run("black", ".")


@nox.session(python=python_versions[-1])
def lint_files(session: nox.Session) -> None:
    """Lint files."""
    session.install(*constraints, "ruff")
    session.run("ruff", "check", ".")


@nox.session(python=python_versions)
def type_check_code(session: nox.Session) -> None:
    """Type-check code."""
    session.install(*constraints, ".[dev]")
    session.run("mypy")


@nox.session(python=python_versions)
def test_code(session: nox.Session) -> None:
    """Test code."""
    session.install(*constraints, ".[tests]")
    session.run("pytest")
