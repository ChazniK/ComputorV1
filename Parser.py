import sys, re

class Lexer:
    def __init__(self):
        self.lhs = []
        self.rhs = []

        if len(sys.argv) != 2:
            raise Exception("There should only be 2 arguments")

    def split_into_lhs_rhs(self, expression):
        expression_no_space = expression.replace(" ", "")
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
        

class Parser:

    def simplify_expression(self):
        lexer = Lexer()
        lexer.tokenize(sys.argv[1])
        new_token = ""
        for token in lexer.rhs:
            if token[0] == "+":
                new_token = "-" + token[1:]
            elif str.isdigit(token[0]):
                new_token += "-" + token
            elif token[0] == "-":
                new_token = "+" + token[1:]
            lexer.lhs.append(new_token)
        return lexer.lhs

    def print_simplified_expression(self):
        expression_list = self.simplify_expression()
        expression = "Reduced form: "
        for token in expression_list:
            expression += token
        expression += " = 0"
        print(expression, end="")


p = Parser()
p.print_simplified_expression()
