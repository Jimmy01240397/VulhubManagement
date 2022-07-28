#!/bin/bash
cd /tmp

rm -r VulnhubManagement

git clone https://github.com/Jimmy01240397/VulnhubManagement

cd VulnhubManagement

systemd=$(ls systemd)

for a in $(ls -a)
do
    # some shell that didn't copy to configdir or some config
    if [ "$a" != "." ] && [ "$a" != ".." ] && [ "$a" != ".git" ] && [ "$a" != "README.md" ] && [ "$a" != "install.sh" ] && [ "$a" != "remove.sh" ] && [ "$a" != "setupgit.sh" ]
    then
        rm -rf $a
    fi
done

configdir=/etc/vulnhubmanagement

for a in $(ls -a $configdir)
do

    # some config that don't want to copy
    if [ "$a" != "." ] && [ "$a" != ".." ] && [ "$(cat $configdir/.gitignore | sed 's/\/.*//g' | sed '/^!.*/d' | grep -P "^$(echo "$a" | sed 's/\./\\\./g')$")" == "" ]
    then
        sudo cp -r $configdir/$a $a
    fi
done

for a in $systemd
do
    sudo cp /etc/systemd/system/$a $a
done
