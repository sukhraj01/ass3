# Octal Calculator - README

## Project Overview

This is a complete implementation of a calculator that operates entirely in the octal (base-8) number system. The calculator supports arithmetic operations, variable bindings, user-defined recursive functions, and conditional expressions.

## Files Included

1. **octal_calculator.py** - Main implementation with all calculator functionality
2. **exceptions.py** - Custom exception hierarchy for error handling
3. **test_cases.py** - Comprehensive test suite
4. **Report.pdf** - Detailed documentation
5. **README.md** - This file

## Requirements

- Python 3.7 or higher
- No external libraries required (only standard library)

## Installation

No installation required. Simply ensure you have Python 3.7+ installed.

```bash
python --version  # Should be 3.7 or higher
```

## Usage

### Interactive Mode (REPL)

Run the calculator in interactive mode:

```bash
python octal_calculator.py
```

This will start an interactive session where you can:
- Enter arithmetic expressions in octal
- Define functions using DEF syntax
- Use LET bindings and conditionals

Example session:
```
> 10 + 7
  => 17

> DEF square(x) = x * x
  => Function defined successfully

> square(5)
  => 31

> LET x = 10 IN x + 7
  => 17

> IF 10 > 7 THEN 5 ELSE 3
  => 5
```

### Running Tests

Execute the comprehensive test suite:

```bash
python test_cases.py
```

This will run all test cases and display results.

### Using as a Module

You can also import and use the calculator in your own Python code:

```python
from octal_calculator import OctalCalculator

calc = OctalCalculator()

# Basic arithmetic
result = calc.calculate("10 + 7")  # Returns "17"

# Define a function
calc.execute("DEF factorial(n) = IF n <= 1 THEN 1 ELSE n * factorial(n - 1)")

# Call the function
result = calc.calculate("factorial(5)")  # Returns "170" (120 in decimal)
```

## Features

### 1. Octal Arithmetic Operations
- **Operators**: `+`, `-`, `*`, `/`, `%`, `^`
- **PEMDAS** order of operations
- **Nested parentheses** support
- All operations work with octal numbers

Examples:
```
10 + 7      → 17   (8 + 7 = 15)
5 * 3       → 17   (5 * 3 = 15)
2 ^ 3       → 10   (2³ = 8)
(2 + 3) * 4 → 24   (5 * 4 = 20)
```

### 2. Variable Bindings (LET)
- Local variable scoping
- Nested LET bindings
- Variables evaluated in octal

Examples:
```
LET x = 10 IN x + 7                    → 17
LET x = 5 IN x * x                     → 31
LET x = 2 IN LET y = 3 IN x + y        → 5
```

### 3. User-Defined Recursive Functions
- DEF syntax for function definition
- Multiple parameters supported
- Full recursion support
- Recursion depth limit: 1000 calls

Examples:
```
DEF square(x) = x * x
square(5)  → 31

DEF factorial(n) = IF n <= 1 THEN 1 ELSE n * factorial(n - 1)
factorial(5)  → 170  (120 in decimal)
```

### 4. Conditional Expressions
- IF-THEN-ELSE syntax
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Fully nestable
- Works with variables and functions

Examples:
```
IF 10 > 7 THEN 5 ELSE 3                → 5
IF 5 == 5 THEN 1 ELSE 0                → 1
LET x = 10 IN IF x > 5 THEN x ELSE 0   → 10
```

## Input/Output Format

- **All inputs** must be in octal format (digits 0-7 only)
- **All outputs** are returned in octal format
- Invalid octal digits (8, 9) will raise an error

## Error Handling

The calculator includes comprehensive error handling for:
- Invalid octal numbers
- Syntax errors
- Undefined variables/functions
- Division by zero
- Recursion depth exceeded
- Wrong number of function arguments
- And more...

All errors provide informative error messages.

## Assumptions and Limitations

1. **No negative number display**: While the calculator can handle negative intermediate values, the primary focus is on positive octal numbers.

2. **Integer arithmetic only**: Division returns integer results (no fractions).

3. **Recursion limit**: Maximum 1000 recursive calls to prevent stack overflow.

4. **No floating-point**: All calculations are performed with integers.

5. **Octal input only**: Input must be valid octal numbers (0-7 digits).

## Testing

The test suite (`test_cases.py`) includes:
- Octal conversion tests (50+ test cases)
- Basic arithmetic operations
- PEMDAS and parentheses
- LET bindings and scoping
- User-defined functions
- Recursive functions
- Conditional expressions
- Feature integration tests
- Edge cases
- Error handling verification

Run tests with:
```bash
python test_cases.py
```

## Troubleshooting

### "Invalid octal number" error
- Ensure your input only contains digits 0-7
- Check that you're not using 8 or 9

### "Recursion depth exceeded" error
- Your recursive function may have infinite recursion
- Check the base case in your recursive function
- The limit is 1000 calls

### "Undefined variable" error
- Variables must be defined with LET before use
- Check variable names for typos

### "Unexpected token" error
- Check your syntax
- Ensure proper parentheses matching
- Verify keyword spelling (LET, IN, DEF, IF, THEN, ELSE)

## Contact

For issues or questions about this implementation, please refer to the Report.pdf for detailed documentation.

## License

This project is submitted as part of an academic assignment.
