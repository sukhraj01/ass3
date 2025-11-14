"""
Comprehensive Test Suite for Octal Calculator

Tests cover:
- Octal conversion (octal to decimal and back)
- Basic arithmetic operations in octal
- PEMDAS order of operations
- Variable bindings with LET
- User-defined recursive functions
- Conditional expressions
- Edge cases and error handling
"""

import sys
from octal_calculator import OctalCalculator, OctalConverter
from exceptions import *


class TestRunner:
    """Simple test runner to organize and run tests."""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.test_results = []
    
    def test(self, description, test_func):
        """Run a single test."""
        try:
            test_func()
            self.passed += 1
            self.test_results.append(('PASS', description))
            print(f"✓ {description}")
        except AssertionError as e:
            self.failed += 1
            self.test_results.append(('FAIL', description, str(e)))
            print(f"✗ {description}")
            print(f"  Error: {e}")
        except Exception as e:
            self.failed += 1
            self.test_results.append(('ERROR', description, str(e)))
            print(f"✗ {description}")
            print(f"  Unexpected error: {e}")
    
    def summary(self):
        """Print test summary."""
        total = self.passed + self.failed
        print("\n" + "=" * 60)
        print(f"Test Summary: {self.passed}/{total} passed")
        if self.failed > 0:
            print(f"\nFailed tests:")
            for result in self.test_results:
                if result[0] != 'PASS':
                    print(f"  - {result[1]}")
        print("=" * 60)


def test_octal_conversion():
    """Test octal to decimal and decimal to octal conversion."""
    print("\n" + "=" * 60)
    print("Testing Octal Conversion")
    print("=" * 60)
    
    runner = TestRunner()
    converter = OctalConverter()
    
    # Octal to Decimal tests
    runner.test("Convert octal '0' to decimal", 
                lambda: assert_equal(converter.octal_to_decimal('0'), 0))
    
    runner.test("Convert octal '7' to decimal", 
                lambda: assert_equal(converter.octal_to_decimal('7'), 7))
    
    runner.test("Convert octal '10' to decimal", 
                lambda: assert_equal(converter.octal_to_decimal('10'), 8))
    
    runner.test("Convert octal '17' to decimal", 
                lambda: assert_equal(converter.octal_to_decimal('17'), 15))
    
    runner.test("Convert octal '100' to decimal", 
                lambda: assert_equal(converter.octal_to_decimal('100'), 64))
    
    runner.test("Convert octal '777' to decimal", 
                lambda: assert_equal(converter.octal_to_decimal('777'), 511))
    
    # Decimal to Octal tests
    runner.test("Convert decimal 0 to octal", 
                lambda: assert_equal(converter.decimal_to_octal(0), '0'))
    
    runner.test("Convert decimal 7 to octal", 
                lambda: assert_equal(converter.decimal_to_octal(7), '7'))
    
    runner.test("Convert decimal 8 to octal", 
                lambda: assert_equal(converter.decimal_to_octal(8), '10'))
    
    runner.test("Convert decimal 15 to octal", 
                lambda: assert_equal(converter.decimal_to_octal(15), '17'))
    
    runner.test("Convert decimal 64 to octal", 
                lambda: assert_equal(converter.decimal_to_octal(64), '100'))
    
    runner.test("Convert decimal 511 to octal", 
                lambda: assert_equal(converter.decimal_to_octal(511), '777'))
    
    # Round-trip tests
    runner.test("Round-trip: '12345' -> decimal -> octal",
                lambda: assert_equal(
                    converter.decimal_to_octal(converter.octal_to_decimal('12345')),
                    '12345'
                ))
    
    # Error cases
    runner.test("Invalid octal digit '8' raises error",
                lambda: assert_raises(OctalConversionError, 
                                     lambda: converter.octal_to_decimal('8')))
    
    runner.test("Invalid octal digit '9' raises error",
                lambda: assert_raises(OctalConversionError, 
                                     lambda: converter.octal_to_decimal('19')))
    
    runner.test("Invalid octal string 'abc' raises error",
                lambda: assert_raises(OctalConversionError, 
                                     lambda: converter.octal_to_decimal('abc')))
    
    runner.summary()


def test_basic_arithmetic():
    """Test basic arithmetic operations."""
    print("\n" + "=" * 60)
    print("Testing Basic Arithmetic")
    print("=" * 60)
    
    runner = TestRunner()
    calc = OctalCalculator()
    
    # Addition
    runner.test("10 + 7 = 17 (8 + 7 = 15)",
                lambda: assert_equal(calc.calculate("10 + 7"), "17"))
    
    runner.test("5 + 3 = 10 (5 + 3 = 8)",
                lambda: assert_equal(calc.calculate("5 + 3"), "10"))
    
    runner.test("1 + 1 = 2",
                lambda: assert_equal(calc.calculate("1 + 1"), "2"))
    
    # Subtraction
    runner.test("10 - 7 = 1 (8 - 7 = 1)",
                lambda: assert_equal(calc.calculate("10 - 7"), "1"))
    
    runner.test("20 - 10 = 10 (16 - 8 = 8)",
                lambda: assert_equal(calc.calculate("20 - 10"), "10"))
    
    # Multiplication
    runner.test("5 * 3 = 17 (5 * 3 = 15)",
                lambda: assert_equal(calc.calculate("5 * 3"), "17"))
    
    runner.test("10 * 10 = 100 (8 * 8 = 64)",
                lambda: assert_equal(calc.calculate("10 * 10"), "100"))
    
    # Division
    runner.test("20 / 4 = 4 (16 / 4 = 4)",
                lambda: assert_equal(calc.calculate("20 / 4"), "4"))
    
    runner.test("17 / 3 = 5 (15 / 3 = 5)",
                lambda: assert_equal(calc.calculate("17 / 3"), "5"))
    
    runner.test("10 / 2 = 4 (8 / 2 = 4)",
                lambda: assert_equal(calc.calculate("10 / 2"), "4"))
    
    # Modulo
    runner.test("17 % 10 = 7 (15 % 8 = 7)",
                lambda: assert_equal(calc.calculate("17 % 10"), "7"))
    
    runner.test("20 % 3 = 2 (16 % 3 = 1, wait... 20oct=16dec, 16%3=1=1oct)",
                lambda: assert_equal(calc.calculate("20 % 3"), "1"))
    
    # Exponentiation
    runner.test("2 ^ 3 = 10 (2^3 = 8)",
                lambda: assert_equal(calc.calculate("2 ^ 3"), "10"))
    
    runner.test("3 ^ 2 = 11 (3^2 = 9)",
                lambda: assert_equal(calc.calculate("3 ^ 2"), "11"))
    
    runner.test("10 ^ 2 = 100 (8^2 = 64)",
                lambda: assert_equal(calc.calculate("10 ^ 2"), "100"))
    
    # Division by zero
    runner.test("Division by zero raises error",
                lambda: assert_raises(DivisionByZeroError,
                                     lambda: calc.calculate("10 / 0")))
    
    runner.summary()


def test_pemdas_and_parentheses():
    """Test order of operations (PEMDAS) and parentheses."""
    print("\n" + "=" * 60)
    print("Testing PEMDAS and Parentheses")
    print("=" * 60)
    
    runner = TestRunner()
    calc = OctalCalculator()
    
    # Order of operations
    runner.test("2 + 3 * 4 = 16 (2 + 12 = 14)",
                lambda: assert_equal(calc.calculate("2 + 3 * 4"), "16"))
    
    runner.test("10 - 2 * 3 = 4 (8 - 6 = 2)",
                lambda: assert_equal(calc.calculate("10 - 2 * 3"), "2"))
    
    runner.test("2 ^ 3 + 1 = 11 (8 + 1 = 9)",
                lambda: assert_equal(calc.calculate("2 ^ 3 + 1"), "11"))
    
    # Parentheses override
    runner.test("(2 + 3) * 4 = 24 (5 * 4 = 20)",
                lambda: assert_equal(calc.calculate("(2 + 3) * 4"), "24"))
    
    runner.test("2 * (3 + 4) = 16 (2 * 7 = 14)",
                lambda: assert_equal(calc.calculate("2 * (3 + 4)"), "16"))
    
    runner.test("(10 + 10) / 4 = 4 (16 / 4 = 4)",
                lambda: assert_equal(calc.calculate("(10 + 10) / 4"), "4"))
    
    # Nested parentheses
    runner.test("((2 + 3) * 4) - 5 = 17 ((5 * 4) - 5 = 15)",
                lambda: assert_equal(calc.calculate("((2 + 3) * 4) - 5"), "17"))
    
    runner.test("2 * (3 + (4 * 5)) = 56 (2 * (3 + 20) = 46)",
                lambda: assert_equal(calc.calculate("2 * (3 + (4 * 5))"), "56"))
    
    # Complex expression
    runner.test("(10 + 7) * 2 - 3 / 3 = 35 ((8+7)*2 - 3/3 = 29)",
                lambda: assert_equal(calc.calculate("(10 + 7) * 2 - 3 / 3"), "35"))
    
    runner.summary()


def test_let_bindings():
    """Test LET variable bindings."""
    print("\n" + "=" * 60)
    print("Testing LET Bindings")
    print("=" * 60)
    
    runner = TestRunner()
    calc = OctalCalculator()
    
    # Simple LET
    runner.test("LET x = 10 IN x + 7",
                lambda: assert_equal(calc.calculate("LET x = 10 IN x + 7"), "17"))
    
    runner.test("LET x = 5 IN x * x",
                lambda: assert_equal(calc.calculate("LET x = 5 IN x * x"), "31"))
    
    # LET with expressions
    runner.test("LET x = 2 + 3 IN x * 4",
                lambda: assert_equal(calc.calculate("LET x = 2 + 3 IN x * 4"), "24"))
    
    # Nested LET
    runner.test("LET x = 2 IN LET y = 3 IN x + y",
                lambda: assert_equal(calc.calculate("LET x = 2 IN LET y = 3 IN x + y"), "5"))
    
    runner.test("LET x = 5 IN LET x = 3 IN x",
                lambda: assert_equal(calc.calculate("LET x = 5 IN LET x = 3 IN x"), "3"))
    
    # LET with complex expressions
    runner.test("LET x = 10 IN LET y = 7 IN x * y + x",
                lambda: assert_equal(calc.calculate("LET x = 10 IN LET y = 7 IN x * y + x"), "100"))
    
    # Undefined variable error
    runner.test("Undefined variable raises error",
                lambda: assert_raises(UndefinedVariableError,
                                     lambda: calc.calculate("x + 5")))
    
    runner.summary()


def test_user_defined_functions():
    """Test user-defined functions."""
    print("\n" + "=" * 60)
    print("Testing User-Defined Functions")
    print("=" * 60)
    
    runner = TestRunner()
    calc = OctalCalculator()
    
    # Simple function
    def test_square():
        calc.execute("DEF square(x) = x * x")
        assert_equal(calc.calculate("square(5)"), "31")  # 5^2 = 25
    runner.test("DEF square(x) = x * x; square(5) = 31", test_square)
    
    # Function with multiple parameters
    def test_add():
        calc2 = OctalCalculator()
        calc2.execute("DEF add(x, y) = x + y")
        assert_equal(calc2.calculate("add(5, 3)"), "10")
    runner.test("DEF add(x, y) = x + y; add(5, 3) = 10", test_add)
    
    # Function with complex expression
    def test_complex():
        calc3 = OctalCalculator()
        calc3.execute("DEF formula(x, y) = x * x + y * y")
        assert_equal(calc3.calculate("formula(3, 4)"), "31")  # 9 + 16 = 25
    runner.test("DEF formula(x, y) = x*x + y*y; formula(3, 4) = 31", test_complex)
    
    # Recursive function - factorial
    def test_factorial():
        calc4 = OctalCalculator()
        calc4.execute("DEF factorial(n) = IF n <= 1 THEN 1 ELSE n * factorial(n - 1)")
        assert_equal(calc4.calculate("factorial(5)"), "170")  # 5! = 120
    runner.test("Recursive factorial(5) = 170", test_factorial)
    
    # Recursive function - fibonacci
    def test_fibonacci():
        calc5 = OctalCalculator()
        calc5.execute("DEF fib(n) = IF n <= 1 THEN n ELSE fib(n - 1) + fib(n - 2)")
        assert_equal(calc5.calculate("fib(10)"), "107")  # fib(8) = 21 + 34 = 55
    runner.test("Recursive fib(10) = 107", test_fibonacci)
    
    # Function call errors
    def test_undefined_function():
        calc6 = OctalCalculator()
        assert_raises(UndefinedFunctionError, lambda: calc6.calculate("unknown(5)"))
    runner.test("Undefined function raises error", test_undefined_function)
    
    def test_wrong_arg_count():
        calc7 = OctalCalculator()
        calc7.execute("DEF foo(x, y) = x + y")
        assert_raises(FunctionArgumentError, lambda: calc7.calculate("foo(5)"))
    runner.test("Wrong argument count raises error", test_wrong_arg_count)
    
    runner.summary()


def test_recursive_functions():
    """Test recursive function depth and safety."""
    print("\n" + "=" * 60)
    print("Testing Recursive Functions and Depth Limit")
    print("=" * 60)
    
    runner = TestRunner()
    calc = OctalCalculator()
    
    # Sum of first n numbers
    def test_sum():
        calc.execute("DEF sum(n) = IF n <= 0 THEN 0 ELSE n + sum(n - 1)")
        assert_equal(calc.calculate("sum(10)"), "44")  # sum(8) = 36
    runner.test("Recursive sum(10) = 44", test_sum)
    
    # Sum of squares
    def test_sum_squares():
        calc2 = OctalCalculator()
        calc2.execute("DEF sum_squares(n) = IF n <= 0 THEN 0 ELSE n * n + sum_squares(n - 1)")
        assert_equal(calc2.calculate("sum_squares(5)"), "107")  # 1+4+9+16+25 = 55
    runner.test("Recursive sum_squares(5) = 107", test_sum_squares)
    
    # Deep recursion (should work)
    def test_deep_recursion():
        calc3 = OctalCalculator()
        calc3.execute("DEF countdown(n) = IF n <= 0 THEN 0 ELSE countdown(n - 1)")
        result = calc3.calculate("countdown(100)")  # Should complete
        assert_equal(result, "0")
    runner.test("Deep recursion (100 levels) completes", test_deep_recursion)
    
    # Recursion depth exceeded (should fail)
    def test_infinite_recursion():
        calc4 = OctalCalculator()
        calc4.execute("DEF infinite(n) = infinite(n)")
        assert_raises(RecursionDepthError, lambda: calc4.calculate("infinite(1)"))
    runner.test("Infinite recursion raises RecursionDepthError", test_infinite_recursion)
    
    runner.summary()


def test_conditionals():
    """Test IF-THEN-ELSE conditionals."""
    print("\n" + "=" * 60)
    print("Testing Conditional Expressions")
    print("=" * 60)
    
    runner = TestRunner()
    calc = OctalCalculator()
    
    # Comparison operators
    runner.test("IF 10 > 7 THEN 5 ELSE 3 = 5",
                lambda: assert_equal(calc.calculate("IF 10 > 7 THEN 5 ELSE 3"), "5"))
    
    runner.test("IF 5 < 3 THEN 1 ELSE 0 = 0",
                lambda: assert_equal(calc.calculate("IF 5 < 3 THEN 1 ELSE 0"), "0"))
    
    runner.test("IF 5 == 5 THEN 1 ELSE 0 = 1",
                lambda: assert_equal(calc.calculate("IF 5 == 5 THEN 1 ELSE 0"), "1"))
    
    runner.test("IF 5 != 3 THEN 1 ELSE 0 = 1",
                lambda: assert_equal(calc.calculate("IF 5 != 3 THEN 1 ELSE 0"), "1"))
    
    runner.test("IF 10 >= 10 THEN 1 ELSE 0 = 1",
                lambda: assert_equal(calc.calculate("IF 10 >= 10 THEN 1 ELSE 0"), "1"))
    
    runner.test("IF 5 <= 3 THEN 1 ELSE 0 = 0",
                lambda: assert_equal(calc.calculate("IF 5 <= 3 THEN 1 ELSE 0"), "0"))
    
    # Nested conditionals
    runner.test("Nested IF expressions",
                lambda: assert_equal(
                    calc.calculate("IF 10 > 7 THEN IF 5 > 3 THEN 2 ELSE 1 ELSE 0"),
                    "2"
                ))
    
    # With variables
    runner.test("IF with LET binding",
                lambda: assert_equal(
                    calc.calculate("LET x = 10 IN IF x > 5 THEN x ELSE 0"),
                    "10"
                ))
    
    runner.summary()


def test_feature_integration():
    """Test integration of all features together."""
    print("\n" + "=" * 60)
    print("Testing Feature Integration")
    print("=" * 60)
    
    runner = TestRunner()
    calc = OctalCalculator()
    
    # LET + Function
    def test1():
        calc.execute("DEF double(x) = x * 2")
        result = calc.calculate("LET x = 5 IN double(x)")
        assert_equal(result, "12")  # double(5) = 10
    runner.test("LET + Function: LET x = 5 IN double(x)", test1)
    
    # Function + Conditional
    def test2():
        calc2 = OctalCalculator()
        calc2.execute("DEF max(x, y) = IF x > y THEN x ELSE y")
        assert_equal(calc2.calculate("max(10, 7)"), "10")
    runner.test("Function with conditional: max(10, 7)", test2)
    
    # Recursive + Conditional
    def test3():
        calc3 = OctalCalculator()
        calc3.execute("DEF abs_diff(x, y) = IF x > y THEN x - y ELSE y - x")
        assert_equal(calc3.calculate("abs_diff(3, 10)"), "5")
    runner.test("abs_diff(3, 10) = 5", test3)
    
    # Complex recursive with all features
    def test4():
        calc4 = OctalCalculator()
        calc4.execute("DEF power(base, exp) = IF exp <= 0 THEN 1 ELSE base * power(base, exp - 1)")
        assert_equal(calc4.calculate("power(2, 4)"), "20")  # 2^4 = 16
    runner.test("Recursive power(2, 4) = 20", test4)
    
    # The example from the assignment
    def test5():
        calc5 = OctalCalculator()
        calc5.execute("DEF sum_squares(n) = IF n <= 0 THEN 0 ELSE n * n + sum_squares(n - 1)")
        assert_equal(calc5.calculate("sum_squares(5)"), "107")
    runner.test("Assignment example: sum_squares(5) = 107", test5)
    
    runner.summary()


def test_edge_cases():
    """Test edge cases and boundary conditions."""
    print("\n" + "=" * 60)
    print("Testing Edge Cases")
    print("=" * 60)
    
    runner = TestRunner()
    calc = OctalCalculator()
    
    # Zero operations
    runner.test("0 + 0 = 0",
                lambda: assert_equal(calc.calculate("0 + 0"), "0"))
    
    runner.test("0 * 100 = 0",
                lambda: assert_equal(calc.calculate("0 * 100"), "0"))
    
    runner.test("0 ^ 5 = 0",
                lambda: assert_equal(calc.calculate("0 ^ 5"), "0"))
    
    # Large numbers
    runner.test("777 + 1 = 1000 (511 + 1 = 512)",
                lambda: assert_equal(calc.calculate("777 + 1"), "1000"))
    
    runner.test("1000 * 10 = 10000 (512 * 8 = 4096)",
                lambda: assert_equal(calc.calculate("1000 * 10"), "10000"))
    
    # Empty expressions
    runner.test("Empty expression raises error",
                lambda: assert_raises(EmptyExpressionError,
                                     lambda: calc.calculate("")))
    
    # Mismatched parentheses
    runner.test("Mismatched parentheses raises error",
                lambda: assert_raises(SyntaxError,
                                     lambda: calc.calculate("(1 + 2")))
    
    # Invalid octal in input
    runner.test("Invalid octal digit '8' raises error",
                lambda: assert_raises(OctalConversionError,
                                     lambda: calc.calculate("8 + 1")))
    
    runner.summary()


def test_error_handling():
    """Test comprehensive error handling."""
    print("\n" + "=" * 60)
    print("Testing Error Handling")
    print("=" * 60)
    
    runner = TestRunner()
    calc = OctalCalculator()
    
    # Division by zero
    runner.test("Division by zero",
                lambda: assert_raises(DivisionByZeroError,
                                     lambda: calc.calculate("5 / 0")))
    
    runner.test("Modulo by zero",
                lambda: assert_raises(DivisionByZeroError,
                                     lambda: calc.calculate("5 % 0")))
    
    # Undefined references
    runner.test("Undefined variable",
                lambda: assert_raises(UndefinedVariableError,
                                     lambda: calc.calculate("x + 1")))
    
    runner.test("Undefined function",
                lambda: assert_raises(UndefinedFunctionError,
                                     lambda: calc.calculate("foo(1)")))
    
    # Syntax errors
    runner.test("Invalid syntax",
                lambda: assert_raises((SyntaxError, ParseError),
                                     lambda: calc.calculate("1 + + 2")))
    
    # Invalid octal
    runner.test("Invalid octal '89'",
                lambda: assert_raises(OctalConversionError,
                                     lambda: calc.calculate("89")))
    
    runner.summary()


# Helper functions
def assert_equal(actual, expected):
    """Assert that two values are equal."""
    if actual != expected:
        raise AssertionError(f"Expected '{expected}', got '{actual}'")


def assert_raises(exception_type, func):
    """Assert that a function raises a specific exception."""
    try:
        func()
        raise AssertionError(f"Expected {exception_type.__name__} to be raised")
    except exception_type:
        pass  # Expected
    except Exception as e:
        raise AssertionError(f"Expected {exception_type.__name__}, got {type(e).__name__}: {e}")


def run_all_tests():
    """Run all test suites."""
    print("\n" + "=" * 60)
    print("OCTAL CALCULATOR TEST SUITE")
    print("=" * 60)
    
    test_octal_conversion()
    test_basic_arithmetic()
    test_pemdas_and_parentheses()
    test_let_bindings()
    test_user_defined_functions()
    test_recursive_functions()
    test_conditionals()
    test_feature_integration()
    test_edge_cases()
    test_error_handling()
    
    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()
