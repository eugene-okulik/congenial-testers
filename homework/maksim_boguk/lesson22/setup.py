import sys

import requests
import unittest
from datetime import datetime


class TestPostAPI(unittest.TestCase):
    def get_current_data(self):
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
        self.assertEquals(response['title'], 'my tileUPD')


class TestAPInoSetUp(unittest.TestCase):
    @unittest.skip('Bug #42')
    def test_get_one(self):
        post_id = 42
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
        print(response['id'])
        self.assertEqual(response['id'], 42)

    @unittest.skipIf(sys.platform == 'linux', 'Not for linux' )
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
        self.assertEquals(response['title'], 'my tile')
