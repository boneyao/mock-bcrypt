# -*- coding:utf-8 -*-
import mock
import unittest
from passlib.hash import bcrypt
from mockbcrypt import plugin

from nose_parameterized import parameterized


class TestMockBcryptPlugin(unittest.TestCase):

    def setUp(self):
        super(TestMockBcryptPlugin, self).setUp()
        self.plugin = plugin.MockBcryptPlugin()
        self.plugin.enabled = True
        self.opts_mock = mock.MagicMock(name='opts')

    def test_options(self):
        parser = mock.MagicMock()
        self.plugin.options(parser)
        self.assertEquals(parser.add_option.call_count, 1)

    @parameterized.expand([
        ('1', '1'),
        ('A', 'A')
    ])
    def test_configure(self, pwd, pwd2):
        self.plugin.configure(self.opts_mock, None)

        assert bcrypt.encrypt(pwd) == pwd2

        assert bcrypt.verify(pwd, pwd2)
