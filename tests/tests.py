# coding: utf-8

import unittest
from app import app


class TestsCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_get(self):
        response = self.client.get("/resource/")

        self.assertEqual(response.status_code, 200)