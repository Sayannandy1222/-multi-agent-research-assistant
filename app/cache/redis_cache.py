import json

import redis

from app.config import REDIS_URL


class RedisCache:
    """
    Simple Redis cache wrapper.
    """

    def __init__(self):
        self.client = redis.Redis.from_url(
            REDIS_URL,
            decode_responses=True,
        )

    def get(self, key: str):
        value = self.client.get(key)

        if value is None:
            return None

        return json.loads(value)

    def set(self, key: str, value, expire: int = 3600):
        self.client.set(
            key,
            json.dumps(value),
            ex=expire,
        )

    def exists(self, key: str):
        return self.client.exists(key) == 1