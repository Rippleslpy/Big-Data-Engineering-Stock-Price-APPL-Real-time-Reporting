## Setting up environment

$ python --version
> Python 2.7.12

$ scala -version
```
Scala code runner version 2.11.8 -- Copyright 2002-2016, LAMP/EPFL
```
$ pip2 --version
```
pip 8.1.2 from /usr/local/lib/python2.7/site-packages (python 2.7)
```

Since I'm using pyhton2 and 3 at the same time, this is the pip for python2. 

$ sbt sbtVersion
```
[info] Set current project to terrywang (in build file:/Users/TerryWang/)
[info] 0.13.12
```
$ docker -v
```
Docker version 1.12.2, build bb80604
```

## Setting up docker

Create virtual machine first by:
$ docker-machine create --driver virtualbox --virtualbox-cpu-count 2 --virtualbox-memory 2048 bigdata

$ Docker-machine ip bigdata
```
192.168.99.100
```
$ eval $(docker-machine env bigdata)

This is the first time I run these images, so I need to fetch the images of chit-chat,kafka and zookeeper from remote server.

$ docker run -d -p 3000:3000 unclebarney/chit-chat
```
Unable to find image 'unclebarney/chit-chat:latest' locally
latest: Pulling from unclebarney/chit-chat
c52e3ed763ff: Pull complete
a3ed95caeb02: Pull complete
39017a32cc96: Pull complete
7d703724b60c: Pull complete
Digest: sha256:5f1cb80597837de5bea1e7e4748c9d5887b161982eee9e798ef7b2de7be251ba
Status: Downloaded newer image for unclebarney/chit-chat:latest
33de7dfe545969126adbb925510d171f61fedf983b94c224b2bfd480ac9e6875
```

$ docker run -d -p 2181:2181 -p 2888:2888 -p 3888:3888 --name zookeeper confluent/zookeeper
```
Unable to find image 'confluent/zookeeper:latest' locally
latest: Pulling from confluent/zookeeper
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
dd7b7029d4f9: Pull complete
5de42c73a24d: Pull complete
82153f3e2e3f: Pull complete
1b403d9fce92: Pull complete
b5c575c9edb6: Pull complete
Digest: sha256:bb097bce322f5553ed1511234f97e7eedb0900211c46958357fbcb342917cbf8
Status: Downloaded newer image for confluent/zookeeper:latest
```
$ docker run -d -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=`docker-machine ip bigdata` -e KAFKA_ADVERTISED_PORT=9092 --name kafka --link zookeeper:zookeeper confluent/kafka

$ docker run -d -p 7199:7199 -p 9042:9042 -p 9160:9160 -p 7001:7001 --name cassandra cassandra:3.7
also pull cassandra for future usage

$ docker images
```
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
cassandra               3.7                 25427f353269        3 weeks ago         382.4 MB
confluent/zookeeper     latest              4a1778ad1528        4 months ago        584.5 MB
confluent/kafka         latest              2b9ba35e1775        4 months ago        584.5 MB
unclebarney/chit-chat   latest              639e46d7a14a        8 months ago        31.86 MB
```
Now I have all 4 containers installed on my mac




## get CLIs

$ wget http://apache.mirrors.ionfish.org/kafka/0.10.0.1/kafka_2.11-0.10.0.1.tgz
$ tar xvf kafka_2.11-0.10.0.1.tgz
$ mv kafka_2.11-0.10.0.1 kafka
$ rm kafka_2.11-0.10.0.1.tgz
$ cd kafka/bin

$ ./kafka-topics.sh --create --zookeeper `docker-machine ip bigdata` --replication-factor 1 --partitions 1 --topic bigdata
```
Created topic "bigdata".
```
$ ./kafka-topics.sh --list --zookeeper `docker-machine ip bigdata`
```
bigdata
```
$ wget http://apache.mirrors.ionfish.org/zookeeper/zookeeper-3.4.8/zookeeper-3.4.8.tar.gz
$ tar xvf zookeeper-3.4.8.tar.gz
$ mv zookeeper-3.4.8 zookeeper
$ rm zookeeper-3.4.8.tar.gz

## Play with Kafka & Zookeeper
$ ./kafka-console-producer.sh --broker-list `docker-machine ip bigdata`:9092 --topic bigdata
```
bigdata
```

$ cd zookeeper/bin
$ ./zkCli.sh -server `docker-machine ip bigdata`:2181
$ ls/
```
ZooKeeper -server host:port cmd args
	stat path [watch]
	set path data [version]
	ls path [watch]
	delquota [-n|-b] path
	ls2 path [watch]
	setAcl path acl
	setquota -n|-b val path
	history
	redo cmdno
	printwatches on|off
	delete path [version]
	sync path
	listquota path
	rmr path
	get path [watch]
	create [-s] [-e] path data acl
	addauth scheme auth
	quit
	getAcl path
	close
	connect host:port
```

$ ls/
$ ls /zookeeper
[zk: 192.168.99.100:2181(CONNECTED) 2] get /zookeeper/quota
```
cZxid = 0x0
ctime = Wed Dec 31 18:00:00 CST 1969
mZxid = 0x0
mtime = Wed Dec 31 18:00:00 CST 1969
pZxid = 0x0
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 0
numChildren = 0
```

[zk: 192.168.99.100:2181(CONNECTED) 3] create /workers "bittiger"
```
Created /workers
```
[zk: 192.168.99.100:2181(CONNECTED) 4] ls/
[zk: 192.168.99.100:2181(CONNECTED) 5] ls /workers
```
[]
```
[zk: 192.168.99.100:2181(CONNECTED) 6] get /workers
```
bittiger
cZxid = 0x32
ctime = Fri Oct 21 21:20:11 CDT 2016
mZxid = 0x32
mtime = Fri Oct 21 21:20:11 CDT 2016
pZxid = 0x32
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 8
numChildren = 0
```
Delete znode:
[zk: 192.168.99.100:2181(CONNECTED) 7] delete /workers
[zk: 192.168.99.100:2181(CONNECTED) 8] ls
[zk: 192.168.99.100:2181(CONNECTED) 9] ls/
[zk: 192.168.99.100:2181(CONNECTED) 10] ls/
[zk: 192.168.99.100:2181(CONNECTED) 11] ls /workers
```
Node does not exist: /workers
```

Create ephemeral znode
[zk: 192.168.99.100:2181(CONNECTED) 12] create -e /workers "unclebarney"
```
Created /workers
```
[zk: 192.168.99.100:2181(CONNECTED) 13] ls/
[zk: 192.168.99.100:2181(CONNECTED) 14] ls /workers
```
[]
```
[zk: 192.168.99.100:2181(CONNECTED) 15] get /workers
```
unclebarney
cZxid = 0x34
ctime = Fri Oct 21 21:23:40 CDT 2016
mZxid = 0x34
mtime = Fri Oct 21 21:23:40 CDT 2016
pZxid = 0x34
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x157e9af3f4d0006
dataLength = 11
numChildren = 0
```

Watcher

[zk: 192.168.99.100:2181(CONNECTED) 16] get /workers true
```
unclebarney
cZxid = 0x34
ctime = Fri Oct 21 21:23:40 CDT 2016
mZxid = 0x34
mtime = Fri Oct 21 21:23:40 CDT 2016
pZxid = 0x34
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x157e9af3f4d0006
dataLength = 11
numChildren = 0
```
