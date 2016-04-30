# -*- coding: utf-8 -*-

import hashlib
import sys

h = hashlib.md5()

def find_lowest(key):
  number_found = False
  number = 1
  while not number_found:
    s = '%s%i' % (key, number)
    generated = get_md5(s)
    if generated.startswith('00000'):
      number_found = True
      print(number)
    number += 1

def get_md5(s):
  h.update(s.encode('ascii', 'ignore'))
  return h.hexdigest()

if __name__ == '__main__':
  print(get_md5('abcdef609043'))
  print(get_md5('pqrstuv1048970'))
  print(get_md5('abcdef%s' % str(609043)))
  print(get_md5('pqrstuv%s' % str(1048970)))
