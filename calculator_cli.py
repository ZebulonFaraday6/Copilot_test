"""
CLI Calculator mimicking Casio FX-991 CN X.
Command-line interface for scientific calculations.
"""

import sys
import os
from calculator_engine import CalculatorEngine


class CasioCalculatorCLI:
    """Command-line calculator interface."""
    
    def __init__(self):
        self.engine = CalculatorEngine()
        self.running = True
        
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        """Print calculator banner."""
        print("=" * 60)
        print("  CASIO FX-991 CN X CALCULATOR - CLI VERSION")
        print("=" * 60)
        print(f"Angle Mode: {self.engine.angle_mode.upper()}")
        print(f"Last Answer: {self.engine.ans}")
        print("=" * 60)
        print()
    
    def print_menu(self):
        """Print main menu."""
        print("MAIN MENU:")
        print("1. Basic Calculator")
        print("2. Equation Solver")
        print("3. Statistics")
        print("4. Base Converter")
        print("5. Calculus (Derivative/Integral)")
        print("6. Settings")
        print("7. Help")
        print("0. Exit")
        print()
    
    def basic_calculator(self):
        """Basic calculator mode."""
        self.clear_screen()
        print("=" * 60)
        print("  BASIC CALCULATOR")
        print("=" * 60)
        print("Enter mathematical expressions (or 'back' to return)")
        print("Examples: sin(45), sqrt(16), 2**3, log(100)")
        print("=" * 60)
        print()
        
        while True:
            try:
                expr = input("Expression: ").strip()
                
                if expr.lower() in ['back', 'exit', 'quit']:
                    break
                
                if not expr:
                    continue
                
                result = self.engine.evaluate(expr)
                
                if isinstance(result, complex):
                    if result.imag == 0:
                        print(f"Result: {result.real:.10g}")
                    else:
                        print(f"Result: {result.real:.10g} + {result.imag:.10g}i")
                else:
                    print(f"Result: {result:.10g}")
                
                print()
                
            except KeyboardInterrupt:
                print("\n")
                break
            except Exception as e:
                print(f"Error: {str(e)}")
                print()
    
    def equation_solver_menu(self):
        """Equation solver menu."""
        while True:
            self.clear_screen()
            print("=" * 60)
            print("  EQUATION SOLVER")
            print("=" * 60)
            print("1. Linear Equation (ax + b = 0)")
            print("2. Quadratic Equation (ax² + bx + c = 0)")
            print("3. Cubic Equation (ax³ + bx² + cx + d = 0)")
            print("4. System of 2 Linear Equations")
            print("5. System of 3 Linear Equations")
            print("0. Back to Main Menu")
            print("=" * 60)
            
            choice = input("\nSelect option: ").strip()
            
            if choice == '0':
                break
            elif choice == '1':
                self.solve_linear()
            elif choice == '2':
                self.solve_quadratic()
            elif choice == '3':
                self.solve_cubic()
            elif choice == '4':
                self.solve_system_2x2()
            elif choice == '5':
                self.solve_system_3x3()
            else:
                print("Invalid option!")
                input("Press Enter to continue...")
    
    def solve_linear(self):
        """Solve linear equation."""
        print("\nLinear Equation: ax + b = 0")
        try:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            
            x = self.engine.solve_linear(a, b)
            print(f"\nSolution: x = {x:.10g}")
            
        except Exception as e:
            print(f"Error: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def solve_quadratic(self):
        """Solve quadratic equation."""
        print("\nQuadratic Equation: ax² + bx + c = 0")
        try:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))
            
            x1, x2 = self.engine.solve_quadratic(a, b, c)
            
            print("\nSolutions:")
            if isinstance(x1, complex) and x1.imag != 0:
                print(f"x₁ = {x1.real:.10g} + {x1.imag:.10g}i")
                print(f"x₂ = {x2.real:.10g} + {x2.imag:.10g}i")
            else:
                x1_real = x1.real if isinstance(x1, complex) else x1
                x2_real = x2.real if isinstance(x2, complex) else x2
                print(f"x₁ = {x1_real:.10g}")
                print(f"x₂ = {x2_real:.10g}")
            
        except Exception as e:
            print(f"Error: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def solve_cubic(self):
        """Solve cubic equation."""
        print("\nCubic Equation: ax³ + bx² + cx + d = 0")
        try:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))
            d = float(input("Enter d: "))
            
            x1, x2, x3 = self.engine.solve_cubic(a, b, c, d)
            
            print("\nSolutions:")
            for i, x in enumerate([x1, x2, x3], 1):
                if isinstance(x, complex) and abs(x.imag) > 1e-10:
                    print(f"x{i} = {x.real:.10g} + {x.imag:.10g}i")
                else:
                    val = x.real if isinstance(x, complex) else x
                    print(f"x{i} = {val:.10g}")
            
        except Exception as e:
            print(f"Error: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def solve_system_2x2(self):
        """Solve system of 2 linear equations."""
        print("\nSystem of 2 Linear Equations:")
        print("a₁x + b₁y = c₁")
        print("a₂x + b₂y = c₂")
        try:
            print("\nFirst equation:")
            a1 = float(input("Enter a₁: "))
            b1 = float(input("Enter b₁: "))
            c1 = float(input("Enter c₁: "))
            
            print("\nSecond equation:")
            a2 = float(input("Enter a₂: "))
            b2 = float(input("Enter b₂: "))
            c2 = float(input("Enter c₂: "))
            
            x, y = self.engine.solve_system_2x2(a1, b1, c1, a2, b2, c2)
            
            print(f"\nSolution:")
            print(f"x = {x:.10g}")
            print(f"y = {y:.10g}")
            
        except Exception as e:
            print(f"Error: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def solve_system_3x3(self):
        """Solve system of 3 linear equations."""
        print("\nSystem of 3 Linear Equations:")
        print("a₁x + b₁y + c₁z = d₁")
        print("a₂x + b₂y + c₂z = d₂")
        print("a₃x + b₃y + c₃z = d₃")
        try:
            print("\nFirst equation:")
            a1 = float(input("Enter a₁: "))
            b1 = float(input("Enter b₁: "))
            c1 = float(input("Enter c₁: "))
            d1 = float(input("Enter d₁: "))
            
            print("\nSecond equation:")
            a2 = float(input("Enter a₂: "))
            b2 = float(input("Enter b₂: "))
            c2 = float(input("Enter c₂: "))
            d2 = float(input("Enter d₂: "))
            
            print("\nThird equation:")
            a3 = float(input("Enter a₃: "))
            b3 = float(input("Enter b₃: "))
            c3 = float(input("Enter c₃: "))
            d3 = float(input("Enter d₃: "))
            
            x, y, z = self.engine.solve_system_3x3(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3)
            
            print(f"\nSolution:")
            print(f"x = {x:.10g}")
            print(f"y = {y:.10g}")
            print(f"z = {z:.10g}")
            
        except Exception as e:
            print(f"Error: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def statistics_calculator(self):
        """Statistics calculator."""
        self.clear_screen()
        print("=" * 60)
        print("  STATISTICS CALCULATOR")
        print("=" * 60)
        print("Enter data values separated by spaces or commas")
        print("Example: 1 2 3 4 5 or 1,2,3,4,5")
        print("=" * 60)
        
        try:
            data_str = input("\nEnter data: ").strip()
            
            if not data_str:
                print("No data entered!")
                input("Press Enter to continue...")
                return
            
            # Parse data
            data_str = data_str.replace(',', ' ')
            data = [float(x) for x in data_str.split() if x]
            
            stats = self.engine.statistics(data)
            
            print("\n" + "=" * 60)
            print("STATISTICAL RESULTS:")
            print("=" * 60)
            print(f"Count (n):              {stats['n']}")
            print(f"Sum (Σx):               {stats['sum']:.10g}")
            print(f"Mean (x̄):               {stats['mean']:.10g}")
            print(f"Sum of squares (Σx²):   {stats['sum_squares']:.10g}")
            print(f"Population Std Dev (σ): {stats['pop_std']:.10g}")
            print(f"Sample Std Dev (s):     {stats['sample_std']:.10g}")
            print(f"Minimum:                {stats['min']:.10g}")
            print(f"Maximum:                {stats['max']:.10g}")
            print("=" * 60)
            
        except Exception as e:
            print(f"Error: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def base_converter(self):
        """Base conversion calculator."""
        self.clear_screen()
        print("=" * 60)
        print("  BASE CONVERTER")
        print("=" * 60)
        print("Supported bases: 2 (binary), 8 (octal), 10 (decimal), 16 (hex)")
        print("=" * 60)
        
        try:
            number = input("\nEnter number: ").strip()
            from_base = int(input("From base (2/8/10/16): "))
            to_base = int(input("To base (2/8/10/16): "))
            
            result = self.engine.convert_base(number, from_base, to_base)
            
            print(f"\nResult: {result}")
            
        except Exception as e:
            print(f"Error: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def calculus_menu(self):
        """Calculus menu."""
        self.clear_screen()
        print("=" * 60)
        print("  CALCULUS")
        print("=" * 60)
        print("1. Numerical Derivative")
        print("2. Numerical Integral")
        print("0. Back")
        print("=" * 60)
        
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            self.calculate_derivative()
        elif choice == '2':
            self.calculate_integral()
    
    def calculate_derivative(self):
        """Calculate numerical derivative."""
        print("\nNumerical Derivative: f'(x)")
        print("Enter function in terms of x")
        print("Example: x**2 + 3*x + 2")
        
        try:
            func = input("\nFunction f(x): ").strip()
            x = float(input("Evaluate at x: "))
            
            result = self.engine.derivative_numerical(func, x)
            print(f"\nf'({x}) = {result:.10g}")
            
        except Exception as e:
            print(f"Error: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def calculate_integral(self):
        """Calculate numerical integral."""
        print("\nNumerical Integral: ∫f(x)dx")
        print("Enter function in terms of x")
        print("Example: x**2")
        
        try:
            func = input("\nFunction f(x): ").strip()
            a = float(input("Lower bound a: "))
            b = float(input("Upper bound b: "))
            
            result = self.engine.integral_numerical(func, a, b)
            print(f"\n∫[{a}, {b}] f(x)dx = {result:.10g}")
            
        except Exception as e:
            print(f"Error: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def settings_menu(self):
        """Settings menu."""
        self.clear_screen()
        print("=" * 60)
        print("  SETTINGS")
        print("=" * 60)
        print(f"Current Angle Mode: {self.engine.angle_mode.upper()}")
        print("=" * 60)
        print("\n1. Set to Degree (deg)")
        print("2. Set to Radian (rad)")
        print("3. Set to Grad (grad)")
        print("0. Back")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            self.engine.set_angle_mode('deg')
            print("Angle mode set to DEGREE")
        elif choice == '2':
            self.engine.set_angle_mode('rad')
            print("Angle mode set to RADIAN")
        elif choice == '3':
            self.engine.set_angle_mode('grad')
            print("Angle mode set to GRAD")
        
        if choice in ['1', '2', '3']:
            input("\nPress Enter to continue...")
    
    def show_help(self):
        """Show help information."""
        self.clear_screen()
        print("=" * 60)
        print("  HELP - CASIO FX-991 CN X CALCULATOR")
        print("=" * 60)
        print("""
BASIC CALCULATOR:
  - Enter mathematical expressions directly
  - Supported functions: sin, cos, tan, asin, acos, atan,
    sinh, cosh, tanh, sqrt, exp, ln, log, abs, factorial
  - Constants: pi, e
  - Use Ans for last answer
  - Examples: sin(45), sqrt(16), 2**3, factorial(5)

EQUATION SOLVER:
  - Solve linear, quadratic, cubic equations
  - Solve systems of linear equations (2x2, 3x3)

STATISTICS:
  - Calculate mean, standard deviation, min, max
  - Enter data as space or comma-separated values

BASE CONVERTER:
  - Convert between binary (2), octal (8), decimal (10), hex (16)

CALCULUS:
  - Numerical derivative and integral calculations
  - Enter functions in terms of x

SETTINGS:
  - Change angle mode (degree/radian/grad)
  - Affects trigonometric functions

ANGLE MODES:
  - deg: Degrees (default) - sin(90) = 1
  - rad: Radians - sin(pi/2) = 1
  - grad: Gradians - sin(100) = 1
""")
        print("=" * 60)
        input("\nPress Enter to continue...")
    
    def run(self):
        """Main run loop."""
        while self.running:
            self.clear_screen()
            self.print_banner()
            self.print_menu()
            
            try:
                choice = input("Select option: ").strip()
                
                if choice == '0':
                    print("\nThank you for using Casio FX-991 CN X Calculator!")
                    self.running = False
                elif choice == '1':
                    self.basic_calculator()
                elif choice == '2':
                    self.equation_solver_menu()
                elif choice == '3':
                    self.statistics_calculator()
                elif choice == '4':
                    self.base_converter()
                elif choice == '5':
                    self.calculus_menu()
                elif choice == '6':
                    self.settings_menu()
                elif choice == '7':
                    self.show_help()
                else:
                    print("Invalid option!")
                    input("Press Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\n\nExiting...")
                self.running = False
            except Exception as e:
                print(f"\nError: {str(e)}")
                input("Press Enter to continue...")


def main():
    """Main function to run the CLI calculator."""
    calculator = CasioCalculatorCLI()
    calculator.run()


if __name__ == "__main__":
    main()
