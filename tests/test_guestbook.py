# -*- coding: utf-8 -*-
import unittest
import guestbook


class TestGuestbookApp(unittest.TestCase):

    def setUp(self):
        self.application = guestbook.application.test_client()

    def test_index(self):
        response = self.application.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('ゲストブック' in response.data)
