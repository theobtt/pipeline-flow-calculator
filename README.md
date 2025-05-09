# Pipeline Flow Calculator

A simple Python tool to calculate Reynolds number, Darcy friction factor, and pressure drop for pipe flow systems. 
Ideal for chemical/process engineers and anyone needing quick fluid dynamics estimates via CLI or a web interface.

---

## Features

- Compute **Reynolds number** (Re = rho.u.D / mu)  
- Estimate **Darcy friction factor** using the laminar flow formula 
- Calculate **pressure drop** via the Darcy–Weisbach equation  
- Optional **Streamlit** GUI for interactive input 
- Automated **pytest** suite to validate core calculations

---

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/theobtt/pipeline-flow-calculator.git
   cd pipeline-flow-calculator
