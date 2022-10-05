# -*- coding: utf-8 -*-

import unittest

from mydict import Dict

# 支持在命名行运行:  python -m unittest mydict_test.py
class TestDict(unittest.TestCase):

    # 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
    def setUp(self):
        print("set up")


    def tearDown(self):
        print("tear down")

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_key_error(self):
        d = Dict()
        # 通过d['empty']访问不存在的key时，断言会抛出KeyError：
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attr_error(self):
        d = Dict()
        # 通过d.empty访问不存在的key时，我们期待抛出AttributeError：
        with self.assertRaises(AttributeError):
            value = d.empty
