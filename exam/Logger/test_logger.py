import pytest
import exam


def test_number():
    t = exam.incr(100)
    assert t == 101


def test_exception():
    with pytest.raises(TypeError):
        exam.incr()
