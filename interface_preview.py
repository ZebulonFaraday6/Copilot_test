"""
GUI Calculator Interface Preview
This script generates a preview/mockup showing the calculator layout.
"""

def print_gui_layout():
    """Print ASCII art representation of the GUI calculator."""
    
    gui_layout = """
╔══════════════════════════════════════════════════════════════════╗
║                CASIO FX-991 CN X CALCULATOR                      ║
╠══════════════════════════════════════════════════════════════════╣
║  File   Mode   Tools                                       Help  ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  History:                                                        ║
║  ┌────────────────────────────────────────────────────────┐    ║
║  │ sin(45) = 0.7071067812                                 │    ║
║  │ sqrt(16) = 4                                           │    ║
║  │ 2**3 = 8                                               │    ║
║  └────────────────────────────────────────────────────────┘    ║
║                                                                  ║
║  ┌────────────────────────────────────────────────────────┐    ║
║  │                                                      0 │    ║
║  └────────────────────────────────────────────────────────┘    ║
║                                                                  ║
║  ┌────────────────────────────────────────────────────────┐    ║
║  │                                                        │    ║
║  └────────────────────────────────────────────────────────┘    ║
║                                                                  ║
║  Angle Mode:  ⦿ Deg   ○ Rad   ○ Grad                           ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║   ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐       ║
║   │shift │ │ mode │ │clear │ │ del  │ │  (   │ │  )   │       ║
║   └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘       ║
║                                                                  ║
║   ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐       ║
║   │  x²  │ │  √   │ │  ^   │ │ log  │ │  ln  │ │  ÷   │       ║
║   └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘       ║
║                                                                  ║
║   ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌────┐║
║   │ sin  │ │ cos  │ │ tan  │ │  7   │ │  8   │ │  9   │ │  × │║
║   └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └────┘║
║                                                                  ║
║   ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌────┐║
║   │sin⁻¹ │ │cos⁻¹ │ │tan⁻¹ │ │  4   │ │  5   │ │  6   │ │  − │║
║   └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └────┘║
║                                                                  ║
║   ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌────┐║
║   │  x!  │ │ abs  │ │  π   │ │  1   │ │  2   │ │  3   │ │  + │║
║   └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └────┘║
║                                                                  ║
║   ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐       ║
║   │ Ans  │ │  e   │ │ exp  │ │  0   │ │  .   │ │  =   │       ║
║   └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘       ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

MENU OPTIONS:
═══════════════

File Menu:
  • Clear History - Clear calculation history
  • Exit - Close the calculator

Mode Menu:
  • Degree - Set angle mode to degrees
  • Radian - Set angle mode to radians
  • Grad - Set angle mode to gradians

Tools Menu:
  • Equation Solver - Solve linear, quadratic, cubic equations
    ┌─────────────────────────────────────┐
    │ • Linear (ax+b=0)                   │
    │ • Quadratic (ax²+bx+c=0)           │
    │ • Cubic (ax³+bx²+cx+d=0)           │
    └─────────────────────────────────────┘
  
  • Function Grapher - Plot mathematical functions
    ┌─────────────────────────────────────┐
    │  Function: sin(x)                   │
    │  x min: -10                         │
    │  x max: 10                          │
    │  [Plot]                             │
    │  ┌───────────────────────────┐     │
    │  │     📈 Graph Display      │     │
    │  └───────────────────────────┘     │
    └─────────────────────────────────────┘
  
  • Statistics - Calculate statistical measures
    ┌─────────────────────────────────────┐
    │  Enter data (one per line):         │
    │  1                                  │
    │  2                                  │
    │  3                                  │
    │  [Calculate]                        │
    │  Results: Mean, Std Dev, Min, Max   │
    └─────────────────────────────────────┘
  
  • Base Converter - Convert between number bases
    ┌─────────────────────────────────────┐
    │  Number: 255                        │
    │  From Base: 10                      │
    │  To Base: 16                        │
    │  [Convert]                          │
    │  Result: FF                         │
    └─────────────────────────────────────┘

Help Menu:
  • About - Information about the calculator
  • Help - Detailed usage instructions

FEATURES HIGHLIGHT:
═══════════════════

✓ Cross-platform (Windows & Linux)
✓ Scientific calculations
✓ Trigonometric functions (with angle modes)
✓ Equation solving (linear, quadratic, cubic)
✓ System of equations solver
✓ Function graphing with matplotlib
✓ Statistics calculator
✓ Base conversion (binary, octal, decimal, hex)
✓ Calculation history
✓ Memory (Ans) function
✓ Intuitive button interface
✓ Keyboard input support
"""
    
    print(gui_layout)


def print_cli_layout():
    """Print ASCII art representation of the CLI calculator."""
    
    cli_layout = """
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║                 CASIO FX-991 CN X CALCULATOR                     ║
║                        CLI VERSION                               ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║  Angle Mode: DEG                                                 ║
║  Last Answer: 0                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  MAIN MENU:                                                      ║
║  1. Basic Calculator                                             ║
║  2. Equation Solver                                              ║
║  3. Statistics                                                   ║
║  4. Base Converter                                               ║
║  5. Calculus (Derivative/Integral)                               ║
║  6. Settings                                                     ║
║  7. Help                                                         ║
║  0. Exit                                                         ║
║                                                                  ║
║  Select option: _                                                ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

BASIC CALCULATOR MODE:
═══════════════════════
  Expression: sin(45)
  Result: 0.7071067812
  
  Expression: sqrt(16)
  Result: 4
  
  Expression: 2**3 + 5
  Result: 13

EQUATION SOLVER:
════════════════
  1. Linear Equation (ax + b = 0)
  2. Quadratic Equation (ax² + bx + c = 0)
  3. Cubic Equation (ax³ + bx² + cx + d = 0)
  4. System of 2 Linear Equations
  5. System of 3 Linear Equations
  
  Example - Quadratic:
    Enter a: 1
    Enter b: -5
    Enter c: 6
    
    Solutions:
    x₁ = 3.0
    x₂ = 2.0

STATISTICS MODE:
════════════════
  Enter data: 1 2 3 4 5
  
  Statistical Results:
  ═══════════════════════
  Count (n):              5
  Sum (Σx):               15
  Mean (x̄):               3
  Population Std Dev (σ): 1.4142
  Sample Std Dev (s):     1.5811
  Minimum:                1
  Maximum:                5

CALCULUS MODE:
══════════════
  Numerical Derivative: f'(x)
    Function f(x): x**2
    Evaluate at x: 2
    f'(2) = 4.0000
  
  Numerical Integral: ∫f(x)dx
    Function f(x): x**2
    Lower bound a: 0
    Upper bound b: 2
    ∫[0, 2] f(x)dx = 2.6667
"""
    
    print(cli_layout)


if __name__ == "__main__":
    print("\n" + "="*70)
    print("CASIO FX-991 CN X CALCULATOR - INTERFACE PREVIEW")
    print("="*70 + "\n")
    
    print("GUI VERSION:")
    print("="*70)
    print_gui_layout()
    
    print("\n" + "="*70)
    print("\nCLI VERSION:")
    print("="*70)
    print_cli_layout()
    
    print("\n" + "="*70)
    print("To run:")
    print("  GUI: python calculator_gui.py")
    print("  CLI: python calculator_cli.py")
    print("="*70 + "\n")
