#!/usr/bin/env python
# -*- coding: latin-1 -*-
from price import Price
import unittest

parsing_tests = { 
  "no symbol":            ["1.00", None],
  "standard price":       ["R$1,99", Price(1, 99)],
  "no cents":             ["R$500", Price(500)],
  "whitespace":           ["R $4 12,53", Price(412, 53)],
  "point":                ["R$ 9.000,50", Price(9000, 50)],
  "point and whitespace":      ["R$ 1. 20 0,2 5", Price(1200, 25)],
  "even more whitespace": ["R$  7  02  1 , 0 9", Price(7021, 9)],
  "line break":           ["Terno e gravata por R$ 35\n0, 99", Price(350, 99)],
  "html tags":            ["Geladeira Brastemp <b>super oferta: <u>R$ 799,99</u></b><br>", Price(799,99)],
  "numbers before price": ["Desconto 35%: Côtes du Rhone 2009 só R$15,90/garrafa", Price(15, 90)]}

class TestPrice(unittest.TestCase):
  pass

def test_generator(a, b):
  def test(self):
    self.assertEqual(a, b)
  return test

if __name__ == '__main__':
  for test_name in parsing_tests.keys():
    test_method_name = "test_" + test_name.replace(" ", "_")
    parsing_test =  test_generator(Price.parse(parsing_tests[test_name][0]), parsing_tests[test_name][1])
    parsing_test.__doc__ = "Testing parsing of string '%s'" % parsing_tests[test_name][0]
    setattr(TestPrice, test_method_name, parsing_test)
  unittest.main()
