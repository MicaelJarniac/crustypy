"""Benchmarking for {{cookiecutter.project_distribution_name}}."""

from {{cookiecutter.project_slug}} import make_greeting


class TimeSuite:
    """A benchmark suite for timing {{cookiecutter.project_distribution_name}}."""

    def setup(self) -> None:
        """Set up the benchmark by initializing the `name` attribute."""
        self.name = "{{cookiecutter.full_name}}"

    def time_make_greeting(self) -> None:
        """Benchmark the `make_greeting` function for its execution time."""
        make_greeting(self.name)


class MemSuite:
    """A benchmark suite for measuring the memory usage of {{cookiecutter.project_distribution_name}}."""

    def setup(self) -> None:
        """Set up the benchmark by initializing the `name` attribute."""
        self.name = "{{cookiecutter.full_name}}"

    def mem_make_greeting(self) -> str:
        """Benchmark the `make_greeting` function for its memory usage."""
        return make_greeting(self.name)
