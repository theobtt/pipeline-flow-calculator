import streamlit as st
from calculations import reynolds_number, friction_factor, pressure_drop

st.title("Pipeline Flow Calculator")

rho = st.number_input(
    "Fluid density (kg/m³)",
    value=1000.0,
    format="%.2f"       # two decimals (e.g. 1000.00)
)
mu = st.number_input(
    "Dynamic viscosity (Pa·s)",
    value=0.001,
    format="%.6f"       # six decimals (e.g. 0.001000)
)
diameter = st.number_input(
    "Pipe diameter (m)",
    value=0.05,
    format="%.4f"       # four decimals
)
length = st.number_input(
    "Pipe length (m)",
    value=10.0,
    format="%.2f"
)
velocity = st.number_input(
    "Fluid velocity (m/s)",
    value=1.0,
    format="%.3f"
)
roughness = st.number_input(
    "Relative roughness (ε/D)",
    value=0.0,
    format="%.6f"
)

if st.button("Calculate"):
    Re = reynolds_number(rho, velocity, diameter, mu)
    f  = friction_factor(Re, roughness)
    dp = pressure_drop(f, length, diameter, rho, velocity)
    st.write(f"**Reynolds number:** {Re:.0f}")
    st.write(f"**Friction factor:** {f:.5f}")
    st.write(f"**Pressure drop:** {dp:.2f} Pa over {length} m")
