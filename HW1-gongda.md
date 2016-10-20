# HW1 - GONGDA GE

## play with docker
* ** docker-machine ip bigdata **
> Error getting IP address: Host is not running

    because bigdata is stopped
* ** docker-machine start bigdata **
* ** docker-machine ip big data **
> 192.168.99.100
*  ** eval $(docker-machine env bigdata) **
> now, we can communicate with docker daemon
* ** docker run -d -p 3000:3000 unclebarney/chit-chat **
> 1cf158f839a5176b434b35f5ce47ea615cc74210469c5d4dccf21bf76831c30b
* ** docker iamges **
> REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
cassandra               3.7                 25427f353269        3 weeks ago         382.4 MB
redis                   alpine              e1f619d04b7a        3 weeks ago         20.38 MB
confluent/zookeeper     latest              4a1778ad1528        4 months ago        584.5 MB
confluent/kafka         latest              2b9ba35e1775        4 months ago        584.5 MB
unclebarney/chit-chat   latest              639e46d7a14a        8 months ago        31.86 MB
* ** docker ps **
> CONTAINER ID        IMAGE                   COMMAND             CREATED              STATUS              PORTS                    NAMES
1cf158f839a5        unclebarney/chit-chat   "node index.js"     About a minute ago   Up About a minute   0.0.0.0:3000->3000/tcp   fervent_brattain

## play with kafka
* version check
  * ** scala -version **
> Scala code runner version 2.11.8 -- Copyright 2002-2016, LAMP/EPFL
  * ** sbt --version **
>[info] Set current project to gongda (in build       file:/Users/gongda/)
[info] 0.13.11
  * ** python --version **
>python --version
Python 2.7.11
  * ** pip --version **
>pip 8.1.2 from /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages (python 2.7)


* *start kafka server*
* ** docker run -d -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME='docker-machine ip bigdata' -e KAFKA_ADVERTISED_PORT=9092 --name kafka --link zookeeper:zookeeper confluent/kafka**
> docker: Error response from daemon: Conflict. The name "/kafka" is already in use by container 04e72b37adc2840919dccf4abaf62519a22e3ee73e57c2646a056a20268eae21. You have to remove (or rename) that container to be able to reuse that name..
kafka已经有了  直接docker start kafka
* ** ./kafka-topics.sh --create --zookeeper `docker-machine ip bigdata` --replication-factor 1 --partitions 1 --topic bigdata **
> Error while executing topic command : Topic "bigdata" already exists.
之前已经创建过该TOPIC
* 怎么删除TOPIC?
* ** ./kafka-topics.sh --list --zookeeper `docker-machine ip bigdata` **
> __consumer_offsets
bigdata
stock-analyzer
tock-analyzer
查看已created 的topic ?

## look up on zookeeper
* ** /zkCli.sh -server `docker-machine ip bigdata`:2181 **
> Connecting to 192.168.99.100:2181
2016-10-20 15:16:47,476 [myid:] - INFO  [main:Environment@100] - Client environment:zookeeper.version=3.4.8--1, built on 02/06/2016 03:18 GMT
2016-10-20 15:16:47,479 [myid:] - INFO  [main:Environment@100] - Client environment:host.name=gongdas-mbp.wv.cc.cmu.edu
2016-10-20 15:16:47,479 [myid:] - INFO  [main:Environment@100] - Client environment:java.version=1.8.0_74
2016-10-20 15:16:47,482 [myid:] - INFO  [main:Environment@100] - Client environment:java.vendor=Oracle Corporation
2016-10-20 15:16:47,482 [myid:] - INFO  [main:Environment@100] - Client environment:java.home=/Library/Java/JavaVirtualMachines/jdk1.8.0_74.jdk/Contents/Home/jre
2016-10-20 15:16:47,482 [myid:] - INFO  [main:Environment@100] - Client environment:java.class.path=/Users/gongda/zookeeper/bin/../build/classes:/Users/gongda/zookeeper/bin/../build/lib/*.jar:/Users/gongda/zookeeper/bin/../lib/slf4j-log4j12-1.6.1.jar:/Users/gongda/zookeeper/bin/../lib/slf4j-api-1.6.1.jar:/Users/gongda/zookeeper/bin/../lib/netty-3.7.0.Final.jar:/Users/gongda/zookeeper/bin/../lib/log4j-1.2.16.jar:/Users/gongda/zookeeper/bin/../lib/jline-0.9.94.jar:/Users/gongda/zookeeper/bin/../zookeeper-3.4.8.jar:/Users/gongda/zookeeper/bin/../src/java/lib/*.jar:/Users/gongda/zookeeper/bin/../conf:
2016-10-20 15:16:47,482 [myid:] - INFO  [main:Environment@100] - Client environment:java.library.path=/Users/gongda/Library/Java/Extensions:/Library/Java/Extensions:/Network/Library/Java/Extensions:/System/Library/Java/Extensions:/usr/lib/java:.
2016-10-20 15:16:47,482 [myid:] - INFO  [main:Environment@100] - Client environment:java.io.tmpdir=/var/folders/kc/y_wqkb212gjdddf2sdk1pwqw0000gn/T/
2016-10-20 15:16:47,482 [myid:] - INFO  [main:Environment@100] - Client environment:java.compiler=<NA>
2016-10-20 15:16:47,482 [myid:] - INFO  [main:Environment@100] - Client environment:os.name=Mac OS X
2016-10-20 15:16:47,482 [myid:] - INFO  [main:Environment@100] - Client environment:os.arch=x86_64
2016-10-20 15:16:47,482 [myid:] - INFO  [main:Environment@100] - Client environment:os.version=10.12
2016-10-20 15:16:47,482 [myid:] - INFO  [main:Environment@100] - Client environment:user.name=gongda
2016-10-20 15:16:47,483 [myid:] - INFO  [main:Environment@100] - Client environment:user.home=/Users/gongda
2016-10-20 15:16:47,483 [myid:] - INFO  [main:Environment@100] - Client environment:user.dir=/Users/gongda/zookeeper/bin
2016-10-20 15:16:47,484 [myid:] - INFO  [main:ZooKeeper@438] - Initiating client connection, connectString=192.168.99.100:2181 sessionTimeout=30000 watcher=org.apache.zookeeper.ZooKeeperMain$MyWatcher@446cdf90
Welcome to ZooKeeper!
2016-10-20 15:16:47,510 [myid:] - INFO  [main-SendThread(192.168.99.100:2181):ClientCnxn$SendThread@1032] - Opening socket connection to server 192.168.99.100/192.168.99.100:2181. Will not attempt to authenticate using SASL (unknown error)
JLine support is enabled
2016-10-20 15:16:47,568 [myid:] - INFO  [main-SendThread(192.168.99.100:2181):ClientCnxn$SendThread@876] - Socket connection established to 192.168.99.100/192.168.99.100:2181, initiating session
2016-10-20 15:16:47,578 [myid:] - INFO  [main-SendThread(192.168.99.100:2181):ClientCnxn$SendThread@1299] - Session establishment complete on server 192.168.99.100/192.168.99.100:2181, sessionid = 0x157e37c13090004, negotiated timeout = 30000
WATCHER::
WatchedEvent state:SyncConnected type:None path:null
* ** ls / **
> [controller_epoch, controller, brokers, zookeeper, admin, isr_change_notification, consumers, config]

## produce message and comsume message
* produce message: ** ./kafka-console-producer.sh --broker-list `docker-machine ip bigdata`:9092 --topic bigdata **
> 开始写message, 每次回车为一条
* consume message
  * ** ./kafka-console-consumer.sh --zookeeper `docker-machine ip bigdata`:2181 --topic bigdata **
> 读取最新的message
每次发送一条, comsumer 会读取一条
  * ** ./kafka-console-consumer.sh --zookeeper `docker-machine ip bigdata`:2181 --topic bigdata --from-beginning **
> 读取所有的

## look into kafka broker
* ** docker exec -it kafka bash **
> confluent@04e72b37adc2:/$ 进入?
* confluent@04e72b37adc2:/$ ** ls **
> bin  boot  dev	etc  home  lib	lib64  media  mnt  opt	proc  root  run  sbin  srv  sys  tmp  usr  var
* ** cd /var/lib/kafka  ** then ** ls **
> __consumer_offsets-0   __consumer_offsets-18  __consumer_offsets-27  __consumer_offsets-36  __consumer_offsets-45  bigdata-0
__consumer_offsets-1   __consumer_offsets-19  __consumer_offsets-28  __consumer_offsets-37  __consumer_offsets-46  cleaner-offset-checkpoint
__consumer_offsets-10  __consumer_offsets-2   __consumer_offsets-29  __consumer_offsets-38  __consumer_offsets-47  meta.properties
__consumer_offsets-11  __consumer_offsets-20  __consumer_offsets-3   __consumer_offsets-39  __consumer_offsets-48  recovery-point-offset-checkpoint
__consumer_offsets-12  __consumer_offsets-21  __consumer_offsets-30  __consumer_offsets-4   __consumer_offsets-49  replication-offset-checkpoint
__consumer_offsets-13  __consumer_offsets-22  __consumer_offsets-31  __consumer_offsets-40  __consumer_offsets-5   stock-analyzer-0
__consumer_offsets-14  __consumer_offsets-23  __consumer_offsets-32  __consumer_offsets-41  __consumer_offsets-6   tock-analyzer-0
__consumer_offsets-15  __consumer_offsets-24  __consumer_offsets-33  __consumer_offsets-42  __consumer_offsets-7
__consumer_offsets-16  __consumer_offsets-25  __consumer_offsets-34  __consumer_offsets-43  __consumer_offsets-8
__consumer_offsets-17  __consumer_offsets-26  __consumer_offsets-35  __consumer_offsets-44  __consumer_offsets-9

## work with zookeeper
* ** docker run -d -p 2181:2181 -p 2888:2888 -p 3888:3888 --name zookeeper confluent/zookeeper **
> docker: Error response from daemon: Conflict. The name "/zookeeper" is already in use by container bf767598c6256553fc34cc11d4b065664a4f216e34a8d06cdef64a3b58231e46. You have to remove (or rename) that container to be able to reuse that name..
已经有该container了, 是否只需要start就可以了

* ** cd ~ ** then ** cd zookeeper/bin **
* ** ./zkCli.sh -server `docker-machine ip bigdata`:2181 **
> [zk: 192.168.99.100:2181(CONNECTED) 0]
* ** ./zkCli.sh -server localhost:2181 ** 
> 不知道有什么用
* ** ls / **
> controller_epoch, controller, brokers, zookeeper, admin, isr_change_notification, consumers, config]
* ** ls /zookeeper **
> [quota]
* ** get /zookeeper/quota **
> cZxid = 0x0
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
* ** create /workers "bittiger" **
>reated /workers
* ** ls / **
>controller_epoch, controller, brokers, zookeeper, admin, isr_change_notification, consumers, config, workers]
多了workers
* ** ls /workers **
> []
* ** get /workers **
> bittiger
cZxid = 0x568
ctime = Thu Oct 20 16:10:05 EDT 2016
mZxid = 0x568
mtime = Thu Oct 20 16:10:05 EDT 2016
pZxid = 0x568
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 8
numChildren = 0
* ** delete /workers **
> 删除workers
* ** ls / **
> [controller_epoch, controller, brokers, zookeeper, admin, isr_change_notification, consumers, config]
可以看到workers已经删掉了
* ** ls/workers ** & ** get /workers ** 
* create ephemeral znode data
* ** reate -e /workers "gongda" **
* ** ls / **
> [controller_epoch, controller, brokers, zookeeper, admin, isr_change_notification, consumers, config, workers]又有workers了
* ** ls /workers **
> []
* ** get /workers **
> gongda
cZxid = 0x56a
ctime = Thu Oct 20 16:15:36 EDT 2016
mZxid = 0x56a
mtime = Thu Oct 20 16:15:36 EDT 2016
pZxid = 0x56a
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x157e37c1309000e
dataLength = 6
numChildren = 0
* watcher ** get /workers true **
> gongda
cZxid = 0x56a
ctime = Thu Oct 20 16:15:36 EDT 2016
mZxid = 0x56a
mtime = Thu Oct 20 16:15:36 EDT 2016
pZxid = 0x56a
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x157e37c1309000e
dataLength = 6
numChildren = 0



  
  

