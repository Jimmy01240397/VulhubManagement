# VulhubManagement

Vulhub Management service

- [Install](#Install)
- [Remove](#Remove)
- [Make a git dir for this repo at installed host](#make-a-git-dir-for-this-repo-at-installed-host)

## Install

1. Clone this repo and cd into VulhubManagement.

```bash
git clone https://github.com/Jimmy01240397/VulhubManagement
cd VulhubManagement
```

2. Run `install.sh`

```bash
sh install.sh
```

3. And you can run service with `systemctl start vulhubmanagement.service`

## Remove

1. clone this repo and cd into VulhubManagement than run remove.sh

```bash
git clone https://github.com/Jimmy01240397/VulhubManagement
cd VulhubManagement
sh remove.sh
```

## Make a git dir for this repo at installed host

1. clone this repo and cd into VulhubManagement.

```bash
git clone https://github.com/Jimmy01240397/VulhubManagement
cd VulhubManagement
```

2. Run setupgit.sh

```bash
bash setupgit.sh
```

3. cd into `/tmp/VulhubManagement`

```bash
cd /tmp/VulhubManagement
```

4. and you can run `git status` and `git diff` to see what you change in `/etc/vulhubmanagement/`

```bash
$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

## For Developer Only

### Run the Development environment

1. Install `docker`

2. Run `docker compose -f docker-compose-dev.yml up`

3. If success, you should see the page `http://127.0.0.1:5000/hello`
