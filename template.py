"""A basic template for any function."""
from typing import Any
from cs110 import expect, summarize

def template(x: Any) -> Any:
    """A functiont that returns what it was given."""
    return x

expect(template("1"), equals="1", description="Return anything.")
summarize()