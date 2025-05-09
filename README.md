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

1. **Download the zip archive, extract and navigate to this path in terminal**  
   ```bash
   cd path/to/pipeline-flow-calculator-main

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate (macOS/Linux)
   venv\Scripts\Activate.ps1 (Windows)
3. **Install required packages**
   ```bash
   pip install -r requirements.txt
4. **Launch the app**
   ```bash
   streamlit run app.py
   
