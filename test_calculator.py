#!/usr/bin/env python3
"""
Test suite for Casio FX-991 CN X Calculator
Tests all major functionality of the calculator.
"""

from calculator_engine import CalculatorEngine
import sys


def test_basic_operations():
    """Test basic arithmetic operations."""
    print("Testing Basic Operations...")
    engine = CalculatorEngine()
    
    tests = [
        ("2 + 3", 5),
        ("10 - 4", 6),
        ("6 * 7", 42),
        ("20 / 4", 5),
        ("2**8", 256),
        ("sqrt(64)", 8),
    ]
    
    for expr, expected in tests:
        result = engine.evaluate(expr)
        assert abs(result - expected) < 1e-10, f"Failed: {expr} = {result}, expected {expected}"
        print(f"  ✓ {expr} = {result}")
    
    print("✓ Basic operations passed!\n")


def test_scientific_functions():
    """Test scientific functions."""
    print("Testing Scientific Functions...")
    engine = CalculatorEngine()
    
    # Test trigonometric functions (in degree mode)
    engine.set_angle_mode('deg')
    
    tests = [
        ("sin(30)", 0.5),
        ("cos(60)", 0.5),
        ("tan(45)", 1.0),
        ("log(100)", 2.0),
        ("ln(e)", 1.0),
        ("exp(0)", 1.0),
        ("abs(-5)", 5),
        ("factorial(5)", 120),
    ]
    
    for expr, expected in tests:
        result = engine.evaluate(expr)
        assert abs(result - expected) < 1e-9, f"Failed: {expr} = {result}, expected {expected}"
        print(f"  ✓ {expr} = {result}")
    
    print("✓ Scientific functions passed!\n")


def test_angle_modes():
    """Test different angle modes."""
    print("Testing Angle Modes...")
    engine = CalculatorEngine()
    
    # Degree mode
    engine.set_angle_mode('deg')
    result = engine.evaluate("sin(90)")
    assert abs(result - 1.0) < 1e-10, f"Degree mode failed: sin(90) = {result}"
    print(f"  ✓ Degree mode: sin(90) = {result}")
    
    # Radian mode
    engine.set_angle_mode('rad')
    result = engine.evaluate("sin(pi/2)")
    assert abs(result - 1.0) < 1e-10, f"Radian mode failed: sin(pi/2) = {result}"
    print(f"  ✓ Radian mode: sin(π/2) = {result}")
    
    print("✓ Angle modes passed!\n")


def test_equation_solvers():
    """Test equation solving functionality."""
    print("Testing Equation Solvers...")
    engine = CalculatorEngine()
    
    # Linear equation: 2x + 4 = 0
    x = engine.solve_linear(2, 4)
    assert abs(x - (-2)) < 1e-10, f"Linear solver failed: x = {x}"
    print(f"  ✓ Linear (2x+4=0): x = {x}")
    
    # Quadratic equation: x^2 - 5x + 6 = 0
    x1, x2 = engine.solve_quadratic(1, -5, 6)
    assert abs(x1 - 3) < 1e-10 and abs(x2 - 2) < 1e-10, f"Quadratic solver failed"
    print(f"  ✓ Quadratic (x²-5x+6=0): x₁ = {x1}, x₂ = {x2}")
    
    # Cubic equation: x^3 - 6x^2 + 11x - 6 = 0
    x1, x2, x3 = engine.solve_cubic(1, -6, 11, -6)
    # Solutions are 1, 2, 3
    real_parts = sorted([x.real if isinstance(x, complex) else x for x in [x1, x2, x3]])
    assert abs(real_parts[0] - 1) < 1e-9, "Cubic solver failed"
    print(f"  ✓ Cubic (x³-6x²+11x-6=0): solutions found")
    
    # System of 2 equations
    # 2x + 3y = 8
    # 4x - y = 2
    x, y = engine.solve_system_2x2(2, 3, 8, 4, -1, 2)
    assert abs(x - 1) < 1e-10 and abs(y - 2) < 1e-10, f"2x2 system solver failed"
    print(f"  ✓ System 2x2: x = {x}, y = {y}")
    
    print("✓ Equation solvers passed!\n")


def test_statistics():
    """Test statistics functionality."""
    print("Testing Statistics...")
    engine = CalculatorEngine()
    
    data = [1, 2, 3, 4, 5]
    stats = engine.statistics(data)
    
    assert stats['n'] == 5, "Count failed"
    assert abs(stats['mean'] - 3.0) < 1e-10, "Mean calculation failed"
    assert abs(stats['sum'] - 15.0) < 1e-10, "Sum calculation failed"
    assert stats['min'] == 1, "Min calculation failed"
    assert stats['max'] == 5, "Max calculation failed"
    
    print(f"  ✓ Data: {data}")
    print(f"  ✓ Mean: {stats['mean']}")
    print(f"  ✓ Std Dev: {stats['sample_std']:.4f}")
    print(f"  ✓ Min: {stats['min']}, Max: {stats['max']}")
    
    print("✓ Statistics passed!\n")


def test_base_conversion():
    """Test base conversion."""
    print("Testing Base Conversion...")
    engine = CalculatorEngine()
    
    tests = [
        ("255", 10, 16, "FF"),
        ("1010", 2, 10, "10"),
        ("77", 8, 10, "63"),
        ("FF", 16, 2, "11111111"),
    ]
    
    for number, from_base, to_base, expected in tests:
        result = engine.convert_base(number, from_base, to_base)
        assert result == expected, f"Conversion failed: {number} (base {from_base}) to base {to_base}"
        print(f"  ✓ {number} (base {from_base}) → {result} (base {to_base})")
    
    print("✓ Base conversion passed!\n")


def test_calculus():
    """Test calculus functions."""
    print("Testing Calculus Functions...")
    engine = CalculatorEngine()
    
    # Test derivative of x^2 at x=2 (should be 4)
    result = engine.derivative_numerical("x**2", 2)
    assert abs(result - 4) < 1e-4, f"Derivative failed: d/dx(x²) at x=2 = {result}"
    print(f"  ✓ Derivative: d/dx(x²) at x=2 = {result:.4f}")
    
    # Test integral of x^2 from 0 to 2 (should be 8/3 ≈ 2.667)
    result = engine.integral_numerical("x**2", 0, 2)
    expected = 8/3
    assert abs(result - expected) < 1e-3, f"Integral failed: ∫x² dx from 0 to 2 = {result}"
    print(f"  ✓ Integral: ∫₀² x² dx = {result:.4f}")
    
    print("✓ Calculus functions passed!\n")


def test_complex_expressions():
    """Test complex mathematical expressions."""
    print("Testing Complex Expressions...")
    engine = CalculatorEngine()
    
    tests = [
        "sin(30)**2 + cos(30)**2",  # Should be 1
        "log(10**3)",                # Should be 3
        "sqrt(2)**2",                # Should be 2
        "factorial(4) / factorial(2)",  # Should be 12
    ]
    
    for expr in tests:
        result = engine.evaluate(expr)
        print(f"  ✓ {expr} = {result}")
    
    print("✓ Complex expressions passed!\n")


def main():
    """Run all tests."""
    print("=" * 60)
    print("  CASIO FX-991 CN X CALCULATOR - TEST SUITE")
    print("=" * 60)
    print()
    
    try:
        test_basic_operations()
        test_scientific_functions()
        test_angle_modes()
        test_equation_solvers()
        test_statistics()
        test_base_conversion()
        test_calculus()
        test_complex_expressions()
        
        print("=" * 60)
        print("  ✓ ALL TESTS PASSED!")
        print("=" * 60)
        return 0
        
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ UNEXPECTED ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
