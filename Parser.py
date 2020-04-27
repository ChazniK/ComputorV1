import sys, re
from Lexer import Lexer

class Parser:
    def __init__(self):
        self.expression = []

    def count_char_in_list(self, lhs_rhs):
        count = 0
        for token in lhs_rhs:
            count += len(token)
        return count

    def validate_expression(self, expression):
        lexer = Lexer()
        lexer.tokenize(expression)
        expected_length = len(lexer.remove_whitespace(expression))
        actual_length = self.count_char_in_list(lexer.lhs) + self.count_char_in_list(lexer.rhs) + 1
        if expected_length == actual_length:
            self.expression.append(lexer.lhs)
            self.expression.append(lexer.rhs)
            return True
        else:
            return False

    def simplify_expression(self):
        expression = ""
        for lhs in self.expression[0]:
            expression += lhs
        for rhs in self.expression[1]:
            if str.isdigit(rhs[0]):
                rhs = "-" + rhs
            elif rhs[0] == "+":
                rhs = "-" + rhs[1:]
            elif rhs[0] == "-":
                rhs = "+" + rhs[1:]
            expression += rhs
        expression += " = 0"
        return expression

    def degree_of_expression(self):
        expression = self.simplify_expression()
        exponents = re.findall(r'\^(\d+)', expression)
        exponents = [int(i) for i in exponents]
        highest_exponent = max(exponents)
        return highest_exponent

    def print_expression(self):
        expression = self.simplify_expression()
        print("Reduced form:", expression)
        degree = self.degree_of_expression()
        print("Polynomial degree:", degree, end="")

  

if __name__ == '__main__':

    parser = Parser()
    if parser.validate_expression(sys.argv[1]):
        parser.print_expression()
