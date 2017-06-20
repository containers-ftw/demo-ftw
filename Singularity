BootStrap: docker
From: ubuntu:14.04

%files
generator.py generator.py

%runscript

     # This will print the scientific result!
     /usr/bin/python /generator.py

%post

     mkdir /data
     apt-get update && apt-get install -y python
     apt-get autoremove -y
     apt-get clean
