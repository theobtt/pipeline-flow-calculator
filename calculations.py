import math

def reynolds_number(rho, velocity, diameter, mu):
    """
    Calculate Reynolds number:
      Re = ρ * u * D / μ
    """
    return rho * velocity * diameter / mu

def friction_factor(re, relative_roughness=0.0):
    """
    Estimate Darcy friction factor:
      – Laminar (Re < 2300): f = 64 / Re
      – Turbulent: Haaland equation
    """
    if re < 2300:
        return 64.0 / re
    return (-1.8 * math.log10((relative_roughness / 3.7) + (6.9 / re))) ** -2

def pressure_drop(f, length, diameter, rho, velocity):
    """
    Darcy–Weisbach pressure drop:
      ΔP = f * (L / D) * (ρ * u^2 / 2)
    """
    return f * (length / diameter) * (rho * velocity**2 / 2.0)
