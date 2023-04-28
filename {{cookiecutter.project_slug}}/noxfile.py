"""Nox file for automation."""

import nox

python_versions = ["3.7", "3.8", "3.9", "3.10"]
deps = {
    "ruff": "ruff==0.0.263",
    "black": "black==23.3.0",
}


@nox.session(python=python_versions[-1], reuse_venv=True)
def format_files(session: nox.Session) -> None:
    """Format files."""
    session.install(deps["ruff"], deps["black"])
    session.run("ruff", "check", "--fix-only", ".")
    session.run("black", ".")


@nox.session(python=python_versions[-1], reuse_venv=True)
def lint_files(session: nox.Session) -> None:
    """Lint files."""
    session.install(deps["ruff"])
    session.run("ruff", "check", ".")


@nox.session(python=python_versions, reuse_venv=True)
def type_check_code(session: nox.Session) -> None:
    """Type-check code."""
    session.install(".[dev]")
    session.run("mypy")


@nox.session(python=python_versions)
def test_code(session: nox.Session) -> None:
    """Test code."""
    session.install(".[tests]")
    session.run("pytest")
