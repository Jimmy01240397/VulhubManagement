from redis import Redis
from rq import Queue
from ..config import COMPOSER_NAME, REDIS_HOST, REDIS_PORT

q = Queue(COMPOSER_NAME, connection=Redis(REDIS_HOST, REDIS_PORT))


up_vultargets = [] # sended task and confirmed up
upping_vultargets = [] # sended task but not confirmed up 

def send_compose_up(vultarget):
  q.enqueue('internal.compose_up', vultarget)
  upping_vultargets.append(vultarget)
  return


def send_compose_down(vultarget):
  q.enqueue('internal.compose_down', vultarget)
  return



