"""Testing for {{ cookiecutter.project_distribution_name }}."""

from pytest_benchmark.fixture import BenchmarkFixture  # type: ignore[import]

from {{cookiecutter.project_slug}} import make_greeting


def test_make_greeting(benchmark: BenchmarkFixture) -> None:
    """Test `make_greeting`."""
    result = benchmark(make_greeting, "{{cookiecutter.full_name}}")
    assert result == "Hello, {{cookiecutter.full_name}}. Welcome to your new project!"
