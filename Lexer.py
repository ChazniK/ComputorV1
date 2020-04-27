import sys, re

class Lexer:
    def __init__(self):
        self.lhs = []
        self.rhs = []

        if len(sys.argv) != 2:
            print("There should only be 2 arguments")
            sys.exit()

    def remove_whitespace(self, expression):
        expression_no_space = expression.replace(" ", "")
        return expression_no_space

    def split_into_lhs_rhs(self, expression):
        expression_no_space = self.remove_whitespace(expression)
        lhs_rhs = expression_no_space.split("=")
        return lhs_rhs

    def tokenize(self, expression):
        try:
            lhs = self.split_into_lhs_rhs(expression)[0]
            rhs = self.split_into_lhs_rhs(expression)[1]
            self.lhs = re.findall(r'[-+]?\d*\.?\d+\*[a-zA-Z]\^\d*', lhs)
            self.rhs = re.findall(r'[-+]?\d*\.?\d+\*[a-zA-Z]\^\d*', rhs)
        except:
            print("Invalid expression, can not be split into left and right hand sides")