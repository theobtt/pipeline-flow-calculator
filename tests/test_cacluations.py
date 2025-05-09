import pytest
from calculations import reynolds_number, friction_factor, pressure_drop

def test_reynolds_number():
    # ρ=1000, u=1, D=0.1, μ=0.001 => Re = 1000*1*0.1/0.001 = 100000
    assert pytest.approx(reynolds_number(1000, 1, 0.1, 0.001), rel=1e-3) == 1e5

def test_friction_factor_laminar():
    f = friction_factor(1000)
    assert pytest.approx(f, rel=1e-4) == 64/1000

def test_friction_factor_turbulent():
    f = friction_factor(1e5, 1e-5)
    assert f > 0  # basic sanity check

def test_pressure_drop():
    f = 0.02
    dp = pressure_drop(f, 10, 0.1, 1000, 1)
    expected = f * (10/0.1) * (1000 * 1**2 / 2)
    assert pytest.approx(dp, rel=1e-4) == expected
