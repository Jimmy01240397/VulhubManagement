import os


COMPOSER_NAME = os.environ.get("COMPOSER_NAME", "COMPOSER")
COMPOSER_HOST = os.environ.get("COMPOSER_HOST", "localhost")
COMPOSER_MODULE = os.environ.get("COMPOSER_MODULE", ".")


REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")

QUEUES = [COMPOSER_NAME]

VULS_ROOT = os.environ.get("VULS_ROOT", f"{__file__}/../../vulnerability")
