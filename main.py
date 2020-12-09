OPERATORS_MATH = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
                  '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y),
                  '~': (3, lambda x: -x),
                  }

OPERATORS_LOG = {
    '-': (1, lambda x: 1 - x),
    '&': (2, lambda x, y: x if x < y else y),
    '|': (3, lambda x, y: x if x > y else y),
    '^': (3, lambda x, y: None),
    '-': (4, lambda x, y: 1 if 1 < 1 - x + y else 1 - x + y),
    '=': (4, lambda x, y: None)
}

OPERATORS = OPERATORS_LOG


# OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
#              '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}


def eval_(formula):
    def parse(formula_string):
        number = ''
        for s in formula_string:
            if s in '1234567890.':
                number += s
            elif number:
                yield float(number)
                number = ''
            if s in OPERATORS or s in "()":
                yield s
        if number:
            yield float(number)

    def shunting_yard(parsed_formula):
        stack = []
        for token in parsed_formula:
            if token in OPERATORS:
                while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                stack.append(token)
            else:
                yield token
        while stack:
            yield stack.pop()

    def calc(polish):
        stack = []
        for token in polish:
            if token in OPERATORS:
                y, x = stack.pop(), stack.pop()
                stack.append(OPERATORS[token][1](x, y))
            else:
                stack.append(token)
        return stack[0]

    return calc(shunting_yard(parse(formula)))


def print_hi(name):
    x = 1
    y = 0
    print(eval_(f"{x} - {y}"))
    # print(1 and 0)
    str_to_fstr("sss",1,2,3,4,5)


def str_to_fstr(str, *args):
    s = "asas a"
    a =5
    ss = s.replace(' a',' $a')
    print(s)
    print(ss)
    pass

if __name__ == '__main__':
    print_hi('PyCharm')
