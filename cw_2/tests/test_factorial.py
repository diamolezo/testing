import pytest
from cw_2.src.cw_2 import factorial


@pytest.mark.parametrize('value, result',
                         [
                             (4, 24),
                             (5, 120),
                             (10, 3628800),
                             (15, 1307674368000),
                         ])

def test_positive(value, result):
    assert factorial(value) == result

@pytest.mark.parametrize('value, result',
                         [
                             (-10, pytest.raises(ValueError)),
                             (-5.0, pytest.raises(ValueError)),
                             (None, pytest.raises(TypeError)),
                             (True, pytest.raises(AssertionError)),
                         ])

def test_negative(value, result):

    with result:
        assert factorial(value) == result