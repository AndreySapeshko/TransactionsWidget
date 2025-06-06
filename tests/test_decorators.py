import pytest

from src.decorators import log


@pytest.mark.parametrize('a, b, expected', [(5, 1, 'division ok. Result: 5.0. Input: (5, 1), {}\n'), (5, 0, 'erorr: None. Input: (5, 0), {}\n')])
def test_log(a: int, b: int, expected: str, capsys):
    @log()
    def division(a, b):
        return a / b
    division(a, b)
    captured = capsys.readouterr()
    assert captured.out[54:] == expected
