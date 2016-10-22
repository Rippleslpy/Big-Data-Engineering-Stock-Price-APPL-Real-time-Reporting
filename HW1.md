### Homework 1

- List existing docker-machine by
  ```
  docker-machine ls
  ```
  shows
  ```
  NAME      ACTIVE   DRIVER       STATE     URL   SWARM   DOCKER    ERRORS
  
  bigdata   -        virtualbox   Stopped                 Unknown
  ```
  
- Start the `bigdata` docker-machine by
  ```
  docker-machine start bigdata
  ```
  shows
  ```
  Starting "bigdata"...
  (bigdata) Check network to re-create if needed...
  (bigdata) Waiting for an IP...
  Machine "bigdata" was started.
  Waiting for SSH to be available...
  Detecting the provisioner...
  Started machines may have new IP addresses. You may need to re-run the `docker-machine env` command.
  ```

- Show the `bigdata` docker-machine ip address by
  ```
  docker-machine ip bigdata
  ```
  shows
  ```
  192.168.99.100
  ```

- Create an isolated environment for the `bigdata` docker-machine by
  ```
  eval $(docker-machine env bigdata)
  ```
  shows
  ```
  
  ```

- List all images in the `bigdata` docker-machine by
  ```
  docker images -a
  ```
  shows
  ```
  REPOSITORY            TAG                 IMAGE ID            CREATED             SIZE
  confluent/zookeeper   latest              4a1778ad1528        4 months ago        584.5 MB
  confluent/kafka       latest              2b9ba35e1775        4 months ago        584.5 MB
  ```

- List all containers in the `bigdata` docker-machine by
  ```
  docker ps -a
  ```
  shows
  ```
  CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS                  PORTS             NAMES
  524db896b63c        confluent/kafka       "/usr/local/bin/kafka"   3 days ago          Exited (0) 2 days ago                     kafka
  a66bee8c4bd1        confluent/zookeeper   "/usr/local/bin/zk-do"   3 days ago          Exited (0) 2 days ago                 zookeeper
  ```

- Check environments by
  - `scala --version` shows `Scala code runner version 2.11.8 -- Copyright 2002-2016, LAMP/EPFL`
  - `sbt sbtVersion` shows `[info] Set current project to yang (in build file:/Users/yang/)[info] 0.13.12`
  - `python --version` shows `Python 2.7.12`
  - `pip --version` shows `pip 8.1.2 from /usr/local/lib/python2.7/site-packages (python 2.7)`

- Start the existing `Zookeeper` and `Kafka` containers by
  ```
  docker start a66bee8c4bd1 524db896b63c
  ```
  shows
  ```
  a66bee8c4bd1
  524db896b63c
  ```

- List the current `docker-machine` information by
  
  `docker info`
  
  shows
  ```
  ontainers: 2
 Running: 2
 Paused: 0
 Stopped: 0
Images: 2
Server Version: 1.12.2
Storage Driver: aufs
 Root Dir: /mnt/sda1/var/lib/docker/aufs
 Backing Filesystem: extfs
 Dirs: 33
 Dirperm1 Supported: true
Logging Driver: json-file
Cgroup Driver: cgroupfs
Plugins:
 Volume: local
 Network: null bridge host overlay
Swarm: inactive
Runtimes: runc
Default Runtime: runc
Security Options: seccomp
Kernel Version: 4.4.24-boot2docker
Operating System: Boot2Docker 1.12.2 (TCL 7.2); HEAD : 9d8e41b - Tue Oct 11 23:40:08 UTC 2016
OSType: linux
Architecture: x86_64
CPUs: 2
Total Memory: 1.955 GiB
Name: bigdata
ID: H4M6:EIYG:VJ7A:FLV5:CZZN:VOQA:CBWT:C34E:4W5F:7M6C:SDR4:66JM
Docker Root Dir: /mnt/sda1/var/lib/docker
Debug Mode (client): false
Debug Mode (server): true
 File Descriptors: 22
 Goroutines: 36
 System Time: 2016-10-22T01:41:43.513176376Z
 EventsListeners: 0
Username: vincentdocker
Registry: https://index.docker.io/v1/
Labels:
 provider=virtualbox
Insecure Registries:
 127.0.0.0/8
 ```
