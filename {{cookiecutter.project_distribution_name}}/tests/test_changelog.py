"""Guard the contract between docs/CHANGELOG.md and python-semantic-release.

PSR runs the changelog in ``update`` mode: it splits the existing file on the
``insertion_flag`` and writes the new release between the two halves. If the
flag is missing, the file is written back unchanged and nothing warns about it,
so releases silently go unrecorded. These tests fail the build instead.
"""

__all__: tuple[str, ...] = ()

import tomllib
from pathlib import Path
from typing import Final, Literal, TypedDict, cast

import pytest

REPO_ROOT: Final = Path(__file__).resolve().parent.parent
PYPROJECT: Final = REPO_ROOT / "pyproject.toml"
RELEASE_HEADING: Final = "\n## v"


class _DefaultTemplates(TypedDict):
    changelog_file: str


class _ChangelogConfig(TypedDict):
    mode: Literal["init", "update"]
    insertion_flag: str
    default_templates: _DefaultTemplates


class _SemanticRelease(TypedDict):
    changelog: _ChangelogConfig


class _Tool(TypedDict):
    semantic_release: _SemanticRelease


class _Project(TypedDict):
    version: str


class _PyProject(TypedDict):
    """The parts of pyproject.toml these tests read."""

    project: _Project
    tool: _Tool


@pytest.fixture(scope="module")
def pyproject() -> _PyProject:
    """The parsed pyproject.toml."""
    with PYPROJECT.open("rb") as fh:
        return cast("_PyProject", tomllib.load(fh))


@pytest.fixture(scope="module")
def changelog_config(pyproject: _PyProject) -> _ChangelogConfig:
    """The ``[tool.semantic_release.changelog]`` table."""
    return pyproject["tool"]["semantic_release"]["changelog"]


@pytest.fixture(scope="module")
def changelog_text(changelog_config: _ChangelogConfig) -> str:
    """Contents of the changelog file PSR is configured to write."""
    changelog_file = changelog_config["default_templates"]["changelog_file"]
    return (REPO_ROOT / changelog_file).read_text(encoding="utf-8")


def test_changelog_mode_is_pinned_to_update(
    changelog_config: _ChangelogConfig,
) -> None:
    """The mode is explicit, so a future PSR default flip cannot change behavior."""
    assert changelog_config["mode"] == "update"


def test_changelog_carries_the_insertion_flag_below_the_title(
    changelog_config: _ChangelogConfig, changelog_text: str
) -> None:
    """Update mode splices new releases in at the flag, so it must be present.

    It must also sit directly under the title: PSR emits the header, the flag,
    then the newest release, so anything between the flag and the first
    ``## v`` heading would be pushed below every future entry. Before the first
    release there is no heading yet, so nothing may follow the flag at all.
    """
    flag = changelog_config["insertion_flag"]
    assert changelog_text.count(flag) == 1, "exactly one insertion flag expected"
    flag_at = changelog_text.index(flag)
    first_release_at = changelog_text.find(RELEASE_HEADING)
    if first_release_at == -1:
        first_release_at = len(changelog_text)
    assert flag_at < first_release_at, "flag must precede the newest release"
    assert changelog_text[:flag_at].strip() == "# CHANGELOG", (
        "only the title belongs above the insertion flag"
    )
    assert changelog_text[flag_at + len(flag) : first_release_at].strip() == "", (
        "nothing belongs between the insertion flag and the newest release"
    )


def test_current_version_is_recorded(
    pyproject: _PyProject, changelog_text: str
) -> None:
    """The released version in pyproject.toml has a changelog heading.

    PSR bumps the version and writes the changelog in the same release commit,
    so a version without a heading means the changelog step silently did
    nothing. Reading the version from pyproject.toml rather than git tags keeps
    the test meaningful in a shallow checkout.

    A freshly generated project has not released yet, so the check starts once
    the changelog holds its first release.
    """
    if RELEASE_HEADING not in changelog_text:
        pytest.skip("nothing released yet")
    version = pyproject["project"]["version"]
    assert f"{RELEASE_HEADING}{version} (" in changelog_text, (
        f"v{version} is missing from the changelog"
    )
