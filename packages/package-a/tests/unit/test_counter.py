import pytest

from package_a.counter import count_charcaters


@pytest.mark.parameterize(
        "given, expected", [
            ("foo", {"f": 1, "o": 2}),
            ("bar", {"b": 1, "a": 1, "r": 1})
        ]
)
def test_count_characters(given: str, expected: dict[str, int]) -> None:
    assert count_charcaters(given) == expected