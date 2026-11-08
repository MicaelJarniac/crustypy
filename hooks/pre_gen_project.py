"""Reject answers that would bake a broken project.

Cookiecutter pastes the answers verbatim into Python, TOML, YAML and JSON, so a
stray double quote, or a slug that is not an importable name, produces files
that do not parse or a package that cannot be imported. Failing here, before
any file is written, explains the problem instead.
"""

__all__: tuple[str, ...] = ()

import json
import keyword
import re
import sys
from typing import Any, Final

# Rendered through `tojson`, so no answer can break out of this literal.
CONTEXT: Final[dict[str, Any]] = json.loads(r"""{{ cookiecutter | tojson }}""")

# Ends up inside double-quoted strings in Python, TOML, YAML and JSON.
TEXT: Final = re.compile(r'[^"\\\x00-\x1f\x7f]+')
PATTERNS: Final = {
    "full_name": TEXT,
    "email": re.compile(r'[^@\s"\\]+@[^@\s"\\]+'),
    "github_username": re.compile(r"[A-Za-z0-9](?:-?[A-Za-z0-9]){0,38}"),
    "project_name": TEXT,
    "project_slug": re.compile(r"[a-z_][a-z0-9_]*"),
    # A normalized distribution name; it doubles as the Read the Docs subdomain.
    "project_distribution_name": re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*"),
    "project_short_description": TEXT,
    "version": re.compile(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.]+)?"),
    "main_branch": re.compile(r"[A-Za-z0-9._/-]+"),
    "shields_url": re.compile(r'https?://[^\s"\\]*[^/\s"\\]'),
    "discord_invite": re.compile(r"[A-Za-z0-9-]*"),
}
HINTS: Final = {TEXT: 'no double quotes ("), backslashes or line breaks'}
# Top-level names in the generated project that the package must not shadow.
RESERVED_SLUGS: Final = frozenset({"benchmarks", "docs", "noxfile", "tests"})


def problems() -> list[str]:
    """Describe every answer that would bake a broken project."""
    found = [
        f"{key}={CONTEXT[key]!r}: {HINTS.get(pattern, f'must match {pattern.pattern}')}"
        for key, pattern in PATTERNS.items()
        if not pattern.fullmatch(CONTEXT[key])
    ]
    slug = CONTEXT["project_slug"]
    if keyword.iskeyword(slug) or keyword.issoftkeyword(slug):
        found.append(f"project_slug={slug!r}: is a Python keyword")
    if slug in sys.stdlib_module_names or slug in RESERVED_SLUGS:
        found.append(f"project_slug={slug!r}: would shadow the {slug!r} module")
    return found


if found := problems():
    sys.exit("Cannot bake the project:\n" + "\n".join(f"  - {p}" for p in found))
