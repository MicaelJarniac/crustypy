from loguru import logger


def make_greeting(name: str) -> str:
    """Make greeting message.

    This function is an example, and should be deleted once
    you're familiar with how the project is structured.

    Make sure to also remove this function from the `__init__.py`
    file, as well as from the tests.

    Args:
        name: The name of the person to greet.

    Returns:
        A greeting message for that person.

    Examples:
        >>> print(make_greeting("Foo"))
        Hello, Foo. Welcome to your new project!
    """
    logger.debug(f"Welcoming {name}.")
    return f"Hello, {name}. Welcome to your new project!"
