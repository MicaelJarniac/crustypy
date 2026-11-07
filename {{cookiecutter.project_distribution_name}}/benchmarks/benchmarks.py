"""Benchmarking for {{cookiecutter.project_distribution_name}}."""

__all__: tuple[str, ...] = ("MemSuite", "TimeSuite")

from {{cookiecutter.project_slug}} import make_greeting


class TimeSuite:
    """Benchmarks for execution time."""

    def setup(self) -> None:
        """Set up the benchmark by initializing the `name` attribute."""
        self.name = "World"

    def time_make_greeting(self) -> None:
        """Benchmark the `make_greeting` function for its execution time."""
        make_greeting(self.name)


class MemSuite:
    """Benchmarks for memory usage."""

    def setup(self) -> None:
        """Set up the benchmark by initializing the `name` attribute."""
        self.name = "World"

    def mem_make_greeting(self) -> str:
        """Benchmark the `make_greeting` function for its memory usage."""
        return make_greeting(self.name)
