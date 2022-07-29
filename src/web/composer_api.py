import sys
import redis
from redis import Redis
from rq import Queue
from ..config import COMPOSER_NAME, COMPOSER_MODULE, REDIS_HOST, REDIS_PORT

q = Queue(COMPOSER_NAME, connection=Redis(REDIS_HOST, REDIS_PORT))

r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

up_vultargets = []  # sended task and confirmed up
upping_vultargets = []  # sended task but not confirmed up


def send_compose_up(vultarget):
    q.enqueue(f"{COMPOSER_MODULE}.compose_up", vultarget)
    upping_vultargets.append(vultarget)
    r.set('upping:' + vultarget, vultarget)
    return


def send_compose_down(vultarget):
    q.enqueue(f"{COMPOSER_MODULE}.compose_down", vultarget)
    return

def get_compose_status():
    outdata = {'upping':[], 'running':[]}
    for key in r.scan_iter("upping:*"):
        outdata['upping'].append(r.get(key).decode())
    for key in r.scan_iter("running:*"):
        outdata['running'].append(r.get(key).decode())
    return outdata

