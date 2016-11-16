
# Dependencies
> $ scala -version
```
Scala code runner version 2.11.8 -- Copyright 2002-2016, LAMP/EPFL
```
> $ sbt sbtVersion
```
[info] Set current project to xb (in build file:Users/yifengr/)
[info] 0.13.12
```
> $ python --version
```
Python 2.7.10
```
> $ pip --version
```
pip 8.1.2 from /Library/Python/2.7/site-packages/pip-8.1.2-py2.7.egg (python 2.7)
```

----------


rk with Zookeeper
### Start Zookeeper Server
> $ docker run -d -p 2181:2181 -p 2888:2888 -p 3888:3888 --name zookeeper confluent/zookeeper
> ``First time run``
```
docker: Error response from daemon: Conflict. The name "/zookeeper" is already in use by container 35c0580fd78c174970faf032b24f9e7c4b1bf76516fba314c6a57603cbb48230. You have to remove (or rename) that container to be able to reuse that name..
See 'docker run --help'.
```
```
I had this error is because system had already pulled zookeeper to docker when I played the chit-chat, so I just run "docker start zookeeper" to start it. 
```
> ``Second time run``
```
zookeeper
```
> $docker images
```
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
redis                   alpine              906fffc0e2f4        10 days ago         20.38 MB
cassandra               3.7                 25427f353269        4 weeks ago         382.4 MB
confluent/zookeeper     latest              4a1778ad1528        5 months ago        584.5 MB
confluent/kafka         latest              2b9ba35e1775        5 months ago        584.5 MB
unclebarney/chit-chat   latest              639e46d7a14a        8 months ago        31.86 MB
```
> $ docker ps
```
35c0580fd78c        confluent/zookeeper   "/usr/local/bin/zk-do"   9 days ago          Up 11 hours         0.0.0.0:2181->2181/tcp, 0.0.0.0:2888->2888/tcp, 0.0.0.0:3888->3888/tcp   zookeeper
```
### Start Zookeeper CLI
> $ ./zkCli.sh -server  \`docker-machine ip bigdata`:2181
```
Connecting to 192.168.99.100:2181
2016-10-29 15:10:18,600 [myid:] - INFO  [main:Environment@100] - Client environment:zookeeper.version=3.4.8--1, built on 02/06/2016 03:18 GMT
2016-10-29 15:10:18,605 [myid:] - INFO  [main:Environment@100] - Client environment:host.name=yifengs-mbp
2016-10-29 15:10:18,605 [myid:] - INFO  [main:Environment@100] - Client environment:java.version=1.8.0_71
2016-10-29 15:10:18,608 [myid:] - INFO  [main:Environment@100] - Client environment:java.vendor=Oracle Corporation
2016-10-29 15:10:18,608 [myid:] - INFO  [main:Environment@100] - Client environment:java.home=/Library/Java/JavaVirtualMachines/jdk1.8.0_71.jdk/Contents/Home/jre
2016-10-29 15:10:18,608 [myid:] - INFO  [main:Environment@100] - Client environment:java.class.path=/Users/yifengr/Downloads/zookeeper/bin/../build/classes:/Users/yifengr/Downloads/zookeeper/bin/../build/lib/*.jar:/Users/yifengr/Downloads/zookeeper/bin/../lib/slf4j-log4j12-1.6.1.jar:/Users/yifengr/Downloads/zookeeper/bin/../lib/slf4j-api-1.6.1.jar:/Users/yifengr/Downloads/zookeeper/bin/../lib/netty-3.7.0.Final.jar:/Users/yifengr/Downloads/zookeeper/bin/../lib/log4j-1.2.16.jar:/Users/yifengr/Downloads/zookeeper/bin/../lib/jline-0.9.94.jar:/Users/yifengr/Downloads/zookeeper/bin/../zookeeper-3.4.8.jar:/Users/yifengr/Downloads/zookeeper/bin/../src/java/lib/*.jar:/Users/yifengr/Downloads/zookeeper/bin/../conf:
2016-10-29 15:10:18,609 [myid:] - INFO  [main:Environment@100] - Client environment:java.library.path=/Users/yifengr/Library/Java/Extensions:/Library/Java/Extensions:/Network/Library/Java/Extensions:/System/Library/Java/Extensions:/usr/lib/java:.
2016-10-29 15:10:18,609 [myid:] - INFO  [main:Environment@100] - Client environment:java.io.tmpdir=/var/folders/t4/827jlskj7bq54t074brjng7m0000gn/T/
2016-10-29 15:10:18,609 [myid:] - INFO  [main:Environment@100] - Client environment:java.compiler=<NA>
2016-10-29 15:10:18,609 [myid:] - INFO  [main:Environment@100] - Client environment:os.name=Mac OS X
2016-10-29 15:10:18,609 [myid:] - INFO  [main:Environment@100] - Client environment:os.arch=x86_64
2016-10-29 15:10:18,609 [myid:] - INFO  [main:Environment@100] - Client environment:os.version=10.12.1
2016-10-29 15:10:18,609 [myid:] - INFO  [main:Environment@100] - Client environment:user.name=yifengr
2016-10-29 15:10:18,609 [myid:] - INFO  [main:Environment@100] - Client environment:user.home=/Users/yifengr
2016-10-29 15:10:18,609 [myid:] - INFO  [main:Environment@100] - Client environment:user.dir=/Users/yifengr/Downloads/zookeeper/bin
2016-10-29 15:10:18,611 [myid:] - INFO  [main:ZooKeeper@438] - Initiating client connection, connectString=192.168.99.100:2181 sessionTimeout=30000 watcher=org.apache.zookeeper.ZooKeeperMain$MyWatcher@446cdf90
Welcome to ZooKeeper!
2016-10-29 15:10:18,646 [myid:] - INFO  [main-SendThread(192.168.99.100:2181):ClientCnxn$SendThread@1032] - Opening socket connection to server 192.168.99.100/192.168.99.100:2181. Will not attempt to authenticate using SASL (unknown error)
JLine support is enabled
2016-10-29 15:10:18,730 [myid:] - INFO  [main-SendThread(192.168.99.100:2181):ClientCnxn$SendThread@876] - Socket connection established to 192.168.99.100/192.168.99.100:2181, initiating session
[zk: 192.168.99.100:2181(CONNECTING) 0] 2016-10-29 15:10:18,835 [myid:] - INFO  [main-SendThread(192.168.99.100:2181):ClientCnxn$SendThread@1299] - Session establishment complete on server 192.168.99.100/192.168.99.100:2181, sessionid = 0x1580fe537270000, negotiated timeout = 30000
>
WATCHER::
>
WatchedEvent state:SyncConnected type:None path:null
```

### Browse Znode Data
> [zk: 192.168.99.100:2181(CONNECTED) 0] ls /
```
[controller_epoch, brokers, zookeeper, admin, isr_change_notification, consumers, config]
```
> [zk: 192.168.99.100:2181(CONNECTED) 1] ls /zookeeper
```
[quota]
```
> [zk: 192.168.99.100:2181(CONNECTED) 2] get /zookeeper/quota
```
cZxid = 0x0
ctime = Wed Dec 31 16:00:00 PST 1969
mZxid = 0x0
mtime = Wed Dec 31 16:00:00 PST 1969
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
[controller_epoch, brokers, zookeeper, admin, isr_change_notification, consumers, config, workers]
```
> [zk: 192.168.99.100:2181(CONNECTED) 5] ls /workers
```
[]
```
> [zk: 192.168.99.100:2181(CONNECTED) 6] get /workers
```
bittiger
cZxid = 0x46f
ctime = Sat Oct 29 18:08:08 PDT 2016
mZxid = 0x46f
mtime = Sat Oct 29 18:08:08 PDT 2016
pZxid = 0x46f
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
[controller_epoch, brokers, zookeeper, admin, isr_change_notification, consumers, config]
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
[controller_epoch, brokers, zookeeper, admin, isr_change_notification, consumers, config]
```
> [zk: 192.168.99.100:2181(CONNECTED) 13] ls /workers
```
[]
```
> [zk: 192.168.99.100:2181(CONNECTED) 14] get /workers
```
unclebarney
cZxid = 0x471
ctime = Sat Oct 29 18:48:50 PDT 2016
mZxid = 0x471
mtime = Sat Oct 29 18:48:50 PDT 2016
pZxid = 0x471
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x1580fe537270000
dataLength = 11
numChildren = 0
```
----------

# Work with Kafka
### Start kafka Server
> docker start kafka
```
kafka
```
> $ docker images
```
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
redis                   alpine              906fffc0e2f4        11 days ago         20.38 MB
cassandra               3.7                 25427f353269        4 weeks ago         382.4 MB
confluent/zookeeper     latest              4a1778ad1528        5 months ago        584.5 MB
confluent/kafka         latest              2b9ba35e1775        5 months ago        584.5 MB
unclebarney/chit-chat   latest              639e46d7a14a        8 months ago        31.86 MB
```
> $ docker ps
```
CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                                                                    NAMES
3597faa922a5        confluent/kafka       "/usr/local/bin/kafka"   10 days ago         Up 4 seconds        0.0.0.0:9092->9092/tcp                                                   kafka
35c0580fd78c        confluent/zookeeper   "/usr/local/bin/zk-do"   10 days ago         Up 15 hours         0.0.0.0:2181->2181/tcp, 0.0.0.0:2888->2888/tcp, 0.0.0.0:3888->3888/tcp   zookeeper
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
> <br> ``message input from command line``
```
hello world
awesome
fascinating
```

### Consume Messages
> $ ./kafka-console-consumer.sh --zookeeper \`docker-machine ip bigdata`:2181 --topic bigdata
```
this line is produced after starting consumer
```
> $ ./kafka-console-consumer.sh --zookeeper \`docker-machine ip bigdata`:2181 --topic bigdata --from-beginning
```
hello world
awesome
fascinating
```

### Look into Kafka Broker
> $ docker exec -it kafka bash
> <br> confluent@f22de4ef65b1:/$ cd /var/lib/kafka
> <br> confluent@f22de4ef65b1:/var/lib/kafka$ ls
```
bigdata-0  cleaner-offset-checkpoint  meta.properties  recovery-point-offset-checkpoint  replication-offset-checkpoint
```

