%bash

# simple VM set-up
gcloud beta compute --project=psychic-empire-247615 instances create datalab-vm --zone=europe-west1-b --machine-type=n1-standard-1 --subnet=default --network-tier=PREMIUM --maintenance-policy=MIGRATE --service-account=446608842394-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/cloud-platform --image=debian-9-stretch-v20190813 --image-project=debian-cloud --boot-disk-size=10GB --boot-disk-type=pd-standard --boot-disk-device-name=datalab-vm --reservation-affinity=any

# get VM informations
cat /proc/cpuinfo

# importing git and git repo

sudo apt-get -y -qq install git
git --version #checking git version

git clone <XXXXX> #cloning github repository

# getting necessary python packages

#!/bin/bash
sudo apt-get update
sudo apt-get -y -qq --fix-missing install python3-mpltoolkits.basemap python3-numpy python3-matplotlib python3-requests

### HOW TO :
# bash <XXX>.sh #run a bash file called <XXX>
