"""
Custom Exception Hierarchy for Octal Calculator

This module defines a comprehensive exception hierarchy for handling
all possible error scenarios in the octal calculator system.

Design Rationale:
- Base OctalCalculatorError for catching any calculator-related error
- Specific exceptions for each error category to enable precise error handling
- Informative error messages that help users identify and fix issues
"""


class OctalCalculatorError(Exception):
    """Base exception for all octal calculator errors."""
    pass


class OctalConversionError(OctalCalculatorError):
    """Raised when octal number conversion fails."""
    
    def __init__(self, value, message=None):
        self.value = value
        if message is None:
            message = f"Invalid octal number: '{value}'. Octal numbers can only contain digits 0-7."
        super().__init__(message)


class ParseError(OctalCalculatorError):
    """Raised when expression parsing fails."""
    
    def __init__(self, expression, position=None, message=None):
        self.expression = expression
        self.position = position
        if message is None:
            if position is not None:
                message = f"Parse error at position {position} in expression: '{expression}'"
            else:
                message = f"Parse error in expression: '{expression}'"
        super().__init__(message)


class SyntaxError(ParseError):
    """Raised for syntax errors in expressions."""
    
    def __init__(self, message, expression=None):
        self.message = message
        super().__init__(expression or "", message=message)


class UndefinedVariableError(OctalCalculatorError):
    """Raised when accessing an undefined variable."""
    
    def __init__(self, variable_name):
        self.variable_name = variable_name
        super().__init__(f"Undefined variable: '{variable_name}'")


class UndefinedFunctionError(OctalCalculatorError):
    """Raised when calling an undefined function."""
    
    def __init__(self, function_name):
        self.function_name = function_name
        super().__init__(f"Undefined function: '{function_name}'")


class FunctionArgumentError(OctalCalculatorError):
    """Raised when function is called with wrong number of arguments."""
    
    def __init__(self, function_name, expected, provided):
        self.function_name = function_name
        self.expected = expected
        self.provided = provided
        super().__init__(
            f"Function '{function_name}' expects {expected} argument(s), "
            f"but {provided} were provided"
        )


class RecursionDepthError(OctalCalculatorError):
    """Raised when recursion depth exceeds the maximum limit."""
    
    def __init__(self, max_depth=1000):
        self.max_depth = max_depth
        super().__init__(
            f"Recursion depth exceeded maximum limit of {max_depth} calls. "
            "This may indicate infinite recursion."
        )


class DivisionByZeroError(OctalCalculatorError):
    """Raised when attempting division by zero."""
    
    def __init__(self):
        super().__init__("Division by zero is undefined")


class InvalidOperationError(OctalCalculatorError):
    """Raised for invalid mathematical operations."""
    
    def __init__(self, operation, message=None):
        self.operation = operation
        if message is None:
            message = f"Invalid operation: {operation}"
        super().__init__(message)


class NegativeNumberError(OctalCalculatorError):
    """Raised when negative numbers are encountered (if not supported)."""
    
    def __init__(self, message="Negative numbers are not supported in octal representation"):
        super().__init__(message)


class EmptyExpressionError(ParseError):
    """Raised when an empty expression is provided."""
    
    def __init__(self):
        super().__init__("", message="Empty expression provided")
