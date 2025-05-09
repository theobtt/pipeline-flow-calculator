import argparse
from calculations import reynolds_number, friction_factor, pressure_drop

def parse_args():
    p = argparse.ArgumentParser(
        description="Pipeline Flow Calculator: Reynolds, friction factor, ΔP"
    )
    p.add_argument("--rho", type=float, required=True, help="Fluid density (kg/m³)")
    p.add_argument("--mu", type=float, required=True, help="Viscosity (Pa·s)")
    p.add_argument("--diameter", type=float, required=True, help="Pipe diameter (m)")
    p.add_argument("--length", type=float, required=True, help="Pipe length (m)")
    p.add_argument("--velocity", type=float, required=True, help="Flow velocity (m/s)")
    p.add_argument(
        "--roughness",
        type=float,
        default=0.0,
        help="Relative roughness (ε/D)",
    )
    return p.parse_args()

def main():
    args = parse_args()
    Re = reynolds_number(args.rho, args.velocity, args.diameter, args.mu)
    f = friction_factor(Re, args.roughness)
    dp = pressure_drop(f, args.length, args.diameter, args.rho, args.velocity)

    print(f"Reynolds number:         {Re:.0f}")
    print(f"Darcy friction factor:   {f:.5f}")
    print(f"Pressure drop over {args.length} m: {dp:.2f} Pa")

if __name__ == "__main__":
    main()
