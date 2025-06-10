import pytest
from src.utils import converter_from_json


@pytest.mark.parametrize('filename, expected', [('', 0), ('../data/operations.json', 101)])
def test_converter_from_json(filename: str, expected: int) -> None:
    assert len(converter_from_json(filename)) == expected
