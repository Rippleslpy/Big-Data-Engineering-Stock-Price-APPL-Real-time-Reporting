## Week 1 - Homework 1：ZhengKUANG
Submission requirements, submit in form of Markdown document, need to have commandlines, and corresponding output
* Play with Apache Kafka
* Play with Apache Zookeeper

----------

 - docker-machine create --driver virtualbox --virtualbox-cpu-count 2 --virtualbox-memory
2048 bigdata2
 - docker-machine ls
 - 这两行的作用是创建bigdata2这个docker deamon并且在docker-machine里面查看

输出：
C:\Users\kuang>docker-machine ls
NAME       ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER    ERRORS
bigdata    -        virtualbox   Stopped                                       Unknown
bigdata2   -        virtualbox   Running   tcp://192.168.99.100:2376           v1.12.2
default    -        virtualbox   Stopped                                       Unknown


----------

 - Docker-machine ip bigdata2
 
输出：192.168.99.100


----------

 - FOR /f "tokens=*" %i IN ('docker-machine env --shell cmd bigdata') DO
   %i

输出：
C:\Users\kuang>FOR /f "tokens=*" %i IN ('docker-machine env --shell cmd bigdata2') DO %i

C:\Users\kuang>SET DOCKER_TLS_VERIFY=1

C:\Users\kuang>SET DOCKER_HOST=tcp://192.168.99.100:2376

C:\Users\kuang>SET DOCKER_CERT_PATH=C:\Users\kuang\.docker\machine\machines\bigdata2

C:\Users\kuang>SET DOCKER_MACHINE_NAME=bigdata2

C:\Users\kuang>REM Run this command to configure your shell:

C:\Users\kuang>REM      @FOR /f "tokens=*" %i IN ('docker-machine env --shell cmd bigdata2') DO @%i

 - 目的：让客户端和server通信


----------

 - docker run -d -p 3000:3000 unclebarney/chit-chat

输出：
Unable to find image 'unclebarney/chit-chat:latest' locally
latest: Pulling from unclebarney/chit-chat
c52e3ed763ff: Pull complete
a3ed95caeb02: Pull complete
39017a32cc96: Pull complete
7d703724b60c: Pull complete
Digest: sha256:5f1cb80597837de5bea1e7e4748c9d5887b161982eee9e798ef7b2de7be251ba
Status: Downloaded newer image for unclebarney/chit-chat:latest
0ef0e30e9524f5722f5d185c3191be7e82b00289dc2f4d2b7fcbfa428b43058e


----------

 - docker images
输出：
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
unclebarney/chit-chat   latest              639e46d7a14a        8 months ago        31.86 MB

 


----------



 - docker ps
输出：
CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                    NAMES
0ef0e30e9524        unclebarney/chit-chat   "node index.js"     4 minutes ago       Up 4 minutes        0.0.0.0:3000->3000/tcp   ecstatic_thompson


----------


## 关于bigdata2的docker deamon就演示到这里，现在演示自己在bigdata上面搭建的zookeeper，kafka和cassandra ##


----------

 - docker-machine stop bigdata2
 - docker-machine start bigdata
 - FOR /f "tokens=*" %i IN ('docker-machine env --shell cmd bigdata') DO %i
 - docker-machine ls
 -
输出：
NAME       ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER    ERRORS
bigdata    *        virtualbox   Running   tcp://192.168.99.100:2376           v1.12.1
bigdata2   -        virtualbox   Stopped                                       Unknown
default    -        virtualbox   Stopped                                       Unknown


----------

 - docker ps -a
CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS                     PORTS                                                                                                      NAMES
5c4b007b67be        cassandra:3.7         "/docker-entrypoint.s"   3 days ago          Exited (1) 3 minutes ago   0.0.0.0:7001->7001/tcp, 0.0.0.0:7199->7199/tcp, 0.0.0.0:9042->9042/tcp, 7000/tcp, 0.0.0.0:9160->9160/tcp   cassandra
1b9bd4e0ab22        confluent/kafka       "/usr/local/bin/kafka"   3 days ago          Exited (1) 3 minutes ago   0.0.0.0:9092->9092/tcp                                                                                     kafka
ed5f41e31640        confluent/zookeeper   "/usr/local/bin/zk-do"   3 days ago          Exited (1) 3 minutes ago   0.0.0.0:2181->2181/tcp, 0.0.0.0:2888->2888/tcp, 0.0.0.0:3888->3888/tcp                                     zookeeper
 - docker start zookeeper
 - docker start kafka
 - docker start cassandra
 - docker ps
 
输出：

CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                                                                                                      NAMES
5c4b007b67be        cassandra:3.7         "/docker-entrypoint.s"   3 days ago          Up About a minute   0.0.0.0:7001->7001/tcp, 0.0.0.0:7199->7199/tcp, 0.0.0.0:9042->9042/tcp, 7000/tcp, 0.0.0.0:9160->9160/tcp   cassandra
1b9bd4e0ab22        confluent/kafka       "/usr/local/bin/kafka"   3 days ago          Up 4 seconds        0.0.0.0:9092->9092/tcp                                                                                     kafka
ed5f41e31640        confluent/zookeeper   "/usr/local/bin/zk-do"   3 days ago          Up About a minute   0.0.0.0:2181->2181/tcp, 0.0.0.0:2888->2888/tcp, 0.0.0.0:3888->3888/tcp        


----------

 - kafka-topics.bat --list --zookeeper 192.168.99.100
输出：
__consumer_offsets
bigdata
stock-analyser
stock-analyzer
stock_analyser
stock_analyzer
 - zkCli.cmd -server 192.168.99.100:2181
 
 - ls /
输出：
[controller_epoch, controller, brokers, zookeeper, admin, isr_change_notification, consumers, config]


----------

 - kafka-console-producer.bat --broker-list 192.168.99.100:9092 --topic bigdata
ddddsfd
afdasfa
qwerqewr
zcvzcxv
gfsdgdsf
erqwrqew
 - kafka-console-consumer.bat --zookeeper 192.168.99.100:2181 --topic bigdata --from-beginning
输出：
nning
ddd
safd
eqwreq
hello
world
kafka
adsfa
ddddsfd
afdasfa
qwerqewr
zcvzcxv
gfsdgdsf
erqwrqew
 


----------

 - zkCli.cmd -server 192.168.99.100:2181
 - ls /
 - ls /zookeeper
 - get /zookeeper/quota
输出：

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

 - create /workers "bittiger"
输出：Created /workers
 - ls /
输出：
[controller_epoch, controller, brokers, zookeeper, admin, isr_change_notification, consumers, config, workers]
 - ls /workers
输出：
[]
 - get  /workers
输出：
bittiger
cZxid = 0x2a4
ctime = Mon Oct 17 14:23:00 CST 2016
mZxid = 0x2a4
mtime = Mon Oct 17 14:23:00 CST 2016
pZxid = 0x2a4
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 8
numChildren = 0


----------

 - delete /workers
 - ls /
输出：
[controller_epoch, controller, brokers, zookeeper, admin, isr_change_notification, consumers, config]
 - ls /workers
 - get /workers
输出:
 Node does not exist: /workers


----------

 - create -e /workers "unclebarney"
 输出：
Created /workers
 - ls /
 输出：
[controller_epoch, controller, brokers, zookeeper, admin, isr_change_notification, consumers, config, workers]
 - ls /workers
输出：
[]
 - get /workers
输出：
unclebarney
cZxid = 0x2a6
ctime = Mon Oct 17 14:41:34 CST 2016
mZxid = 0x2a6
mtime = Mon Oct 17 14:41:34 CST 2016
pZxid = 0x2a6
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x157d127038a0007
dataLength = 11
numChildren = 0
 - get /workers true
输出：
unclebarney
cZxid = 0x2a6
ctime = Mon Oct 17 14:41:34 CST 2016
mZxid = 0x2a6
mtime = Mon Oct 17 14:41:34 CST 2016
pZxid = 0x2a6
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x157d127038a0007
dataLength = 11
numChildren = 0

 


             

 
