from locust import task, HttpUser
import random


class PostsUser(HttpUser):
    post_id = None
    token = None

    def on_start(self):
        payload = {
            "title": "My tile",
            "body": "my body",
            "userId": 1
        }
        response = self.client.post('/posts', json=payload).json()
        self.post_id = response['id']
        response2 = self.client.post('/posts/authorize', json={"username": 'John', 'passw': 'skdjfhsdf'}).json()
        self.token = response2['token']

    @task(6)
    def get_one_post(self):
        self.client.get(f'/posts/{random.randrange(1, 101)}', headers={'Authorization': self.token})

    @task(1)
    def get_created_post(self):
        self.client.get(f'/posts/{random.choice([self.post_id, 42, 54, 76])}')
