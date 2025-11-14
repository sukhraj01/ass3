"""
Octal Calculator - A Complete Implementation

This module implements a calculator that operates entirely in the octal (base-8) number system.
It supports arithmetic operations, variable bindings, user-defined recursive functions, and
conditional expressions.

Key Features:
- Custom octal to decimal and decimal to octal conversion (no built-in functions)
- PEMDAS order of operations with nested parentheses
- LET bindings for local variable scoping
- DEF syntax for user-defined recursive functions
- IF-THEN-ELSE conditional expressions
- Recursion depth tracking (max 1000 calls)
- Comprehensive error handling and assertions
"""

import re
from exceptions import *


class OctalConverter:
    """
    Handles conversion between octal and decimal number systems without using built-in functions.
    
    Algorithm:
    - Octal to Decimal: Multiply each digit by 8^position and sum
    - Decimal to Octal: Repeatedly divide by 8 and collect remainders
    """
    
    @staticmethod
    def octal_to_decimal(octal_str):
        """
        Convert octal string to decimal integer.
        
        Args:
            octal_str: String representation of octal number
            
        Returns:
            Decimal integer value
            
        Raises:
            OctalConversionError: If string contains invalid octal digits
        """
        # Pre-condition: input must be a string
        assert isinstance(octal_str, str), "Octal input must be a string"
        
        octal_str = octal_str.strip()
        
        # Handle empty string
        if not octal_str:
            raise OctalConversionError(octal_str, "Empty octal string")
        
        # Handle negative numbers
        is_negative = False
        if octal_str[0] == '-':
            is_negative = True
            octal_str = octal_str[1:]
        
        # Validate octal digits (0-7 only)
        for char in octal_str:
            if char not in '01234567':
                raise OctalConversionError(octal_str)
        
        # Convert using positional notation: sum(digit * 8^position)
        decimal_value = 0
        power = 0
        
        # Process from right to left
        for i in range(len(octal_str) - 1, -1, -1):
            digit = int(octal_str[i])
            # Invariant: digit must be 0-7
            assert 0 <= digit <= 7, f"Invalid octal digit: {digit}"
            
            decimal_value += digit * (8 ** power)
            power += 1
        
        # Post-condition: result must be non-negative before applying sign
        assert decimal_value >= 0, "Conversion produced negative value"
        
        return -decimal_value if is_negative else decimal_value
    
    @staticmethod
    def decimal_to_octal(decimal_int):
        """
        Convert decimal integer to octal string.
        
        Args:
            decimal_int: Decimal integer value
            
        Returns:
            String representation in octal
        """
        # Pre-condition: input must be an integer
        assert isinstance(decimal_int, int), "Decimal input must be an integer"
        
        # Handle zero specially
        if decimal_int == 0:
            return "0"
        
        # Handle negative numbers
        is_negative = False
        if decimal_int < 0:
            is_negative = True
            decimal_int = -decimal_int
        
        # Convert by repeatedly dividing by 8 and collecting remainders
        octal_digits = []
        while decimal_int > 0:
            remainder = decimal_int % 8
            # Invariant: remainder must be 0-7
            assert 0 <= remainder <= 7, f"Invalid remainder in conversion: {remainder}"
            
            octal_digits.append(str(remainder))
            decimal_int = decimal_int // 8
        
        # Reverse to get correct order
        octal_str = ''.join(reversed(octal_digits))
        
        # Post-condition: result should only contain 0-7
        assert all(c in '01234567' for c in octal_str), "Invalid octal string produced"
        
        return ('-' + octal_str) if is_negative else octal_str


class Token:
    """Represents a token in the expression."""
    
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        return f"Token({self.type}, {self.value})"


class Lexer:
    """
    Tokenizes input expressions into meaningful tokens.
    
    Token Types:
    - NUMBER: Octal numbers
    - OPERATOR: +, -, *, /, %, ^
    - LPAREN, RPAREN: Parentheses
    - KEYWORD: LET, IN, DEF, IF, THEN, ELSE
    - IDENTIFIER: Variable and function names
    - COMMA: Function argument separator
    - EQUALS: Assignment and comparison
    - COMPARISON: <, >, <=, >=, ==, !=
    """
    
    def __init__(self, text):
        self.text = text
        self.pos = 0
        
    def tokenize(self):
        """
        Convert input text into list of tokens.
        
        Returns:
            List of Token objects
        """
        tokens = []
        
        while self.pos < len(self.text):
            # Skip whitespace
            if self.text[self.pos].isspace():
                self.pos += 1
                continue
            
            # Numbers (octal digits)
            if self.text[self.pos].isdigit():
                tokens.append(self._read_number())
                continue
            
            # Identifiers and keywords
            if self.text[self.pos].isalpha() or self.text[self.pos] == '_':
                tokens.append(self._read_identifier())
                continue
            
            # Two-character operators
            if self.pos + 1 < len(self.text):
                two_char = self.text[self.pos:self.pos + 2]
                if two_char in ['<=', '>=', '==', '!=']:
                    tokens.append(Token('COMPARISON', two_char))
                    self.pos += 2
                    continue
            
            # Single-character tokens
            char = self.text[self.pos]
            if char == '+':
                tokens.append(Token('OPERATOR', '+'))
            elif char == '-':
                tokens.append(Token('OPERATOR', '-'))
            elif char == '*':
                tokens.append(Token('OPERATOR', '*'))
            elif char == '/':
                tokens.append(Token('OPERATOR', '/'))
            elif char == '%':
                tokens.append(Token('OPERATOR', '%'))
            elif char == '^':
                tokens.append(Token('OPERATOR', '^'))
            elif char == '(':
                tokens.append(Token('LPAREN', '('))
            elif char == ')':
                tokens.append(Token('RPAREN', ')'))
            elif char == ',':
                tokens.append(Token('COMMA', ','))
            elif char == '=':
                tokens.append(Token('EQUALS', '='))
            elif char == '<':
                tokens.append(Token('COMPARISON', '<'))
            elif char == '>':
                tokens.append(Token('COMPARISON', '>'))
            else:
                raise ParseError(self.text, self.pos, f"Unexpected character: '{char}'")
            
            self.pos += 1
        
        return tokens
    
    def _read_number(self):
        """Read a number token (octal digits only)."""
        start = self.pos
        while self.pos < len(self.text) and self.text[self.pos].isdigit():
            self.pos += 1
        
        num_str = self.text[start:self.pos]
        
        # Validate octal digits
        for char in num_str:
            if char not in '01234567':
                raise OctalConversionError(num_str)
        
        return Token('NUMBER', num_str)
    
    def _read_identifier(self):
        """Read an identifier or keyword token."""
        start = self.pos
        while self.pos < len(self.text) and (self.text[self.pos].isalnum() or self.text[self.pos] == '_'):
            self.pos += 1
        
        text = self.text[start:self.pos]
        
        # Check if it's a keyword
        if text in ['LET', 'IN', 'DEF', 'IF', 'THEN', 'ELSE']:
            return Token('KEYWORD', text)
        
        return Token('IDENTIFIER', text)


class ASTNode:
    """Base class for Abstract Syntax Tree nodes."""
    pass


class NumberNode(ASTNode):
    """Represents a number literal (in octal)."""
    
    def __init__(self, value):
        self.value = value  # String in octal format


class BinaryOpNode(ASTNode):
    """Represents a binary operation."""
    
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


class UnaryOpNode(ASTNode):
    """Represents a unary operation (e.g., negation)."""
    
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand


class VariableNode(ASTNode):
    """Represents a variable reference."""
    
    def __init__(self, name):
        self.name = name


class LetNode(ASTNode):
    """Represents a LET binding: LET var = value IN expression."""
    
    def __init__(self, var_name, value_expr, body_expr):
        self.var_name = var_name
        self.value_expr = value_expr
        self.body_expr = body_expr


class FunctionCallNode(ASTNode):
    """Represents a function call."""
    
    def __init__(self, func_name, arguments):
        self.func_name = func_name
        self.arguments = arguments


class ConditionalNode(ASTNode):
    """Represents an IF-THEN-ELSE conditional."""
    
    def __init__(self, condition, then_expr, else_expr):
        self.condition = condition
        self.then_expr = then_expr
        self.else_expr = else_expr


class ComparisonNode(ASTNode):
    """Represents a comparison operation."""
    
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


class Parser:
    """
    Recursive descent parser for the octal calculator language.
    
    Grammar (simplified):
    expression := let_expr | conditional | comparison
    let_expr := LET IDENTIFIER = expression IN expression
    conditional := IF comparison THEN expression ELSE expression
    comparison := arith_expr [COMP_OP arith_expr]
    arith_expr := term ((+|-) term)*
    term := factor ((*|/|%) factor)*
    factor := power
    power := atom (^ atom)*
    atom := NUMBER | IDENTIFIER | function_call | (expression) | -atom
    """
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def parse(self):
        """Parse tokens into an AST."""
        if not self.tokens:
            raise EmptyExpressionError()
        
        ast = self.expression()
        
        # Ensure all tokens consumed
        if self.pos < len(self.tokens):
            raise SyntaxError(f"Unexpected token: {self.tokens[self.pos]}")
        
        return ast
    
    def current_token(self):
        """Get current token without consuming it."""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None
    
    def consume(self, expected_type=None, expected_value=None):
        """Consume and return current token."""
        token = self.current_token()
        
        if token is None:
            raise SyntaxError("Unexpected end of expression")
        
        if expected_type and token.type != expected_type:
            raise SyntaxError(f"Expected {expected_type}, got {token.type}")
        
        if expected_value and token.value != expected_value:
            raise SyntaxError(f"Expected '{expected_value}', got '{token.value}'")
        
        self.pos += 1
        return token
    
    def expression(self):
        """Parse a full expression."""
        token = self.current_token()
        
        if token and token.type == 'KEYWORD':
            if token.value == 'LET':
                return self.let_expression()
            elif token.value == 'IF':
                return self.conditional_expression()
        
        return self.comparison()
    
    def let_expression(self):
        """Parse: LET var = value IN body."""
        self.consume('KEYWORD', 'LET')
        var_token = self.consume('IDENTIFIER')
        self.consume('EQUALS')
        value_expr = self.expression()
        self.consume('KEYWORD', 'IN')
        body_expr = self.expression()
        
        return LetNode(var_token.value, value_expr, body_expr)
    
    def conditional_expression(self):
        """Parse: IF condition THEN expr1 ELSE expr2."""
        self.consume('KEYWORD', 'IF')
        condition = self.comparison()
        self.consume('KEYWORD', 'THEN')
        then_expr = self.expression()
        self.consume('KEYWORD', 'ELSE')
        else_expr = self.expression()
        
        return ConditionalNode(condition, then_expr, else_expr)
    
    def comparison(self):
        """Parse comparison expressions."""
        left = self.arithmetic_expression()
        
        token = self.current_token()
        if token and token.type == 'COMPARISON':
            op = self.consume('COMPARISON')
            right = self.arithmetic_expression()
            return ComparisonNode(left, op.value, right)
        
        return left
    
    def arithmetic_expression(self):
        """Parse addition and subtraction."""
        left = self.term()
        
        while True:
            token = self.current_token()
            if token and token.type == 'OPERATOR' and token.value in ['+', '-']:
                op = self.consume('OPERATOR')
                right = self.term()
                left = BinaryOpNode(left, op.value, right)
            else:
                break
        
        return left
    
    def term(self):
        """Parse multiplication, division, and modulo."""
        left = self.power()
        
        while True:
            token = self.current_token()
            if token and token.type == 'OPERATOR' and token.value in ['*', '/', '%']:
                op = self.consume('OPERATOR')
                right = self.power()
                left = BinaryOpNode(left, op.value, right)
            else:
                break
        
        return left
    
    def power(self):
        """Parse exponentiation (right-associative)."""
        left = self.atom()
        
        token = self.current_token()
        if token and token.type == 'OPERATOR' and token.value == '^':
            self.consume('OPERATOR')
            right = self.power()  # Right-associative
            return BinaryOpNode(left, '^', right)
        
        return left
    
    def atom(self):
        """Parse atomic expressions."""
        token = self.current_token()
        
        if not token:
            raise SyntaxError("Unexpected end of expression")
        
        # Number
        if token.type == 'NUMBER':
            self.consume('NUMBER')
            return NumberNode(token.value)
        
        # Parenthesized expression
        if token.type == 'LPAREN':
            self.consume('LPAREN')
            expr = self.expression()
            self.consume('RPAREN')
            return expr
        
        # Unary minus
        if token.type == 'OPERATOR' and token.value == '-':
            self.consume('OPERATOR')
            operand = self.atom()
            return UnaryOpNode('-', operand)
        
        # Identifier (variable or function call)
        if token.type == 'IDENTIFIER':
            name = self.consume('IDENTIFIER').value
            
            # Check if it's a function call
            if self.current_token() and self.current_token().type == 'LPAREN':
                self.consume('LPAREN')
                args = []
                
                # Parse arguments
                if self.current_token() and self.current_token().type != 'RPAREN':
                    args.append(self.expression())
                    
                    while self.current_token() and self.current_token().type == 'COMMA':
                        self.consume('COMMA')
                        args.append(self.expression())
                
                self.consume('RPAREN')
                return FunctionCallNode(name, args)
            
            # Just a variable
            return VariableNode(name)
        
        raise SyntaxError(f"Unexpected token: {token}")


class FunctionDefinition:
    """Represents a user-defined function."""
    
    def __init__(self, name, params, body_ast):
        self.name = name
        self.params = params
        self.body_ast = body_ast


class Evaluator:
    """
    Evaluates the AST and performs calculations in octal.
    
    Maintains:
    - Variable environment (scoped)
    - Function definitions (global)
    - Recursion depth counter
    """
    
    MAX_RECURSION_DEPTH = 1000
    
    def __init__(self):
        self.functions = {}  # Global function store
        self.recursion_depth = 0
        self.converter = OctalConverter()
    
    def define_function(self, name, params, body_ast):
        """Store a function definition."""
        # Pre-condition: params must be a list
        assert isinstance(params, list), "Function parameters must be a list"
        
        self.functions[name] = FunctionDefinition(name, params, body_ast)
    
    def evaluate(self, ast, environment=None):
        """
        Evaluate an AST node and return the result in octal.
        
        Args:
            ast: AST node to evaluate
            environment: Dictionary of variable bindings
            
        Returns:
            Result as octal string
        """
        if environment is None:
            environment = {}
        
        # Pre-condition: environment must be a dictionary
        assert isinstance(environment, dict), "Environment must be a dictionary"
        
        if isinstance(ast, NumberNode):
            return ast.value
        
        elif isinstance(ast, VariableNode):
            if ast.name not in environment:
                raise UndefinedVariableError(ast.name)
            return environment[ast.name]
        
        elif isinstance(ast, UnaryOpNode):
            operand_octal = self.evaluate(ast.operand, environment)
            operand_decimal = self.converter.octal_to_decimal(operand_octal)
            
            if ast.operator == '-':
                result_decimal = -operand_decimal
            else:
                raise InvalidOperationError(f"Unknown unary operator: {ast.operator}")
            
            return self.converter.decimal_to_octal(result_decimal)
        
        elif isinstance(ast, BinaryOpNode):
            left_octal = self.evaluate(ast.left, environment)
            right_octal = self.evaluate(ast.right, environment)
            
            left_decimal = self.converter.octal_to_decimal(left_octal)
            right_decimal = self.converter.octal_to_decimal(right_octal)
            
            result_decimal = self._perform_operation(ast.operator, left_decimal, right_decimal)
            
            return self.converter.decimal_to_octal(result_decimal)
        
        elif isinstance(ast, LetNode):
            # Evaluate the value expression in current environment
            value_octal = self.evaluate(ast.value_expr, environment)
            
            # Create new environment with the binding
            new_env = environment.copy()
            new_env[ast.var_name] = value_octal
            
            # Evaluate body in new environment
            return self.evaluate(ast.body_expr, new_env)
        
        elif isinstance(ast, FunctionCallNode):
            return self._evaluate_function_call(ast, environment)
        
        elif isinstance(ast, ConditionalNode):
            return self._evaluate_conditional(ast, environment)
        
        elif isinstance(ast, ComparisonNode):
            left_octal = self.evaluate(ast.left, environment)
            right_octal = self.evaluate(ast.right, environment)
            
            left_decimal = self.converter.octal_to_decimal(left_octal)
            right_decimal = self.converter.octal_to_decimal(right_octal)
            
            result = self._perform_comparison(ast.operator, left_decimal, right_decimal)
            
            # Return 1 (true) or 0 (false) in octal
            return "1" if result else "0"
        
        else:
            raise InvalidOperationError(f"Unknown AST node type: {type(ast)}")
    
    def _perform_operation(self, operator, left, right):
        """Perform arithmetic operation on decimal values."""
        # Pre-condition: operands must be integers
        assert isinstance(left, int), "Left operand must be integer"
        assert isinstance(right, int), "Right operand must be integer"
        
        if operator == '+':
            result = left + right
        elif operator == '-':
            result = left - right
        elif operator == '*':
            result = left * right
        elif operator == '/':
            if right == 0:
                raise DivisionByZeroError()
            result = left // right  # Integer division
        elif operator == '%':
            if right == 0:
                raise DivisionByZeroError()
            result = left % right
        elif operator == '^':
            if right < 0:
                raise InvalidOperationError("Negative exponents not supported")
            result = left ** right
        else:
            raise InvalidOperationError(f"Unknown operator: {operator}")
        
        # Post-condition: result must be an integer
        assert isinstance(result, int), "Operation must produce integer result"
        
        return result
    
    def _perform_comparison(self, operator, left, right):
        """Perform comparison on decimal values."""
        if operator == '==':
            return left == right
        elif operator == '!=':
            return left != right
        elif operator == '<':
            return left < right
        elif operator == '>':
            return left > right
        elif operator == '<=':
            return left <= right
        elif operator == '>=':
            return left >= right
        else:
            raise InvalidOperationError(f"Unknown comparison operator: {operator}")
    
    def _evaluate_function_call(self, call_node, environment):
        """Evaluate a function call with recursion depth tracking."""
        func_name = call_node.func_name
        
        if func_name not in self.functions:
            raise UndefinedFunctionError(func_name)
        
        func_def = self.functions[func_name]
        
        # Check argument count
        if len(call_node.arguments) != len(func_def.params):
            raise FunctionArgumentError(
                func_name,
                len(func_def.params),
                len(call_node.arguments)
            )
        
        # Check recursion depth
        self.recursion_depth += 1
        if self.recursion_depth > self.MAX_RECURSION_DEPTH:
            self.recursion_depth -= 1
            raise RecursionDepthError(self.MAX_RECURSION_DEPTH)
        
        try:
            # Evaluate arguments in current environment
            arg_values = []
            for arg_ast in call_node.arguments:
                arg_octal = self.evaluate(arg_ast, environment)
                arg_values.append(arg_octal)
            
            # Create new environment for function body
            func_env = {}
            for param, value in zip(func_def.params, arg_values):
                func_env[param] = value
            
            # Evaluate function body
            result = self.evaluate(func_def.body_ast, func_env)
            
            return result
        finally:
            # Always decrement depth, even if error occurs
            self.recursion_depth -= 1
    
    def _evaluate_conditional(self, cond_node, environment):
        """Evaluate IF-THEN-ELSE conditional."""
        # Evaluate condition
        condition_result = self.evaluate(cond_node.condition, environment)
        
        # Convert to boolean (0 is false, anything else is true)
        condition_decimal = self.converter.octal_to_decimal(condition_result)
        
        if condition_decimal != 0:
            return self.evaluate(cond_node.then_expr, environment)
        else:
            return self.evaluate(cond_node.else_expr, environment)


class OctalCalculator:
    """
    Main calculator class that orchestrates all components.
    
    Usage:
    calc = OctalCalculator()
    result = calc.calculate("10 + 7")  # Returns "17" in octal
    calc.execute("DEF square(x) = x * x")
    result = calc.calculate("square(5)")  # Returns "31" in octal
    """
    
    def __init__(self):
        self.evaluator = Evaluator()
    
    def execute(self, expression):
        """
        Execute an expression (for DEF statements).
        
        Args:
            expression: String expression
            
        Returns:
            Message indicating success, or result for calculations
        """
        expression = expression.strip()
        
        if not expression:
            raise EmptyExpressionError()
        
        # Check if it's a function definition
        if expression.startswith('DEF '):
            self._define_function(expression)
            return f"Function defined successfully"
        
        # Otherwise, evaluate as expression
        return self.calculate(expression)
    
    def calculate(self, expression):
        """
        Calculate an expression and return result in octal.
        
        Args:
            expression: String expression in octal
            
        Returns:
            Result as octal string
        """
        expression = expression.strip()
        
        if not expression:
            raise EmptyExpressionError()
        
        # Tokenize
        lexer = Lexer(expression)
        tokens = lexer.tokenize()
        
        # Parse
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Evaluate
        result = self.evaluator.evaluate(ast)
        
        return result
    
    def _define_function(self, definition):
        """Parse and store a function definition."""
        # Pattern: DEF name(param1, param2, ...) = expression
        match = re.match(r'DEF\s+(\w+)\s*\(([^)]*)\)\s*=\s*(.+)', definition)
        
        if not match:
            raise SyntaxError("Invalid function definition syntax")
        
        func_name = match.group(1)
        params_str = match.group(2).strip()
        body_str = match.group(3).strip()
        
        # Parse parameters
        if params_str:
            params = [p.strip() for p in params_str.split(',')]
        else:
            params = []
        
        # Parse body expression
        lexer = Lexer(body_str)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        body_ast = parser.parse()
        
        # Store function
        self.evaluator.define_function(func_name, params, body_ast)


def main():
    """Interactive REPL for testing."""
    calc = OctalCalculator()
    
    print("Octal Calculator (Base-8)")
    print("=" * 40)
    print("Commands:")
    print("  - Enter expressions in octal")
    print("  - DEF name(params) = expression")
    print("  - Type 'quit' to exit")
    print("=" * 40)
    
    while True:
        try:
            line = input("\n> ").strip()
            
            if not line:
                continue
            
            if line.lower() in ['quit', 'exit', 'q']:
                break
            
            result = calc.execute(line)
            print(f"  => {result}")
            
        except OctalCalculatorError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()