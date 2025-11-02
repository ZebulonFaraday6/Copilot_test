# Quick Start Guide - Casio FX-991 CN X Calculator

## Installation

### Windows

1. **Install Python** (if not already installed):
   - Download Python from https://www.python.org/downloads/
   - During installation, check "Add Python to PATH"

2. **Install dependencies**:
   ```cmd
   pip install -r requirements.txt
   ```

3. **Run the calculator**:
   - GUI version: `python calculator_gui.py`
   - CLI version: `python calculator_cli.py`

### Linux

1. **Install Python and tkinter**:
   ```bash
   # Ubuntu/Debian
   sudo apt-get update
   sudo apt-get install python3 python3-pip python3-tk
   
   # Fedora
   sudo dnf install python3 python3-pip python3-tkinter
   
   # Arch
   sudo pacman -S python python-pip tk
   ```

2. **Install dependencies**:
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Run the calculator**:
   - GUI version: `python3 calculator_gui.py`
   - CLI version: `python3 calculator_cli.py`

## Quick Examples

### Basic Calculations
```
sin(45)           # Sine of 45 degrees
sqrt(16)          # Square root of 16
2**3              # 2 to the power of 3
log(100)          # Log base 10 of 100
factorial(5)      # Factorial of 5
pi * 2            # Pi times 2
```

### Equation Solving

**GUI**: Tools → Equation Solver → Select equation type
**CLI**: Main Menu → 2. Equation Solver

Example - Solve x² - 5x + 6 = 0:
- a = 1
- b = -5
- c = 6
- Result: x₁ = 3, x₂ = 2

### Function Graphing (GUI only)

1. Tools → Function Grapher
2. Enter function: `sin(x)`
3. Set range: x min = -10, x max = 10
4. Click "Plot"

### Statistics

**Example dataset**: 1, 2, 3, 4, 5

**GUI**: Tools → Statistics → Enter data (one per line)
**CLI**: Main Menu → 3. Statistics → Enter data

Results: Mean = 3, Std Dev = 1.58, Min = 1, Max = 5

## Keyboard Shortcuts (GUI)

- Type expressions directly into the display
- `Enter` or `=` button to calculate
- Standard operators: `+`, `-`, `*`, `/`, `**` (power)
- Functions: `sin()`, `cos()`, `tan()`, `sqrt()`, `log()`, `ln()`

## Common Issues

### "No module named 'tkinter'"
**Solution**: Install tkinter package for your system (see Linux installation above)

### "No module named 'numpy'" or "'matplotlib'"
**Solution**: Run `pip install -r requirements.txt`

## Features Summary

✓ Scientific calculator with 30+ functions
✓ Equation solver (linear, quadratic, cubic)
✓ System of equations solver (2x2, 3x3)
✓ Function graphing (GUI)
✓ Statistics calculator
✓ Base converter (binary, octal, decimal, hex)
✓ Numerical calculus (derivative, integral)
✓ Multiple angle modes (deg, rad, grad)
✓ Calculation history (GUI)
✓ Cross-platform (Windows & Linux)

## Support

For detailed documentation, see README.md
For interface preview, run: `python3 interface_preview.py`
To run tests: `python3 test_calculator.py`

## Tips

1. **Change angle mode** before using trig functions
2. **Use parentheses** for clarity: `sin(30) + cos(60)`
3. **Access advanced features** via the Tools menu (GUI) or Main menu (CLI)
4. **View history** in the GUI to see previous calculations
5. **Use Ans** to reference the last calculation result
