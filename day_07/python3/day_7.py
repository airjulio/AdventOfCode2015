import codecs
import re
from pprint import pprint

# 16-bit signal -> 0 to 65535
MAX_BIT = 65535

BINARY_EXPR_PTN = re.compile(r'^([a-z0-9]{1,2}) (AND|OR|[LR]SHIFT) ([a-z0-9]{1,2})$')
UNARY_EXPR_PTN = re.compile(r'^(NOT) ([a-z]{1,2})$')
ASSIGN_EXPR_PTN = re.compile(r'^[a-z0-9]+$')

VAR_PTN = re.compile(r'^[a-z]+$')

CIRCUIT = dict()


def _is(key, value):
    CIRCUIT[key] = value

def is_literal(s):
    if type(s) == str:
        return str.isdigit(s)
    return False


def is_variable(s):
    return re.match(VAR_PTN, str(s))


def is_expression(s):
    return not is_literal(s) and not is_variable(s)


def process_unknown(input):
    if is_variable(input):
        return CIRCUIT.get(input)
    elif is_expression(input):
        return eval(input)
    else:
        return input

def process_binary(x, y):
    orig_x, orig_y = None, None
    if is_variable(x):
        orig_x = x
    if is_variable(y):
        orig_y = y
    while not is_literal(x):
        x = process_unknown(x)
    while not is_literal(y):
        y = process_unknown(y)
    if orig_x is not None:
        CIRCUIT[orig_x] = x
    if orig_y is not None:
        CIRCUIT[orig_y] = y
    return int(x), int(y)


def process_unary(x):
    orig_x = None
    if is_variable(x):
        orig_x = x
    while not is_literal(x):
        x = process_unknown(x)
    if orig_x is not None:
        CIRCUIT[orig_x] = x
    return int(x)


def AND(x, y):
    x, y = process_binary(x, y)
    return str(x & y)


def OR(x, y):
    x, y = process_binary(x, y)
    return str(x | y)


def NOT(x):
    x = process_unary(x)
    return str(MAX_BIT - x)


def LSHIFT(x, y):
    x, y = process_binary(x, y)
    return str(x << y)


def RSHIFT(x, y):
    x, y = process_binary(x, y)
    return str(x >> y)


def read_expression(expr_text):
    if re.match(BINARY_EXPR_PTN, expr_text):
        m = re.match(BINARY_EXPR_PTN, expr_text)
        return '{1}("{0}", "{2}")'.format(m.group(1), m.group(2), m.group(3))
    elif re.match(UNARY_EXPR_PTN, expr_text):
        m = re.match(UNARY_EXPR_PTN, expr_text)
        return '{0}("{1}")'.format(m.group(1), m.group(2))
    elif re.match(ASSIGN_EXPR_PTN, expr_text):
        m = re.match(ASSIGN_EXPR_PTN, expr_text)
        return m.group(0)


def read_input():
    with codecs.open('../inputb.txt') as f:
        for line in f:
            line = line.strip()
            if not line.startswith('#'):
                expression, var = [i.strip() for i in line.split('->')]
                expression = read_expression(expression)
                _is(var, expression)


def evaluate(circuit):
    for k, v in circuit.items():
        new_value = v
        while not is_literal(new_value):
            new_value = process_unknown(v)
        circuit[k] = new_value


read_input()
evaluate(CIRCUIT)
pprint(CIRCUIT)
