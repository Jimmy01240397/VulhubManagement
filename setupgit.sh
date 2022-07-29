#!/bin/bash
cd /tmp

rm -r VulhubManagement

git clone https://github.com/Jimmy01240397/VulhubManagement

cd VulhubManagement

git submodule update --init --recursive

systemd=$(ls systemd)

for a in $(ls -a)
do
    # some shell that didn't copy to configdir or some config
    if [ "$a" != "." ] && [ "$a" != ".." ] && [ "$a" != ".git" ] && [ "$a" != ".gitmodules" ] && [ "$a" != "README.md" ] && [ "$a" != "LICENSE" ] && [ "$a" != "install.sh" ] && [ "$a" != "remove.sh" ] && [ "$a" != "setupgit.sh" ]
    then
        rm -rf $a
    fi
done

configdir=/etc/vulhubmanagement

for a in $(ls -a $configdir)
do

    # some config that don't want to copy
    if [ "$a" != "." ] && [ "$a" != ".." ] && [ "$(cat $configdir/.gitignore | sed 's/\/.*//g' | sed '/^!.*/d' | grep -P "^$(echo "$a" | sed 's/\./\\\./g')$")" == "" ]
    then
        sudo cp -r $configdir/$a $a
    fi
done

mkdir systemd

for a in $systemd
do
    sudo cp /etc/systemd/system/$a systemd/$a
done
