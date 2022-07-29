import subprocess
import os
import redis
from ..config import VULS_ROOT, COMPOSER_NAME, COMPOSER_MODULE, REDIS_HOST, REDIS_PORT

r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

# if non exist return None
def get_context_path(vultarget) -> "str | None":
    context_path = os.path.normpath(f"{VULS_ROOT}/{vultarget}")
    return (
        context_path if os.path.exists(f"{context_path}/docker-compose.yml") else None
    )


# make it vulnerable ?
def compose_up(vultarget):
    context_path = get_context_path(vultarget)
    if context_path != None:
        completed = subprocess.run(
            f"cd {context_path} && docker-compose up -d", shell=True
        )
        if completed.returncode == 0:
            r.set("running:" + vultarget, vultarget)
        else:
            subprocess.run(f"cd {context_path} && docker-compose down", shell=True)
    r.delete("upping:" + vultarget)


def compose_down(vultarget):
    context_path = get_context_path(vultarget)
    if context_path != None:
        completed = subprocess.run(
            f"cd {context_path} && docker-compose down", shell=True
        )
        if completed.returncode == 0:
            r.delete("running:" + vultarget)
    r.delete("stopping:" + vultarget)


def connect_network(vulid: str):
    vulid = vulid.lower()
    networks = (
        subprocess.run(
            ["docker", "network", "ls", "--format='{{ .Name }}'"], capture_output=True
        )
        .stdout.decode()
        .replace("'", "")
        .split("\n")
    )  # > <
    name = f"{vulid}_default"
    if name not in networks:
        print(networks)
        print(f"{name} network not exist")
        return
    # vulnerable?
    completed = subprocess.run(["docker", "network", "connect", name, "vulhubShell"])
    return


def disconnect_network(vulid: str):
    vulid = vulid.lower()
    networks = (
        subprocess.run(
            ["docker", "network", "ls", "--format='{{ .Name }}'"], capture_output=True
        )
        .stdout.decode()
        .replace("'", "")
        .split("\n")
    )  # > <
    name = f"{vulid}_default"
    if name not in networks:
        print(networks)
        print(f"{name} network not exist")
        return
    # vulnerable?
    completed = subprocess.run(["docker", "network", "disconnect", name, "vulhubShell"])
    return


def is_running(vultarget):
    pass
