import pytest
from cw_1.src.calculator import Calculator

test_positive = [(-8, -4, -1),
                      (44, 88, 234),
                      (-17.5, -1.9, -97.2),
                      (17.5, 1.9, 97.2),
                      (-17.5, 1.9, 97.2),
                      (-7, 9, 2),
                      (0, 0, 0),
                      (0, 7, 7),
                      (0, -9, -9),
                      (0, -2.8, -2.8),
                      (0, 3.4, 3.4)]

@pytest.mark.parametrize('value_left, value_right, result', test_positive)
def test_add_positive(value_left, value_right, result):
    calc = Calculator()
    assert calc.add(value_left, value_right) == result


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
        assert calc.add(value_left, value_right) == result