"""
单元测试代码
"""
import re

from django.test import TestCase

from common.utils import gen_mobile_code, to_md5_hex


class TestViewFunction(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_captcha(self):
        resp = self.client.get('/common/captcha/')
        self.assertEqual(200, resp.status_code)


class TestUtils(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_gen_mobile_code(self):
        pattern = re.compile(r'[0-9]{6}')
        for _ in range(1000):
            self.assertIsNotNone(pattern.match(gen_mobile_code()))
        pattern = re.compile(r'\d{4}')
        for _ in range(1000):
            self.assertIsNotNone(pattern.match(gen_mobile_code(length=4)))

    def test_to_md5_hex(self):
        pass_pairs = {
            '123456': 'e10adc3949ba59abbe56e057f20f883e',
            '123123': '4297f44b13955235245b2497399d7a93',
            '1qaz2wsx': '1c63129ae9db9c60c3e8aa94d3e00495',
        }
        for key, value in pass_pairs.items():
            self.assertEqual(value, to_md5_hex(key))
