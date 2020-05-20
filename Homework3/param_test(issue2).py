import pytest
import morse


@pytest.mark.parametrize('test, exp', [
    ('-..', 'D'),
    ('-..-.', '/'),
    ('.----', '1'),
    ('.--- --', 'JM')
])
def test_decode(test, exp):
    assert morse.decode(test) == exp
    
