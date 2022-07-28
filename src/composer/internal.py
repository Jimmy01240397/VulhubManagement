import subprocess
import os
from ..config import VULS_ROOT

# if non exist return None
def get_context_path(vultarget) -> 'str | None':
    context_path = os.path.normpath(f'{VULS_ROOT}/{vultarget}')    
    return context_path if os.path.exists(f'{context_path}/docker-compose.yml') else None

# make it vulnerable ?
def compose_up(vultarget):
  context_path = get_context_path(vultarget)
  if context_path != None:
    completed = subprocess.run(f"cd {context_path} && docker-compose up -d", shell=True)
    if completed.returncode == 0:
      return 



def compose_down(vultarget):
  context_path = get_context_path(vultarget)
  if context_path != None:
    completed = subprocess.run(f"cd {context_path} && docker-compose down", shell=True)
    if completed.returncode == 0:
      return 
      

def is_running(vultarget):
  pass


