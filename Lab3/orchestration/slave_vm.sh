#!/bin/sh

echo "This slave is alive!"

echo "Mounting the data..."
sudo mkdir /mnt/tweet_data
sudo mount /dev/vdb /mnt/tweet_data
sudo chown ubuntu:ubuntu /mnt/tweet_data

sudo apt-get update -y
sudo apt-get upgrade -y

echo "Installing pip..."
sudo apt-get install -y python3-pip
sudo -H pip3 install --upgrade pip

echo "Installing celery, flasp..."
sudo -H pip3 install celery==4.4 #celery needs to be lower than 5.0.0 for flower to work.
sudo -H pip3 install Flask

echo "Installing Tabea's code..."
cd /home/ubuntu
sudo git clone https://github.com/TabeaHaverkamp/ACC-Labs.git
cd /home/ubuntu/ACC-Labs/Lab3/
sudo git checkout concurrent

echo "Setting permission"
sudo chown -R ubuntu.users /home/ubuntu/ACC-Labs

echo "Connecting to the main rabbitmq node..."
sudo sed 's/localhost/MASTER_IP/' -i /home/ubuntu/ACC-Labs/Lab3/tasks.py

echo "Starting celery worker..."
cd /home/ubuntu/ACC-Labs/Lab3
sleep 5
sudo screen -S celeryserver -d -m bash -c 'cd /home/ubuntu/ACC-Labs/Lab3/ && celery -A tasks worker --loglevel=INFO -n worker1@%h --autoscale=10,3 --max-memory-per-child 100'
echo "started server"
echo "Initialization complete!"
