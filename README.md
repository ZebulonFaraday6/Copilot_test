# Casio FX-991 CN X Calculator

A cross-platform scientific calculator that mimics the functionality and interface of the Casio FX-991 CN X calculator. This implementation provides both a GUI version and a CLI version, supporting Windows and Linux systems.

![Calculator Type](https://img.shields.io/badge/Type-Scientific%20Calculator-blue)
![Python](https://img.shields.io/badge/Python-3.7+-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)

## Features

### Core Calculation Features
- **Basic Operations**: Addition, subtraction, multiplication, division, powers, roots
- **Scientific Functions**: 
  - Trigonometric functions (sin, cos, tan) with degree/radian/grad modes
  - Inverse trigonometric functions (arcsin, arccos, arctan)
  - Hyperbolic functions (sinh, cosh, tanh) and their inverses
  - Exponential and logarithmic functions (exp, ln, log, log2)
  - Factorial, absolute value, floor, ceiling, rounding
- **Mathematical Constants**: π (pi), e, φ (golden ratio)

### Advanced Features
- **Equation Solver**:
  - Linear equations (ax + b = 0)
  - Quadratic equations (ax² + bx + c = 0)
  - Cubic equations (ax³ + bx² + cx + d = 0)
  - Systems of 2 linear equations (2x2)
  - Systems of 3 linear equations (3x3)

- **Function Graphing** (GUI only):
  - Plot mathematical functions
  - Customizable x-axis range
  - Interactive matplotlib-based graphs

- **Statistics Calculator**:
  - Mean, sum, count
  - Population and sample standard deviation
  - Minimum and maximum values
  - Sum of squares

- **Base Converter**:
  - Convert between binary (base 2), octal (base 8), decimal (base 10), and hexadecimal (base 16)

- **Calculus** (CLI version):
  - Numerical derivative calculation
  - Numerical integration using Simpson's rule

### Interface Features
- **Multiple Angle Modes**: Degree, Radian, Gradians
- **Calculation History**: View previous calculations (GUI)
- **Memory Functions**: Store and recall last answer (Ans)
- **User-Friendly Interface**: Both GUI and CLI versions designed for ease of use

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. **Clone or download this repository**:
   ```bash
   git clone <repository-url>
   cd Copilot_test
   ```

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   The requirements include:
   - `numpy`: For numerical computations
   - `matplotlib`: For function graphing (GUI version)
   - `tkinter`: Built-in Python GUI library (usually comes with Python)

   **Note for Linux users**: If tkinter is not installed, install it using:
   - Ubuntu/Debian: `sudo apt-get install python3-tk`
   - Fedora: `sudo dnf install python3-tkinter`
   - Arch: `sudo pacman -S tk`

## Usage

### GUI Version

To launch the graphical user interface version:

```bash
python calculator_gui.py
```

or on some systems:

```bash
python3 calculator_gui.py
```

#### GUI Features:
1. **Main Calculator**:
   - Use on-screen buttons or keyboard to enter expressions
   - Press `=` to calculate
   - View calculation history in the upper panel
   - Result displayed in the lower panel

2. **Menu Options**:
   - **File**: Clear history, Exit
   - **Mode**: Change angle mode (Degree/Radian/Grad)
   - **Tools**: Access equation solver, function grapher, statistics, base converter
   - **Help**: View about information and help documentation

3. **Keyboard Shortcuts**:
   - You can type directly into the display field
   - Use standard mathematical notation (*, /, +, -, **)

4. **Function Grapher**:
   - Tools → Function Grapher
   - Enter function in terms of x (e.g., `sin(x)`, `x**2 + 3*x + 2`)
   - Set x range (minimum and maximum values)
   - Click "Plot" to visualize the function

5. **Equation Solver**:
   - Tools → Equation Solver
   - Choose equation type from tabs
   - Enter coefficients
   - Click "Solve" to get solutions

### CLI Version

To launch the command-line interface version:

```bash
python calculator_cli.py
```

or on some systems:

```bash
python3 calculator_cli.py
```

#### CLI Features:
1. **Main Menu**: Navigate using numeric options (0-7)
2. **Basic Calculator**: Enter expressions directly
3. **Equation Solver**: Solve various types of equations
4. **Statistics**: Calculate statistical measures for datasets
5. **Base Converter**: Convert numbers between different bases
6. **Calculus**: Calculate derivatives and integrals numerically
7. **Settings**: Change angle mode
8. **Help**: View detailed help information

## Examples

### Basic Calculations

**GUI/CLI**:
```
sin(45)           → 0.7071067812 (in degree mode)
sqrt(16)          → 4
2**3              → 8
log(100)          → 2
factorial(5)      → 120
abs(-10)          → 10
pi * 2            → 6.283185307
```

### Equation Solving

**Linear Equation**: 2x + 4 = 0
- Input: a=2, b=4
- Output: x = -2

**Quadratic Equation**: x² - 5x + 6 = 0
- Input: a=1, b=-5, c=6
- Output: x₁ = 3, x₂ = 2

**Cubic Equation**: x³ - 6x² + 11x - 6 = 0
- Input: a=1, b=-6, c=11, d=-6
- Output: x₁ = 1, x₂ = 2, x₃ = 3

### Statistics

**Dataset**: 1, 2, 3, 4, 5
- Mean: 3
- Population Std Dev: 1.414213562
- Sample Std Dev: 1.581138830
- Min: 1, Max: 5

### Base Conversion

**Example 1**: Convert 255 from decimal to hexadecimal
- Input: 255 (base 10) → Output: FF (base 16)

**Example 2**: Convert 1010 from binary to decimal
- Input: 1010 (base 2) → Output: 10 (base 10)

### Function Graphing (GUI Only)

**Example**: Plot sin(x) from -10 to 10
1. Open Tools → Function Grapher
2. Enter function: `sin(x)`
3. Set x min: `-10`
4. Set x max: `10`
5. Click "Plot"

## Angle Modes

The calculator supports three angle modes for trigonometric functions:

1. **Degree (deg)** - Default mode
   - Example: `sin(90)` = 1

2. **Radian (rad)**
   - Example: `sin(pi/2)` = 1

3. **Gradian (grad)**
   - Example: `sin(100)` = 1

Change angle mode via:
- **GUI**: Mode menu or mode selector buttons
- **CLI**: Settings menu (option 6)

## Supported Functions

### Trigonometric
- `sin(x)`, `cos(x)`, `tan(x)`: Trigonometric functions
- `asin(x)`, `acos(x)`, `atan(x)`: Inverse trigonometric functions
- `sinh(x)`, `cosh(x)`, `tanh(x)`: Hyperbolic functions
- `asinh(x)`, `acosh(x)`, `atanh(x)`: Inverse hyperbolic functions

### Exponential and Logarithmic
- `exp(x)`: e raised to power x
- `ln(x)`: Natural logarithm (base e)
- `log(x)`: Common logarithm (base 10)
- `log2(x)`: Binary logarithm (base 2)

### Power and Root
- `sqrt(x)`: Square root
- `cbrt(x)`: Cube root
- `x**y` or `pow(x,y)`: x raised to power y

### Other Functions
- `factorial(n)`: Factorial of n
- `abs(x)`: Absolute value
- `floor(x)`: Floor function
- `ceil(x)`: Ceiling function
- `round(x)`: Round to nearest integer
- `gcd(a,b)`: Greatest common divisor
- `lcm(a,b)`: Least common multiple

### Constants
- `pi` or `π`: Pi (≈3.14159...)
- `e`: Euler's number (≈2.71828...)
- `phi`: Golden ratio (≈1.61803...)

## Platform Compatibility

### Windows
- **GUI**: Fully supported with tkinter (built-in)
- **CLI**: Fully supported in Command Prompt or PowerShell
- **Requirements**: Python 3.7+, numpy, matplotlib

### Linux
- **GUI**: Fully supported (requires python3-tk package)
- **CLI**: Fully supported in terminal
- **Requirements**: Python 3.7+, numpy, matplotlib, python3-tk

## Architecture

The calculator is built with a modular architecture:

1. **calculator_engine.py**: Core calculation engine
   - Implements all mathematical operations
   - Equation solvers
   - Statistics calculations
   - Base conversion
   - Calculus functions

2. **calculator_gui.py**: GUI implementation
   - Built with tkinter for cross-platform compatibility
   - matplotlib integration for graphing
   - Menu system for advanced features

3. **calculator_cli.py**: CLI implementation
   - Menu-driven interface
   - Text-based user interaction
   - Full feature parity with GUI (except graphing uses text output)

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'tkinter'"
**Solution**: Install tkinter:
- Linux: `sudo apt-get install python3-tk` (Ubuntu/Debian)
- This usually comes pre-installed on Windows and macOS

### Issue: "ModuleNotFoundError: No module named 'numpy'" or similar
**Solution**: Install dependencies:
```bash
pip install -r requirements.txt
```

### Issue: Graph window not displaying
**Solution**: Make sure matplotlib is properly installed:
```bash
pip install --upgrade matplotlib
```

### Issue: Display issues on high-DPI screens
**Solution**: The GUI should automatically scale, but if issues persist, try adjusting your system's display scaling settings.

## License

This is an educational project created for learning purposes. The Casio FX-991 CN X is a trademark of Casio Computer Co., Ltd. This project is not affiliated with or endorsed by Casio.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## Acknowledgments

- Inspired by the Casio FX-991 CN X scientific calculator
- Built with Python, tkinter, numpy, and matplotlib
- Created as a cross-platform educational tool
