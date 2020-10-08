#!/bin/sh

echo "I'm alive!"

echo "Mounting the data..."
sudo mkdir /mnt/tweet_data
sudo mount /dev/vdb /mnt/tweet_data
sudo chown ubuntu:ubuntu /mnt/tweet_data

sudo apt-get update -y
sudo apt-get upgrade -y

echo "Installing pip..."
sudo apt-get install -y python3-pip
sudo -H pip3 install --upgrade pip

echo "Installing rabbitmq..."
sudo apt-get install -y rabbitmq-server
sudo service rabbitmq-server -detached

echo "Configuring rabbitmq..."
sudo rabbitmqctl add_user tabea tabeapassword
sudo rabbitmqctl add_vhost tabeavhost
#sudo rabbitmqctl set_user_tags milo_user milotweet
sudo rabbitmqctl set_permissions -p tabeavhost tabea ".*" ".*" ".*"

echo "Adding the SSH private key..."
echo "PRIVATE_KEY" > /home/ubuntu/.ssh/id_rsa
echo "PUBLIC KEY" > /home/ubuntu/.ssh/id_rsa.pub

echo "Installing celery..."
sudo -H pip3 install celery

echo "Installing flower..."
sudo -H pip3 install flower

echo "Installing flask..."
sudo -H pip install Flask


echo "Installing Tabea's code..."
cd /home/ubuntu
sudo git clone https://github.com/TabeaHaverkamp/ACC-Labs.git
cd /home/ubuntu/ACC-Labs/Lab3/
sudo git checkout concurrent

echo "Setting permission"
sudo chown -R ubuntu.users /home/ubuntu/ACC-Labs

echo "Starting flower..."
sudo screen -S celeryserver -d -m bash -c 'celery flower -A tasks --port=5000'

echo "Starting the celery server..."
sudo screen -S celeryserver -d -m bash -c 'cd /home/ubuntu/ACC-Labs/Lab3/ && celery -A tasks worker --loglevel=INFO -n worker1@%h --autoscale=10,3 --max-memory-per-child 100'

echo "start the app"
sudo screen -S celeryserver -d -m bash -c 'cd /home/ubuntu/ACC-Labs/Lab3/ && python3 flask_app.py'

echo "Initialization complete!"