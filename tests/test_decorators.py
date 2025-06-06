import pytest

from src.decorators import log


coll = [
    (5, 1, 'division ok. Result: 5.0. Input: (5, 1), {}'),
    (5, 0, 'erorr: None. Input: (5, 0), {}')
]


@pytest.mark.parametrize('a, b, expected', coll)
def test_log(a: int, b: int, expected: str, capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def division(a: int, b: int) -> float:
        return a / b
    division(a, b)
    captured = capsys.readouterr()
    assert captured.out[54:] == expected + '\n'
