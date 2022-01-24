#!/bin/bash

yum -y update
yum -y install git
git clone https://github.com/Hawk-Eye-2021/sentiment-extractor.git
cd sentiment-extractor

# add swap
dd if=/dev/zero of=/var/swap.1 bs=1M count=8192
chmod 600 /var/swap.1
mkswap /var/swap.1
swapon /var/swap.1


pip3 install -r requirements.txt --no-cache-dir

python3 api.py