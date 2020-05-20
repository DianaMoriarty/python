import pytest
import one_hot_encoder


def test_empty():
    assert one_hot_encoder.fit_transform([]) == []


def test_arg():
    input = one_hot_encoder.fit_transform(['N', 'o'])
    res = [('N', [0, 1]), ('o', [1, 0]), ]
    assert input == res


def test_arg2():
    input = one_hot_encoder.fit_transform(['X', 'X', 'X'])
    res = [('X', [1]), ('X', [1]), ('X', [1])]
    assert input == res


def test_exception():
    with pytest.raises(TypeError):
        one_hot_encoder.fit_transform(123)
