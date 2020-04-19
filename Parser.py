import sys

class Polynomial:
    def __init__(self, sign, coefficient, variable, degree):
        self.sign = sign
        self.coefficient = coefficient
        self.variable = variable
        self.degree = degree


class Equation:
    def __init__(self):
        self.list_of_polynomials = []


class Parser:
    def __init__(self):

        if len(sys.argv) != 2:
            raise Exception("There should only be 2 arguments")

    def remove_white_space(self, expression):
        expression_no_spaces = ""
        for char in expression:
            if char == " ":
                continue
            else:
                expression_no_spaces += char
        return expression_no_spaces

    def separate_into_parts(self, expression):
        parts = []
        for char in expression:


       




            




parser = Parser()
expression = parser.remove_white_space(sys.argv[1])
parser.separate_into_parts(expression)