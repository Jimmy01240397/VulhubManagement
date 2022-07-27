#!/bin/bash

sudo systemctl stop vulnhubmanagement.service
sudo systemctl disable vulnhubmanagement.service

for a in $(ls systemd)
sudo rm /etc/systemd/system/$a.service

configdir=/etc/vulnhubmanagement

# something need to delete
for filename in __pycache__ requirements.txt venv .gitignore
do
	sudo rm -r $configdir/$filename
done

sudo mv $configdir/server.key .
sudo mv $configdir/server.crt .

if [ "$(ls $configdir)" = "" ]
then
	rm -r $configdir
fi

echo ""
echo ""
echo "Vulnhub Management Service remove.sh complete."

for filename in server.key server.crt
do
	echo "Your ${filename} is at $(pwd)/${filename}."
done

echo "If you don't need then, please delete then."
