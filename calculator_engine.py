"""
Core calculator engine for scientific calculations.
Mimics Casio FX-991 CN X functionality.
"""

import math
import cmath
import re
from typing import Union, List, Tuple, Optional


class CalculatorEngine:
    """Core calculation engine with scientific functions."""
    
    def __init__(self):
        self.memory = 0
        self.ans = 0
        self.angle_mode = 'deg'  # 'deg', 'rad', or 'grad'
        self.variables = {}
        
    def set_angle_mode(self, mode: str):
        """Set angle mode: deg, rad, or grad."""
        if mode in ['deg', 'rad', 'grad']:
            self.angle_mode = mode
        else:
            raise ValueError("Mode must be 'deg', 'rad', or 'grad'")
    
    def to_radians(self, angle: float) -> float:
        """Convert angle to radians based on current mode."""
        if self.angle_mode == 'deg':
            return math.radians(angle)
        elif self.angle_mode == 'grad':
            return angle * math.pi / 200
        return angle
    
    def from_radians(self, angle: float) -> float:
        """Convert angle from radians to current mode."""
        if self.angle_mode == 'deg':
            return math.degrees(angle)
        elif self.angle_mode == 'grad':
            return angle * 200 / math.pi
        return angle
    
    def evaluate(self, expression: str) -> Union[float, complex]:
        """
        Evaluate a mathematical expression.
        Supports basic operations, scientific functions, and constants.
        """
        # Replace common mathematical notation
        expr = expression.replace('^', '**')
        expr = expr.replace('π', str(math.pi))
        expr = expr.replace('Ans', str(self.ans))
        
        # Replace 'e' constant carefully (avoid replacing 'e' in function names like 'exp')
        import re
        expr = re.sub(r'\be\b', str(math.e), expr)
        
        # Create safe evaluation environment
        safe_dict = {
            # Math functions
            'sin': lambda x: math.sin(self.to_radians(x)),
            'cos': lambda x: math.cos(self.to_radians(x)),
            'tan': lambda x: math.tan(self.to_radians(x)),
            'asin': lambda x: self.from_radians(math.asin(x)),
            'acos': lambda x: self.from_radians(math.acos(x)),
            'atan': lambda x: self.from_radians(math.atan(x)),
            'sinh': math.sinh,
            'cosh': math.cosh,
            'tanh': math.tanh,
            'asinh': math.asinh,
            'acosh': math.acosh,
            'atanh': math.atanh,
            'sqrt': math.sqrt,
            'cbrt': lambda x: x ** (1/3) if x >= 0 else -((-x) ** (1/3)),
            'exp': math.exp,
            'ln': math.log,
            'log': math.log10,
            'log2': math.log2,
            'abs': abs,
            'floor': math.floor,
            'ceil': math.ceil,
            'round': round,
            'factorial': math.factorial,
            'gcd': math.gcd,
            'lcm': lambda a, b: abs(a * b) // math.gcd(a, b) if a and b else 0,
            # Constants
            'pi': math.pi,
            'e': math.e,
            'phi': (1 + math.sqrt(5)) / 2,  # Golden ratio
            # Other functions
            'deg': math.degrees,
            'rad': math.radians,
            'pow': pow,
            'mod': lambda a, b: a % b,
        }
        
        try:
            result = eval(expr, {"__builtins__": {}}, safe_dict)
            self.ans = result
            return result
        except Exception as e:
            raise ValueError(f"Error evaluating expression: {str(e)}")
    
    def solve_linear(self, a: float, b: float) -> float:
        """
        Solve linear equation: ax + b = 0
        Returns x.
        """
        if a == 0:
            raise ValueError("Not a linear equation (a cannot be 0)")
        return -b / a
    
    def solve_quadratic(self, a: float, b: float, c: float) -> Tuple[complex, complex]:
        """
        Solve quadratic equation: ax² + bx + c = 0
        Returns (x1, x2) as tuple of complex numbers.
        """
        if a == 0:
            raise ValueError("Not a quadratic equation (a cannot be 0)")
        
        discriminant = b**2 - 4*a*c
        
        if discriminant >= 0:
            sqrt_disc = math.sqrt(discriminant)
            x1 = (-b + sqrt_disc) / (2*a)
            x2 = (-b - sqrt_disc) / (2*a)
        else:
            sqrt_disc = cmath.sqrt(discriminant)
            x1 = (-b + sqrt_disc) / (2*a)
            x2 = (-b - sqrt_disc) / (2*a)
        
        return (x1, x2)
    
    def solve_cubic(self, a: float, b: float, c: float, d: float) -> Tuple[complex, complex, complex]:
        """
        Solve cubic equation: ax³ + bx² + cx + d = 0
        Returns (x1, x2, x3) as tuple of complex numbers.
        """
        if a == 0:
            raise ValueError("Not a cubic equation (a cannot be 0)")
        
        # Normalize coefficients
        b, c, d = b/a, c/a, d/a
        
        # Calculate discriminants
        Q = (3*c - b**2) / 9
        R = (9*b*c - 27*d - 2*b**3) / 54
        
        disc = Q**3 + R**2
        
        if disc >= 0:
            # One real root and two complex conjugate roots
            S = (R + cmath.sqrt(disc + 0j)) ** (1/3)
            T = (R - cmath.sqrt(disc + 0j)) ** (1/3)
            
            x1 = S + T - b/3
            x2 = -(S + T)/2 - b/3 + 1j * cmath.sqrt(3) * (S - T) / 2
            x3 = -(S + T)/2 - b/3 - 1j * cmath.sqrt(3) * (S - T) / 2
        else:
            # Three real roots
            theta = cmath.acos(R / cmath.sqrt(-Q**3 + 0j))
            x1 = 2 * cmath.sqrt(-Q + 0j) * cmath.cos(theta/3) - b/3
            x2 = 2 * cmath.sqrt(-Q + 0j) * cmath.cos((theta + 2*cmath.pi)/3) - b/3
            x3 = 2 * cmath.sqrt(-Q + 0j) * cmath.cos((theta + 4*cmath.pi)/3) - b/3
        
        return (x1, x2, x3)
    
    def solve_system_2x2(self, a1: float, b1: float, c1: float, 
                         a2: float, b2: float, c2: float) -> Tuple[float, float]:
        """
        Solve system of 2 linear equations:
        a1*x + b1*y = c1
        a2*x + b2*y = c2
        Returns (x, y).
        """
        det = a1*b2 - a2*b1
        if det == 0:
            raise ValueError("System has no unique solution (determinant is 0)")
        
        x = (c1*b2 - c2*b1) / det
        y = (a1*c2 - a2*c1) / det
        
        return (x, y)
    
    def solve_system_3x3(self, a1: float, b1: float, c1: float, d1: float,
                         a2: float, b2: float, c2: float, d2: float,
                         a3: float, b3: float, c3: float, d3: float) -> Tuple[float, float, float]:
        """
        Solve system of 3 linear equations:
        a1*x + b1*y + c1*z = d1
        a2*x + b2*y + c2*z = d2
        a3*x + b3*y + c3*z = d3
        Returns (x, y, z).
        """
        # Calculate determinant
        det = (a1*(b2*c3 - b3*c2) - b1*(a2*c3 - a3*c2) + c1*(a2*b3 - a3*b2))
        
        if det == 0:
            raise ValueError("System has no unique solution (determinant is 0)")
        
        # Cramer's rule
        det_x = (d1*(b2*c3 - b3*c2) - b1*(d2*c3 - d3*c2) + c1*(d2*b3 - d3*b2))
        det_y = (a1*(d2*c3 - d3*c2) - d1*(a2*c3 - a3*c2) + c1*(a2*d3 - a3*d2))
        det_z = (a1*(b2*d3 - b3*d2) - b1*(a2*d3 - a3*d2) + d1*(a2*b3 - a3*b2))
        
        x = det_x / det
        y = det_y / det
        z = det_z / det
        
        return (x, y, z)
    
    def statistics(self, data: List[float]) -> dict:
        """
        Calculate statistical measures for a dataset.
        Returns dict with mean, sum, sum of squares, population std dev, 
        sample std dev, min, max, and count.
        """
        if not data:
            raise ValueError("Data list cannot be empty")
        
        n = len(data)
        sum_x = sum(data)
        mean = sum_x / n
        sum_x2 = sum(x**2 for x in data)
        
        # Population standard deviation
        pop_variance = sum_x2/n - mean**2
        pop_std = math.sqrt(pop_variance) if pop_variance >= 0 else 0
        
        # Sample standard deviation
        if n > 1:
            sample_variance = (sum_x2 - sum_x**2/n) / (n - 1)
            sample_std = math.sqrt(sample_variance) if sample_variance >= 0 else 0
        else:
            sample_std = 0
        
        return {
            'n': n,
            'sum': sum_x,
            'mean': mean,
            'sum_squares': sum_x2,
            'pop_std': pop_std,
            'sample_std': sample_std,
            'min': min(data),
            'max': max(data)
        }
    
    def convert_base(self, number: str, from_base: int, to_base: int) -> str:
        """
        Convert number from one base to another.
        Supports bases 2 (binary), 8 (octal), 10 (decimal), 16 (hexadecimal).
        """
        if from_base not in [2, 8, 10, 16] or to_base not in [2, 8, 10, 16]:
            raise ValueError("Supported bases: 2, 8, 10, 16")
        
        # Convert to decimal first
        decimal = int(number, from_base)
        
        # Convert to target base
        if to_base == 2:
            return bin(decimal)[2:]
        elif to_base == 8:
            return oct(decimal)[2:]
        elif to_base == 10:
            return str(decimal)
        elif to_base == 16:
            return hex(decimal)[2:].upper()
    
    def derivative_numerical(self, func_str: str, x: float, h: float = 1e-5) -> float:
        """
        Calculate numerical derivative using central difference method.
        """
        def f(val):
            return self.evaluate(func_str.replace('x', str(val)))
        
        return (f(x + h) - f(x - h)) / (2 * h)
    
    def integral_numerical(self, func_str: str, a: float, b: float, n: int = 1000) -> float:
        """
        Calculate numerical integral using Simpson's rule.
        """
        if n % 2 == 1:
            n += 1
        
        h = (b - a) / n
        
        def f(val):
            return self.evaluate(func_str.replace('x', str(val)))
        
        sum_odd = sum(f(a + i*h) for i in range(1, n, 2))
        sum_even = sum(f(a + i*h) for i in range(2, n, 2))
        
        result = (h / 3) * (f(a) + f(b) + 4*sum_odd + 2*sum_even)
        return result
