from read_input import *
import re

RULE_1 = re.compile(r'[aeiou].*[aeiou].*[aeiou]')
RULE_2 = re.compile(r'([a-z])\1')
RULE_3 = re.compile(r'(ab|cd|pq|xy)')

RULE_4 = re.compile(r'([a-z][a-z]).*\1')
RULE_5 = re.compile(r'([a-z]).\1')


def validate(s):
    if RULE_1.search(s) and RULE_2.search(s) and not RULE_3.search(s):
        return True
    return False


def validate2(s):
    if RULE_4.search(s) and RULE_5.search(s):
        return True
    return False

total = 0
for line in read_input():
    if validate(line):
        total += 1
print(total)

total = 0
for line in read_input():
    if validate2(line):
        total += 1
print(total)