import sys

class Parser:
    def __init__(self, expression):
        self.expression = expression

        if len(sys.argv) != 2:
            raise Exception("There should only be 2 arguments")

    def remove_white_space(self, expression):
        expression = ""
        for letter in expression:
            if letter == " ":
                continue
            else:
                expression += letter
        return expression


    



p = Parser("")
exp = p.remove_white_space("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
p.separate_into_parts(exp)
