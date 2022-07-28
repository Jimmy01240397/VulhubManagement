#!/bin/bash

sudo systemctl stop vulhubmanagement.service
sudo systemctl disable vulhubmanagement.service

for a in $(ls systemd)
sudo rm /etc/systemd/system/$a.service

configdir=/etc/vulhubmanagement

# something need to delete
for filename in __pycache__ requirements.txt venv .gitignore vulhubmanagement.sh vulnerability
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
echo "Vulhub Management Service remove.sh complete."

for filename in server.key server.crt
do
	echo "Your ${filename} is at $(pwd)/${filename}."
done

echo "If you don't need then, please delete then."
