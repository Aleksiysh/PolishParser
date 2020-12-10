# OPERATORS_MATH = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
#                   '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y),
#                   '~': (3, lambda x: -x), '^': (3, lambda x, y: x ** y),
#                   }

OPERATORS_LOG = {
    '!': (1, lambda x: inv(x)),
    '&': (2, lambda x, y: conj(x, y)),
    '|': (3, lambda x, y: disj(x, y)),
    '^': (3, lambda x, y: disj(conj(inv(x), y), conj(x, inv(y)))),
    '-': (4, lambda x, y: 1 if 1 < 1 - x + y else 1 - x + y),
    '=': (4, lambda x, y: disj(conj(inv(x), y), conj(x, inv(y))))
}


def inv(x):
    return 1 - x


def conj(x, y):
    return x if x < y else y


def disj(x, y):
    return x if x > y else y


OPERATORS = OPERATORS_LOG


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
                if token in ('!', '~'):
                    x = stack.pop()
                    stack.append(OPERATORS[token][1](x))
                else:
                    y, x = stack.pop(), stack.pop()
                    stack.append(OPERATORS[token][1](x, y))
            else:
                stack.append(token)
        return stack[0]

    return calc(shunting_yard(parse(formula)))


def main():
    log = '''Список операций (в скобках как записывать):
! инверсия (!a);
& конъюнкция (a&b);
| дизъюнкция (a|b);
^ строгая дизъюнкция (a^b);
- импликация a->b (a-b);
= эквивиаленция a<->b (a=b);
() скобки
'''

    print(log)

    arr = []

    n = int(input("Количество аргументов: "))
    q = int(input("Система счисления: "))
    str1 = input("функция: ")

    for i in range(q ** n):
        a = convert_base(i, q, 10).zfill(n)
        arr.append(a)

    for aaa in arr:
        print(aaa, end=' ')
        print(int(eval_(str_to_fstr(str1, *aaa))))


def str_to_fstr(str1, *args):
    for i in range(5):
        str1 = str1.replace(chr(ord('a') + i), '{' + str(i) + '}')
    return str1.format(*args)


def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


if __name__ == '__main__':
    main()
