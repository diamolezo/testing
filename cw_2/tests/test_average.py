import pytest
from cw_2.src.cw_2 import average


@pytest.mark.parametrize('value, result',
                         [
                             ([0, 0, 0], 0.0),
                             ([1, 0, 3], 1.3),
                             ([-1, 0, -3], -1.3),
                             ([1, 1, 1], 1.0),
                             ([3, 2, 1], 2.0),
                             ([1, 2, 3], 2.0),
                             ([1.0, 2.5, 3.9], 2.5),
                             ([1, 2, 3], 2.0),
                             ([1, 2.5, 3], 2.2),
                             ([1], 1.0)
                         ])

def test_positive(value, result):
    assert average(value) == result

@pytest.mark.parametrize('value, result',
                         [
                             (['qqq', 'www', 'eee'], pytest.raises(TypeError)),
                             (['111', '222', '333'], pytest.raises(TypeError)),
                             (['*', '&', '^'], pytest.raises(TypeError)),
                             ([1, '&', '^'], pytest.raises(TypeError)),
                             ([9, '&', 99.99], pytest.raises(TypeError)),
                             ([], pytest.raises(ValueError))
                         ])

def test_negative(value, result):

    with result:
        assert average(value) == result