import os



COMPOSER_NAME = os.environ.get('COMPOSER_NAME', 'COMPOSER')
COMPOSER_HOST = os.environ.get('COMPOSER_HOST', 'localhost')

REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
REDIS_PORT = os.environ.get('REDIS_PORT', '6379')

QUEUES = [COMPOSER_NAME]