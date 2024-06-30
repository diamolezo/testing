import pytest
from cw_1.src.calculator import Calculator

test_positive = [(8, 4, 4),
                 (89, 57, 32),
                 (-24.5, -12.7, -11.8),
                 (24.7, 14.7, 10),
                 (-12.4, 45.4, -57.8),
                 (-47, 89, -136),
                 (0, 0, 0),
                 (0, 67, -67,),]

@pytest.mark.parametrize('value_left, value_right, result', test_positive)
def test_add_positive(value_left, value_right, result):
    calc = Calculator()
    assert calc.subtract(value_left, value_right) == result


test_negative = [(None, None, pytest.raises(TypeError)),
                      (None, str, pytest.raises(TypeError)),
                      (None, bool, pytest.raises(TypeError)),
                      (None, int, pytest.raises(TypeError)),
                      (None, float, pytest.raises(TypeError)),
                      (None, list, pytest.raises(TypeError)),
                      (str, int, pytest.raises(TypeError)),
                      (str, float, pytest.raises(TypeError)),
                      (str, str, pytest.raises(TypeError)),
                      (str, list, pytest.raises(TypeError)),
                      (bool, int, pytest.raises(TypeError)),
                      (bool, float, pytest.raises(TypeError)),
                      (bool, list, pytest.raises(TypeError)),
                      (int, list, pytest.raises(TypeError))]

@pytest.mark.parametrize('value_left, value_right, result', test_negative)
def test_add_negative(value_left, value_right, result):
    calc = Calculator()
    with result:
        assert calc.subtract(value_left, value_right) == result