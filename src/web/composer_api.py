import sys
import redis
from redis import Redis
from rq import Queue
from ..config import COMPOSER_NAME, COMPOSER_MODULE, REDIS_HOST, REDIS_PORT

q = Queue(COMPOSER_NAME, connection=Redis(REDIS_HOST, REDIS_PORT))

r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)


def send_compose_up(vultarget):
    if r.get("upping:" + vultarget) == None and r.get("running:" + vultarget) == None:
        q.enqueue(f"{COMPOSER_MODULE}.compose_up", vultarget)
        r.set("upping:" + vultarget, vultarget)
    return


def send_compose_down(vultarget):
    if r.get("stopping:" + vultarget) == None and r.get("running:" + vultarget) != None:
        q.enqueue(f"{COMPOSER_MODULE}.compose_down", vultarget)
        r.set("stopping:" + vultarget, vultarget)
    return


def get_compose_status():
    outdata = {"upping": [], "stopping": [], "running": []}
    for key in r.scan_iter("upping:*"):
        outdata["upping"].append(r.get(key).decode())
    for key in r.scan_iter("running:*"):
        outdata["running"].append(r.get(key).decode())
    for key in r.scan_iter("stopping:*"):
        outdata["stopping"].append(r.get(key).decode())
    return outdata


def send_connect_network(vulid):
    q.enqueue(f"{COMPOSER_MODULE}.connect_network", vulid)
    return


def send_disconnect_network(vulid):
    q.enqueue(f"{COMPOSER_MODULE}.disconnect_network", vulid)
    return
