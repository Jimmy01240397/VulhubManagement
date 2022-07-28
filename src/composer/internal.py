import subprocess
import os

# only check vulhub now
vuls_root = os.path.normpath(os.environ.get('vuls_root', f'{__filename__}/../../vulnerability')) 


# if non exist return None
def get_context_path(vultarget) -> str|None:
    context_path = os.path.normpath(f'{vuls_root}/{vultarget}/docker-compose.yml')    
    return context_path if os.path.exists(context_path) else None

# make it vulnerable ?
def compose_up(vultarget):
  context_path = get_context_path(vultarget)
  if context_path != None:
    completed = subprocess.run(["docker", "compose", "-f", context_path, "up", "-d"])
  if completed.returncode == 0:
    return 



def compose_down(vultarget):
  context_path = get_context_path(vultarget)
  if context_path != None:
    completed = subprocess.run(["docker", "compose", "-f", context_path, "up", "down"])
  if completed.returncode == 0:
    return 

def vultarget_is_running(vultarget):
  pass


