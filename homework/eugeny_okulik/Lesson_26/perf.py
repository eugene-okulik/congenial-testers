import requests
from datetime import datetime

elapsed = []
for _ in range(5):
    start = datetime.now()
    requests.get('https://jsonplaceholder.typicode.com/posts/1')
    end = datetime.now()
    elapsed.append((end - start).microseconds)

print(elapsed)
