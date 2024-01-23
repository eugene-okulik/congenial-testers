import unittest
import requests
import sys
from datetime import datetime


class TestPostAPI(unittest.TestCase):
    def get_current_date(self):
        return datetime.now()

    def setUp(self):
        payload = {
            "title": "My tile",
            "body": "my body",
            "userId": 1
        }
        headers = {
            'Content-type': 'application/json'
        }
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=payload,
            headers=headers
        ).json()
        self.post_id = response['id']

    def tearDown(self):
        requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')

    def test_put_a_post(self):
        payload = {
            "title": "My tileUPD",
            "body": "my bodyUPD",
            "userId": 2
        }
        headers = {
            'Content-type': 'application/json'
        }
        response = requests.put(
            f'https://jsonplaceholder.typicode.com/posts/{self.post_id}',
            json=payload,
            headers=headers
        ).json()
        self.assertEqual(response['title'], 'My tileUPD')


class TestPostAPINOsetUP(unittest.TestCase):
    @unittest.skip('Bug #42')
    def test_get_one(self):
        post_id = 43
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
        self.assertEqual(response['id'], post_id)

    @unittest.skipIf(sys.platform == 'linux', 'Not for linux')
    def test_post_a_post(self):
        payload = {
            "title": "My tile",
            "body": "my body",
            "userId": 1
        }
        headers = {
            'Content-type': 'application/json'
        }
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=payload,
            headers=headers
        ).json()
        self.assertEqual(response['title'], 'My tile')


'''
assertEqual(a, b) — a == b
assertNotEqual(a, b) — a != b
assertTrue(x) — bool(x) is True
assertFalse(x) — bool(x) is False
assertIs(a, b) — a is b
assertIsNot(a, b) — a is not b
assertIsNone(x) — x is None
assertIsNotNone(x) — x is not None
assertIn(a, b) — a in b
assertNotIn(a, b) — a not in b
assertIsInstance(a, b) — isinstance(a, b)
assertNotIsInstance(a, b) — not isinstance(a, b)
assertGreater(a, b) — a > b
assertGreaterEqual(a, b) — a >= b
assertLess(a, b) — a < b
assertLessEqual(a, b) — a <= b
'''
