import pytest
from age_calc.calc import checks_below_value

def test_checks_below_value_raises_ValueError_if_not_below_value():
    with pytest.raises(ValueError):
        checks_below_value(3000, 2022)