
# Dependencies
> $ scala -version
```
Scala code runner version 2.11.8 -- Copyright 2002-2016, LAMP/EPFL
```
> $ sbt sbtVersion
```
Java HotSpot(TM) 64-Bit Server VM warning: ignoring option MaxPermSize=256m; support was removed in 8.0
[info] Set current project to xb (in build file:/C:/Users/xb/)
[info] 0.13.12
```
> $ python --version
```
Python 2.7.10
```
> $ pip --version
```
pip 8.1.2 from c:\python27\lib\site-packages (python 2.7)
```

----------

# Work with Zookeeper
### Start Zookeeper Server
> $ docker run -d -p 2181:2181 -p 2888:2888 -p 3888:3888 --name zookeeper confluent/zookeeper
> <br/> ``首次执行时：``
```
Unable to find image 'confluent/zookeeper:latest' locally
latest: Pulling from confluent/zookeeper
51f5c6a04d83: Pull complete
a3ed95caeb02: Pull complete
7004cfc6e122: Pull complete
aee1f2b2873f: Pull complete
3a68342c4011: Pull complete
6cbd71d4d1f4: Pull complete
a26b1ce3360b: Pull complete
55bdb2de3391: Pull complete
c14c55acf45f: Pull complete
be7e9723819a: Pull complete
ff3558a8d162: Pull complete
c73633913e48: Pull complete
abf0c05f5209: Pull complete
8e0153a3fe95: Pull complete
8476a7f4c120: Pull complete
dd7b7029d4f9: Pull complete
5de42c73a24d: Pull complete
82153f3e2e3f: Pull complete
1b403d9fce92: Pull complete
b5c575c9edb6: Pull complete
Digest: sha256:bb097bce322f5553ed1511234f97e7eedb0900211c46958357fbcb342917cbf8
Status: Downloaded newer image for confluent/zookeeper:latest
b25ff1e39f749b60827da47968c8a43c3343943f871d5e1a63eb489aed09c501
```
> ``再次执行时：``
```
74f2770cd5e66178dfe1598d37aeb2624f4e2a483b42a54bd9fef710e8250314
```
> $docker images
```
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
hello-world             latest              c54a2cc56cbb        3 months ago        1.848 kB
confluent/zookeeper     latest              4a1778ad1528        4 months ago        584.5 MB
confluent/kafka         latest              2b9ba35e1775        4 months ago        584.5 MB
unclebarney/chit-chat   latest              639e46d7a14a        8 months ago        31.86 MB
```
> $ docker ps
```
CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                                                                    NAMES
74f2770cd5e6        confluent/zookeeper   "/usr/local/bin/zk-do"   2 minutes ago       Up 2 minutes        0.0.0.0:2181->2181/tcp, 0.0.0.0:2888->2888/tcp, 0.0.0.0:3888->3888/tcp   zookeeper
```

### Start Zookeeper CLI
> $ cd zookeeper-3.4.9/bin
> $ ./zkCli.sh -server  \`docker-machine ip bigdata`:2181
```
Connecting to 192.168.99.100:2181
2016-10-19 17:16:10,273 [myid:] - INFO  [main:Environment@100] - Client environment:zookeeper.version=3.4.9-1757313, built on 08/23/2016 06:50 GMT
2016-10-19 17:16:10,276 [myid:] - INFO  [main:Environment@100] - Client environment:host.name=ACHILLES
2016-10-19 17:16:10,276 [myid:] - INFO  [main:Environment@100] - Client environment:java.version=1.8.0_102
2016-10-19 17:16:10,277 [myid:] - INFO  [main:Environment@100] - Client environment:java.vendor=Oracle Corporation
2016-10-19 17:16:10,278 [myid:] - INFO  [main:Environment@100] - Client environment:java.home=C:\Program Files\Java\jdk1.8.0_102\jre
2016-10-19 17:16:10,278 [myid:] - INFO  [main:Environment@100] - Client environment:java.class.path=E:\DevelopmentKit\zookeeper-3.4.9\build\classes;E:\DevelopmentKit\zookeeper-3.4.9\build\lib\*.jar;E:\DevelopmentKit\zookeeper-3.4.9\lib\slf4j-log4j12-1.6.1.jar;E:\DevelopmentKit\zookeeper-3.4.9\lib\slf4j-api-1.6.1.jar;E:\DevelopmentKit\zookeeper-3.4.9\lib\netty-3.10.5.Final.jar;E:\DevelopmentKit\zookeeper-3.4.9\lib\log4j-1.2.16.jar;E:\DevelopmentKit\zookeeper-3.4.9\lib\jline-0.9.94.jar;E:\DevelopmentKit\zookeeper-3.4.9\zookeeper-3.4.9.jar;E:\DevelopmentKit\zookeeper-3.4.9\src\java\lib\*.jar;E:\DevelopmentKit\zookeeper-3.4.9\conf;.
2016-10-19 17:16:10,279 [myid:] - INFO  [main:Environment@100] - Client environment:java.library.path=C:\Program Files\Java\jdk1.8.0_102\bin;C:\WINDOWS\Sun\Java\bin;C:\WINDOWS\system32;C:\WINDOWS;C:\Python27;C:\Python27\Scripts;C:\ProgramData\Oracle\Java\javapath;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0;C:\Program Files\Java\jdk1.8.0_102\bin;D:\apache-maven-3.3.9\bin;C:\Program Files\Git\cmd;C:\Program Files (x86)\scala\bin;C:\Program Files (x86)\sbt\bin;C:\cygwin64\bin;C:\Users\xb\AppData\Local\Microsoft\WindowsApps;C:\Program Files\Docker Toolbox;.
2016-10-19 17:16:10,280 [myid:] - INFO  [main:Environment@100] - Client environment:java.io.tmpdir=C:\Users\xb\AppData\Local\Temp\
2016-10-19 17:16:10,280 [myid:] - INFO  [main:Environment@100] - Client environment:java.compiler=<NA>
2016-10-19 17:16:10,280 [myid:] - INFO  [main:Environment@100] - Client environment:os.name=Windows 10
2016-10-19 17:16:10,281 [myid:] - INFO  [main:Environment@100] - Client environment:os.arch=amd64
2016-10-19 17:16:10,281 [myid:] - INFO  [main:Environment@100] - Client environment:os.version=10.0
2016-10-19 17:16:10,282 [myid:] - INFO  [main:Environment@100] - Client environment:user.name=xb
2016-10-19 17:16:10,282 [myid:] - INFO  [main:Environment@100] - Client environment:user.home=C:\Users\xb
2016-10-19 17:16:10,283 [myid:] - INFO  [main:Environment@100] - Client environment:user.dir=E:\DevelopmentKit\zookeeper-3.4.9\bin
2016-10-19 17:16:10,284 [myid:] - INFO  [main:ZooKeeper@438] - Initiating client connection, connectString=192.168.99.100:2181 sessionTimeout=30000 watcher=org.apache.zookeeper.ZooKeeperMain$MyWatcher@277050dc
Welcome to ZooKeeper!
2016-10-19 17:16:10,503 [myid:] - INFO  [main-SendThread(192.168.99.100:2181):ClientCnxn$SendThread@1032] - Opening socket connection to server 192.168.99.100/192.168.99.100:2181. Will not attempt to authenticate using SASL (unknown error)
2016-10-19 17:16:10,504 [myid:] - INFO  [main-SendThread(192.168.99.100:2181):ClientCnxn$SendThread@876] - Socket connection established to 192.168.99.100/192.168.99.100:2181, initiating session
JLine support is enabled
[zk: 192.168.99.100:2181(CONNECTING) 0] 2016-10-19 17:16:10,551 [myid:] - INFO  [main-SendThread(192.168.99.100:2181):ClientCnxn$SendThread@1299] - Session establishment complete on server 192.168.99.100/192.168.99.100:2181, sessionid = 0x157dc2a71b60000, negotiated timeout = 30000
>
WATCHER::
>
WatchedEvent state:SyncConnected type:None path:null
```

### Browse Znode Data
> [zk: 192.168.99.100:2181(CONNECTED) 0] ls /
```
[zookeeper]
```
> [zk: 192.168.99.100:2181(CONNECTED) 1] ls /zookeeper
```
[quota]
```
> [zk: 192.168.99.100:2181(CONNECTED) 2] get /zookeeper/quota
```
cZxid = 0x0
ctime = Thu Jan 01 08:00:00 CST 1970
mZxid = 0x0
mtime = Thu Jan 01 08:00:00 CST 1970
pZxid = 0x0
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 0
numChildren = 0
```

### Create Znode Data
> [zk: 192.168.99.100:2181(CONNECTED) 3] create /workers "bittiger"
```
Created /workers
```
> [zk: 192.168.99.100:2181(CONNECTED) 4] ls /
```
[zookeeper, workers]
```
> [zk: 192.168.99.100:2181(CONNECTED) 5] ls /workers
```
[]
```
> [zk: 192.168.99.100:2181(CONNECTED) 6] get /workers
```
bittiger
cZxid = 0x2
ctime = Wed Oct 19 17:20:02 CST 2016
mZxid = 0x2
mtime = Wed Oct 19 17:20:02 CST 2016
pZxid = 0x2
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 8
numChildren = 0
```

### Delete Znode Data
> [zk: 192.168.99.100:2181(CONNECTED) 7] delete /workers
> <br/> [zk: 192.168.99.100:2181(CONNECTED) 8] ls /
```
[zookeeper]
```
> [zk: 192.168.99.100:2181(CONNECTED) 9] ls /workers
```
Node does not exist: /workers
```
> [zk: 192.168.99.100:2181(CONNECTED) 10] get /workers
```
Node does not exist: /workers
```

### Create Ephemeral Znode Data
> [zk: 192.168.99.100:2181(CONNECTED) 11] create -e /workers "unclebarney"
```
Created /workers
```
> [zk: 192.168.99.100:2181(CONNECTED) 12] ls /
```
[zookeeper, workers]
```
> [zk: 192.168.99.100:2181(CONNECTED) 13] ls /workers
```
[]
```
> [zk: 192.168.99.100:2181(CONNECTED) 14] get /workers
```
unclebarney
cZxid = 0x4
ctime = Wed Oct 19 17:23:03 CST 2016
mZxid = 0x4
mtime = Wed Oct 19 17:23:03 CST 2016
pZxid = 0x4
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x157dc2a71b60000
dataLength = 11
numChildren = 0
```

### Set Watcher
> [zk: 192.168.99.100:2181(CONNECTED) 15] get /workers true
```
unclebarney
cZxid = 0x4
ctime = Wed Oct 19 17:23:03 CST 2016
mZxid = 0x4
mtime = Wed Oct 19 17:23:03 CST 2016
pZxid = 0x4
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x157dc2a71b60000
dataLength = 11
numChildren = 0
```
> [zk: 192.168.99.100:2181(CONNECTED) 19] quit
```
Quitting...
>
WATCHER::
2016-10-19 17:28:10,710 [myid:] - INFO  [main:ZooKeeper@684] - Session: 0x157dc2a71b60000 closed
>
WatchedEvent state:SyncConnected type:NodeDeleted path:/workers
```


----------

# Work with Kafka
### Start kafka Server
> $ docker run -d -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=\`docker-machine ip bigdata\` -e KAFKA_ADVERTISED_PORT=9092 --name kafka --link zookeeper:zookeeper confluent/kafka
> <br/> ``首次执行时：``
```
Unable to find image 'confluent/kafka:latest' locally
latest: Pulling from confluent/kafka
51f5c6a04d83: Already exists
a3ed95caeb02: Already exists
7004cfc6e122: Already exists
aee1f2b2873f: Already exists
3a68342c4011: Already exists
6cbd71d4d1f4: Already exists
a26b1ce3360b: Already exists
55bdb2de3391: Already exists
c14c55acf45f: Already exists
be7e9723819a: Already exists
ff3558a8d162: Already exists
c73633913e48: Already exists
abf0c05f5209: Already exists
8e0153a3fe95: Already exists
8476a7f4c120: Already exists
ed5d8f66195d: Pull complete
a13270395e60: Pull complete
c8661c1d28fc: Pull complete
13f86b2644be: Pull complete
Digest: sha256:de7415d87302269211342bfe6f7b15fe25f157b55970b2307f325d09e173d357
Status: Downloaded newer image for confluent/kafka:latest
358c0e2343d733788f3a07ea0ac6d03bc384185449034c77a2dc4c862de84c27
```
> ``再次执行时：``
```
f22de4ef65b1fa3fe47b650d21109e21e70b6a2837929d7330a3b362ffa7013d
```
> $ docker images
```
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
hello-world             latest              c54a2cc56cbb        3 months ago        1.848 kB
confluent/zookeeper     latest              4a1778ad1528        4 months ago        584.5 MB
confluent/kafka         latest              2b9ba35e1775        4 months ago        584.5 MB
unclebarney/chit-chat   latest              639e46d7a14a        8 months ago        31.86 MB
```
> $ docker ps
```
CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                                                                    NAMES
f22de4ef65b1        confluent/kafka       "/usr/local/bin/kafka"   12 seconds ago      Up 12 seconds       0.0.0.0:9092->9092/tcp                                                   kafka
74f2770cd5e6        confluent/zookeeper   "/usr/local/bin/zk-do"   44 minutes ago      Up 44 minutes       0.0.0.0:2181->2181/tcp, 0.0.0.0:2888->2888/tcp, 0.0.0.0:3888->3888/tcp   zookeeper
```

### Create Kafka Topic
> $ ./kafka-topics.sh --create --zookeeper \`docker-machine ip bigdata` --replication-factor 1 --partitions 1 --topic bigdata
```
Created topic "bigdata".
```
> $ ./kafka-topics.sh --list --zookeeper \`docker-machine ip bigdata`
```
bigdata
```

### Look up on Zookeeper
> $ ./zkCli.sh -server \`docker-machine ip bigdata`:2181
> <br/> [zk: 192.168.99.100:2181(CONNECTED) 0] ls /
```
[controller, controller_epoch, brokers, zookeeper, admin, isr_change_notification, consumers, config]
```

### Produce Messages
> $ ./kafka-console-producer.sh --broker-list \`docker-machine ip bigdata\`:9092 --topic bigdata
> <br> ``以下是输入的内容``
```
this line is produced before starting consumer
this line is produced after starting consumer
this line is produced after stopping consumer
```

### Consume Messages
> $ ./kafka-console-consumers.sh --zookeeper \`docker-machine ip bigdata`:2181 --topic bigdata
```
this line is produced after starting consumer
```
> $ ./kafka-console-consumers.sh --zookeeper \`docker-machine ip bigdata`:2181 --topic bigdata --from-beginning
```
this line is produced before starting consumer
this line is produced after starting consumer
this line is produced after stopping consumer
```

### Look into Kafka Broker
> $ docker exec -it kafka bash
> <br> confluent@f22de4ef65b1:/$ cd /var/lib/kafka
> <br> confluent@f22de4ef65b1:/var/lib/kafka$ ls
```
bigdata-0  cleaner-offset-checkpoint  meta.properties  recovery-point-offset-checkpoint  replication-offset-checkpoint
```