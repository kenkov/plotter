#! /usr/bin/env python
# coding:utf-8


import unittest
from plotter import Point
from plotter import Parser


class TestParser(unittest.TestCase):
    def test_parse(self):
        parser = Parser(" ")
        line = "100 1.2 1.4"
        self.assertEqual(parser.parse(line),
                         Point(x=100, ys=(1.2, 1.4)))

    def test_parse_separator_comma(self):
        parser = Parser(",")
        line = "100,1.2,1.4"
        self.assertEqual(parser.parse(line),
                         Point(x=100, ys=(1.2, 1.4)))
