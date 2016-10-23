# Homework 1

### Set up Zookeeper and Kafka environment on docker-machine
-----

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

### Operations on Zookeeper
-----

- Locate to the `bin` directory of Zookeeper by
  ```
  cd Documents/Zookeeper/zookeeper-3.4.8/bin
  ```
  
- Connect with the Zookeeper on the docker-machine by
  ```
  ./zkCli.sh -server `docker-machine ip bigdata`:2181
  ```
  shows
  ```
  onnecting to 192.168.99.100:2181
2016-10-23 16:20:07,279 [myid:] - INFO  [main:Environment@100] - Client environment:zookeeper.version=3.4.8--1, built on 02/06/2016 03:18 GMT
2016-10-23 16:20:07,286 [myid:] - INFO  [main:Environment@100] - Client environment:host.name=yangs-mbp-3.home
2016-10-23 16:20:07,287 [myid:] - INFO  [main:Environment@100] - Client environment:java.version=1.8.0_45
2016-10-23 16:20:07,290 [myid:] - INFO  [main:Environment@100] - Client environment:java.vendor=Oracle Corporation
2016-10-23 16:20:07,290 [myid:] - INFO  [main:Environment@100] - Client environment:java.home=/Library/Java/JavaVirtualMachines/jdk1.8.0_45.jdk/Contents/Home/jre
2016-10-23 16:20:07,291 [myid:] - INFO  [main:Environment@100] - Client environment:java.class.path=/Users/yang/Documents/Zookeeper/zookeeper-3.4.8/bin/../build/classes:/Users/yang/Documents/Zookeeper/zookeeper-3.4.8/bin/../build/lib/*.jar:/Users/yang/Documents/Zookeeper/zookeeper-3.4.8/bin/../lib/slf4j-log4j12-1.6.1.jar:/Users/yang/Documents/Zookeeper/zookeeper-3.4.8/bin/../lib/slf4j-api-1.6.1.jar:/Users/yang/Documents/Zookeeper/zookeeper-3.4.8/bin/../lib/netty-3.7.0.Final.jar:/Users/yang/Documents/Zookeeper/zookeeper-3.4.8/bin/../lib/log4j-1.2.16.jar:/Users/yang/Documents/Zookeeper/zookeeper-3.4.8/bin/../lib/jline-0.9.94.jar:/Users/yang/Documents/Zookeeper/zookeeper-3.4.8/bin/../zookeeper-3.4.8.jar:/Users/yang/Documents/Zookeeper/zookeeper-3.4.8/bin/../src/java/lib/*.jar:/Users/yang/Documents/Zookeeper/zookeeper-3.4.8/bin/../conf:
2016-10-23 16:20:07,291 [myid:] - INFO  [main:Environment@100] - Client environment:java.library.path=/Users/yang/Library/Java/Extensions:/Library/Java/Extensions:/Network/Library/Java/Extensions:/System/Library/Java/Extensions:/usr/lib/java:.
2016-10-23 16:20:07,291 [myid:] - INFO  [main:Environment@100] - Client environment:java.io.tmpdir=/var/folders/8v/9_5lvzpd7vsfmvpq89vds7b80000gn/T/
2016-10-23 16:20:07,291 [myid:] - INFO  [main:Environment@100] - Client environment:java.compiler=<NA>
2016-10-23 16:20:07,291 [myid:] - INFO  [main:Environment@100] - Client environment:os.name=Mac OS X
2016-10-23 16:20:07,291 [myid:] - INFO  [main:Environment@100] - Client environment:os.arch=x86_64
2016-10-23 16:20:07,291 [myid:] - INFO  [main:Environment@100] - Client environment:os.version=10.11.6
2016-10-23 16:20:07,291 [myid:] - INFO  [main:Environment@100] - Client environment:user.name=yang
2016-10-23 16:20:07,292 [myid:] - INFO  [main:Environment@100] - Client environment:user.home=/Users/yang
2016-10-23 16:20:07,292 [myid:] - INFO  [main:Environment@100] - Client environment:user.dir=/Users/yang/Documents/Zookeeper/zookeeper-3.4.8/bin
2016-10-23 16:20:07,293 [myid:] - INFO  [main:ZooKeeper@438] - Initiating client connection, connectString=192.168.99.100:2181 sessionTimeout=30000 watcher=org.apache.zookeeper.ZooKeeperMain$MyWatcher@69d0a921
Welcome to ZooKeeper!
2016-10-23 16:20:07,362 [myid:] - INFO  [main-SendThread(192.168.99.100:2181):ClientCnxn$SendThread@1032] - Opening socket connection to server 192.168.99.100/192.168.99.100:2181. Will not attempt to authenticate using SASL (unknown error)
JLine support is enabled
2016-10-23 16:20:07,484 [myid:] - INFO  [main-SendThread(192.168.99.100:2181):ClientCnxn$SendThread@876] - Socket connection established to 192.168.99.100/192.168.99.100:2181, initiating session
2016-10-23 16:20:07,499 [myid:] - INFO  [main-SendThread(192.168.99.100:2181):ClientCnxn$SendThread@1299] - Session establishment complete on server 192.168.99.100/192.168.99.100:2181, sessionid = 0x157ea0c38cd0006, negotiated timeout = 30000

WATCHER::

WatchedEvent state:SyncConnected type:None path:null
[zk: 192.168.99.100:2181(CONNECTED) 0]
```

- Check contains by `ls /`
  shows
  ```
  controller_epoch, controller, brokers, zookeeper, admin, isr_change_notification, consumers, config]
  ```
  use `ls /zookeeper` shows
  ```
  [quota]
  ```
  use `get /zookeeper/quota` shows
  ```
  cZxid = 0x0
  ctime = Wed Dec 31 19:00:00 EST 1969
  mZxid = 0x0
  mtime = Wed Dec 31 19:00:00 EST 1969
  pZxid = 0x0
  cversion = 0
  dataVersion = 0
  aclVersion = 0
  ephemeralOwner = 0x0
  dataLength = 0
  numChildren = 0
  ```

- Create Znode Data by `create /workers "bittiger"` shows
  ```
  created /workers
  ```
  use `ls /` shows
  ```
  controller_epoch, controller, brokers, zookeeper, admin, isr_change_notification, consumers, config, workers]
  ```
  use `ls /workers` shows
  ```
  []
  ```
  use `get /workers` shows
  ```
  bittiger
cZxid = 0x2c6
ctime = Sun Oct 23 16:37:47 EDT 2016
mZxid = 0x2c6
mtime = Sun Oct 23 16:37:47 EDT 2016
pZxid = 0x2c6
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 8
numChildren = 0
  ```

- Delete Znode Data by `delete /workers` shows
  ```
  ```
  use `ls /` shows
  ```
  [controller_epoch, controller, brokers, zookeeper, admin, isr_change_notification, consumers, config]
  ```
  use `ls /workers` shows
  ```
  Node does not exist: /workers
  ```
  use `get /workers` shows
  ```
  Node does not exist: /workers
  ```

- Create Ephemeral Znode Data by `create -e /workers "yangcareers"` shows
  ```
  Created /workers
  ```
  use `ls /` shows
  ```
  [controller_epoch, controller, brokers, zookeeper, admin, isr_change_notification, consumers, config, work
  ```
  use `ls /workers` shows
  ```
  []
  ```
  use `get /workers` shows
  ```
  yangcareers
cZxid = 0x2c8
ctime = Sun Oct 23 16:44:55 EDT 2016
mZxid = 0x2c8
mtime = Sun Oct 23 16:44:55 EDT 2016
pZxid = 0x2c8
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x157ea0c38cd0006
dataLength = 11
numChildren = 0
  ```

- Set up Watcher by `get /workers true` shows
  ```
  yangcareers
cZxid = 0x2c8
ctime = Sun Oct 23 16:44:55 EDT 2016
mZxid = 0x2c8
mtime = Sun Oct 23 16:44:55 EDT 2016
pZxid = 0x2c8
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x157ea0c38cd0006
dataLength = 11
numChildren = 0
  ```

- Quit zookeeper by `quit` shows
  ```
  Quitting...

WATCHER::

WatchedEvent state:SyncConnected type:NodeDeleted path:/workers
2016-10-23 16:52:30,651 [myid:] - INFO  [main:ZooKeeper@684] - Session: 0x157ea0c38cd0006 closed
2016-10-23 16:52:30,653 [myid:] - INFO  [main-EventThread:ClientCnxn$EventThread@519] - EventThread shut down for session: 0x157ea0c38cd0006
  ```

### Operations on Kafka
-----

- Locate to the `bin` directory of Kafka by
  ```
  cd Documents/Kafka/kafka_2.11-0.10.0.1/bin
  ```
  
- Create a topic called `bigdata2` by
  ```
  ./kafka-topics.sh --create --zookeeper `docker-machine ip bigdata` --replication-factor 1 --partitions 1 --topic bigdata2
  ```
  shows
  ```
  Created topic "bigdata2".
  ```
  check topics by
  ```
  ./kafka-topics.sh --list --zookeeper `docker-machine ip bigdata`
  ```
  shows
  ```
  __consumer_offsets
bigdata
bigdata2
stock-analyzer
  ```

- Check topics on Zookeeper by
  ```
  ./zkCli.sh -server `docker-machine ip bigdata`:2181
  ```
  use `ls /` shows
  ```
  [controller_epoch, controller, brokers, zookeeper, admin, isr_change_notification, consumers, config]
  ```

- Create a topic called `bigdata` on Kafka by
  ```
  ./kafka-console-producer.sh --broker-list `docker-machine ip bigdata`:9092 --topic bigdata
  ```
  and the terminal is ready to take messages. Type the following message
  ```
  This is the 1st test message.
  ```

- Consumer the `bigdata` topic by
  ```
  ./kafka-console-consumer.sh --zookeeper `docker-machine ip bigdata`:2181 --topic bigdata
  ```
  shows
  ```
  This is the 1st message.
  ```

- Consumer the `bigdata` topic from the beginning by
  ```
  ./kafka-console-consumer.sh --zookeeper `docker-machine ip bigdata`:2181 --topic bigdata --from-beginning
  ```
  and type
  ```
  This is the 2nd message.
  ```
  in the topic terminal. The consumer terminal shows
  ```
  This is the 1st test message.
This is the 2nd test message.
  ```

- Look into Kafka broker by
  ```
  docker exec -it kafka bash
  ```
  shows
  ```
  confluent@524db896b63c:
  ```
  use `cd /var/lib/kafka/ ls` and `ls` shows
  ```
  __consumer_offsets-0   __consumer_offsets-22  __consumer_offsets-36  __consumer_offsets-5
__consumer_offsets-1   __consumer_offsets-23  __consumer_offsets-37  __consumer_offsets-6
__consumer_offsets-10  __consumer_offsets-24  __consumer_offsets-38  __consumer_offsets-7
__consumer_offsets-11  __consumer_offsets-25  __consumer_offsets-39  __consumer_offsets-8
__consumer_offsets-12  __consumer_offsets-26  __consumer_offsets-4   __consumer_offsets-9
__consumer_offsets-13  __consumer_offsets-27  __consumer_offsets-40  bigdata-0
__consumer_offsets-14  __consumer_offsets-28  __consumer_offsets-41  bigdata2-0
__consumer_offsets-15  __consumer_offsets-29  __consumer_offsets-42  cleaner-offset-checkpoint
__consumer_offsets-16  __consumer_offsets-3   __consumer_offsets-43  meta.properties
__consumer_offsets-17  __consumer_offsets-30  __consumer_offsets-44  recovery-point-offset-checkpoint
__consumer_offsets-18  __consumer_offsets-31  __consumer_offsets-45  replication-offset-checkpoint
__consumer_offsets-19  __consumer_offsets-32  __consumer_offsets-46  stock-analyzer-0
__consumer_offsets-2   __consumer_offsets-33  __consumer_offsets-47
__consumer_offsets-20  __consumer_offsets-34  __consumer_offsets-48
__consumer_offsets-21  __consumer_offsets-35  __consumer_offsets-49
  ```
