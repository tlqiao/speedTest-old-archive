import json
import redis
from configs.load_config import get_configs

def get_redis_connection():
    configs = get_configs()["redisdb"]
    connection = redis.Redis(**configs)
    return connection

def get_data(key):
    connection = get_redis_connection()
    data = connection.get(key)
    return data

def set_data(key, value):
    connection = get_redis_connection()
    connection.set(key, value)

def delete_data(key):
    connection = get_redis_connection()
    connection.delete(key)

    