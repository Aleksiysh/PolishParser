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
