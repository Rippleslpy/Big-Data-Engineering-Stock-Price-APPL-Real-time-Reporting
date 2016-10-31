Week 1 Homework

 
**Play with Docker-Windows**

C:\Users\ansonlivingroom>docker-machine create --driver virtualbox --virtualbox-
cpu-count 2 --virtualbox-memory 2048 bigdata2

Running pre-create checks...
Creating machine...
(bigdata2) Copying C:\Users\ansonlivingroom\.docker\machine\cache\boot2docker.is
o to C:\Users\ansonlivingroom\.docker\machine\machines\bigdata2\boot2docker.iso.
..
(bigdata2) Creating VirtualBox VM...
(bigdata2) Creating SSH key...
(bigdata2) Starting the VM...
(bigdata2) Check network to re-create if needed...
(bigdata2) Waiting for an IP...
Waiting for machine to be running, this may take a few minutes...
Detecting operating system of created instance...
Waiting for SSH to be available...
Detecting the provisioner...
Provisioning with boot2docker...
Copying certs to the local machine directory...
Copying certs to the remote machine...
Setting Docker configuration on the remote daemon...
Checking connection to Docker...
Docker is up and running!
To see how to connect your Docker Client to the Docker Engine running on this vi
rtual machine, run: docker-machine env bigdata2

C:\Users\ansonlivingroom>Docker-machine ip bigdata2
192.168.99.101

C:\Users\ansonlivingroom>docker-machine env --shell cmd bigdata2
SET DOCKER_TLS_VERIFY=1
SET DOCKER_HOST=tcp://192.168.99.101:2376
SET DOCKER_CERT_PATH=C:\Users\ansonlivingroom\.docker\machine\machines\bigdata2
SET DOCKER_MACHINE_NAME=bigdata2
REM Run this command to configure your shell:
REM     @FOR /f "tokens=*" %i IN ('docker-machine env --shell cmd bigdata2') DO
@%i

C:\Users\ansonlivingroom>FOR /f "tokens=*" %i IN ('docker-machine env --shell cm
d bigdata2') DO %i

C:\Users\ansonlivingroom>SET DOCKER_TLS_VERIFY=1

C:\Users\ansonlivingroom>SET DOCKER_HOST=tcp://192.168.99.101:2376

C:\Users\ansonlivingroom>SET DOCKER_CERT_PATH=C:\Users\ansonlivingroom\.docker\m
achine\machines\bigdata2

C:\Users\ansonlivingroom>SET DOCKER_MACHINE_NAME=bigdata2

C:\Users\ansonlivingroom>REM Run this command to configure your shell:

C:\Users\ansonlivingroom>REM    @FOR /f "tokens=*" %i IN ('docker-machine env --
shell cmd bigdata2') DO @%i

C:\Users\ansonlivingroom>docker run -d -p 3000:3000 unclebarney/chit-chat
Unable to find image 'unclebarney/chit-chat:latest' locally
latest: Pulling from unclebarney/chit-chat
c52e3ed763ff: Pull complete
a3ed95caeb02: Pull complete
39017a32cc96: Pull complete
7d703724b60c: Pull complete
Digest: sha256:5f1cb80597837de5bea1e7e4748c9d5887b161982eee9e798ef7b2de7be251ba
Status: Downloaded newer image for unclebarney/chit-chat:latest
5532013e87a32356599486559cb83e109731f5b725f0977eedfd5ecdeedb6770

C:\Users\ansonlivingroom>docker images
REPOSITORY              TAG                 IMAGE ID            CREATED
    SIZE
unclebarney/chit-chat   latest              639e46d7a14a        8 months ago
    31.86 MB

C:\Users\ansonlivingroom>docker ps
CONTAINER ID        IMAGE                   COMMAND             CREATED
    STATUS              PORTS                    NAMES
5532013e87a3        unclebarney/chit-chat   "node index.js"     38 seconds ago
    Up 41 seconds       0.0.0.0:3000->3000/tcp   prickly_goodall

**Dependencies**

C:\Users\ansonlivingroom>scala -version
Scala code runner version 2.11.8 -- Copyright 2002-2016, LAMP/EPFL

C:\Users\ansonlivingroom>sbt sbtVersion
Java HotSpot(TM) 64-Bit Server VM warning: ignoring option MaxPermSize=256m; sup
port was removed in 8.0
[info] Set current project to ansonlivingroom (in build file:/C:/Users/ansonlivi
ngroom/)
[info] 0.13.12

C:\Users\ansonlivingroom>python --version
Python 2.7.10

C:\Users\ansonlivingroom>pip --version
pip 7.0.1 from C:\Python27\lib\site-packages (python 2.7)

*Above commands are for creating new virtualbox, below I will switch back to my existing virtualbox "bigdata" where "kafka" and "zookeeper" were previously installed*

docker-machine stop bigdata2
docker-machine start bigdata
docker-machine env --shell cmd bigdata
FOR /f "tokens=*" %i IN ('docker-machine env --shell cmd bigdata') DO %i
docker run -d -p 3000:3000 unclebarney/chit-chat
docker start kafka
docker start zookeeper


**Start Kafka Server**

C:\Users\ansonlivingroom>docker run -d -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAM
E=192.168.99.100 -e KAFKA_ADVERTISED_PORT=9092 --name kafka --link zookeeper:zoo
keeper confluent/kafka
docker: Error response from daemon: Conflict. The name "/kafka" is already in us
e by container 8e0ea68ea6d3b737e804e83bd1c1a366af4c358835d476468ce395643bb24157.
 You have to remove (or rename) that container to be able to reuse that name..
See 'docker run --help'.

C:\Users\ansonlivingroom>docker images
REPOSITORY              TAG                 IMAGE ID            CREATED
    SIZE
zookeeper               latest              ae952b380d94        3 days ago
    154.9 MB
confluent/zookeeper     latest              4a1778ad1528        4 months ago
    584.5 MB
confluent/kafka         latest              2b9ba35e1775        4 months ago
    584.5 MB
unclebarney/chit-chat   latest              639e46d7a14a        8 months ago
    31.86 MB

C:\Users\ansonlivingroom>docker ps
CONTAINER ID        IMAGE                   COMMAND                  CREATED
         STATUS              PORTS
                      NAMES
ee5d4fcf4733        unclebarney/chit-chat   "node index.js"          2 minutes a
go       Up 2 minutes        0.0.0.0:3000->3000/tcp
                      mad_blackwell
8e0ea68ea6d3        confluent/kafka         "/usr/local/bin/kafka"   11 minutes
ago      Up 11 minutes       0.0.0.0:9092->9092/tcp
                      kafka
3b287030001a        confluent/zookeeper     "/usr/local/bin/zk-do"   13 minutes
ago      Up 13 minutes       0.0.0.0:2181->2181/tcp, 0.0.0.0:2888->2888/tcp, 0.0
.0.0:3888->3888/tcp   zookeeper
06d7f6e6973b        zookeeper               "/docker-entrypoint.s"   21 minutes
ago      Up 21 minutes       2181/tcp, 2888/tcp, 3888/tcp
                      happy_shirley

**Get Kafka CLI**
Download directly (Windows)
○ https://www.apache.org/dyn/closer.cgi?path=/kafka/0.10.0.1/kafka_2.11-0.10.0.1.tgz

**Extracted to C:\ with folder name : kakfa*

C:\Users\ansonlivingroom>docker-machine ip bigdata
192.168.99.100

C:\Users\ansonlivingroom>cd..

C:\Users>cd..

C:\>cd kafka

C:\kafka>cd bin

C:\kafka\bin>cd windows

C:\kafka\bin\windows>kafka-topics.bat --create --zookeeper 192.168.99.100 --repl
ication-factor 1 --partitions 1 --topic bigdata
Created topic "bigdata".

C:\kafka\bin\windows>kafka-topics.bat --list --zookeeper 192.168.99.100
bigdata

**Get Zookeeper CLI**

Download directly (Windows)
○ http://www.apache.org/dyn/closer.cgi/zookeeper/

*File was extracted to H:\bigdata with name of "zk"*

**Look up on Zookeeper**

C:\kafka\bin\windows>H:

H:\>cd bigdata

H:\bigdata>cd zk

H:\bigdata\zk>cd bin

H:\bigdata\zk\bin>zkCli.cmd -server 192.168.99.100:2181
Connecting to 192.168.99.100:2181
2016-10-22 17:46:54,589 [myid:] - INFO  [main:Environment@100] - Client environm
ent:zookeeper.version=3.4.8--1, built on 02/06/2016 03:18 GMT
2016-10-22 17:46:54,591 [myid:] - INFO  [main:Environment@100] - Client environm
ent:host.name=livingroom-pc
2016-10-22 17:46:54,592 [myid:] - INFO  [main:Environment@100] - Client environm
ent:java.version=1.8.0_102
2016-10-22 17:46:54,593 [myid:] - INFO  [main:Environment@100] - Client environm
ent:java.vendor=Oracle Corporation
2016-10-22 17:46:54,593 [myid:] - INFO  [main:Environment@100] - Client environm
ent:java.home=C:\Java\jdk1.8.0_102\jre
2016-10-22 17:46:54,593 [myid:] - INFO  [main:Environment@100] - Client environm
ent:java.class.path=H:\bigdata\zk\bin\..\build\classes;H:\bigdata\zk\bin\..\buil
d\lib\*;H:\bigdata\zk\bin\..\zookeeper-3.4.8.jar;H:\bigdata\zk\bin\..\lib\jline-
0.9.94.jar;H:\bigdata\zk\bin\..\lib\log4j-1.2.16.jar;H:\bigdata\zk\bin\..\lib\ne
tty-3.7.0.Final.jar;H:\bigdata\zk\bin\..\lib\slf4j-api-1.6.1.jar;H:\bigdata\zk\b
in\..\lib\slf4j-log4j12-1.6.1.jar;H:\bigdata\zk\bin\..\conf
2016-10-22 17:46:54,593 [myid:] - INFO  [main:Environment@100] - Client environm
ent:java.library.path=C:\Java\jdk1.8.0_102\bin;C:\Windows\Sun\Java\bin;C:\Window
s\system32;C:\Windows;C:\ProgramData\Oracle\Java\javapath;%SCALA_HOME%\bin;%SCAL
A_HOME%\jre\bin;C:\Python27\;C:\Python27\Scripts;C:\Program Files (x86)\Intel\iC
LS Client\;C:\Program Files\Intel\iCLS Client\;C:\Windows\system32;C:\Windows;C:
\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Program Fi
les (x86)\AMD\ATI.ACE\Core-Static;C:\Program Files\Intel\Intel(R) Management Eng
ine Components\DAL;C:\Program Files (x86)\Intel\Intel(R) Management Engine Compo
nents\DAL;C:\Program Files\Intel\Intel(R) Management Engine Components\IPT;C:\Pr
ogram Files (x86)\Intel\Intel(R) Management Engine Components\IPT;C:\Program Fil
es (x86)\scala\bin;C:\Program Files (x86)\sbt\\bin;C:\Program Files\Git\cmd;C:\J
ava\jdk1.8.0_102\bin;C:\Java\jdk1.8.0_102\jre\bin;C:\Program Files\Docker Toolbo
x;.
2016-10-22 17:46:54,594 [myid:] - INFO  [main:Environment@100] - Client environm
ent:java.io.tmpdir=C:\Users\ANSONL~1\AppData\Local\Temp\
2016-10-22 17:46:54,594 [myid:] - INFO  [main:Environment@100] - Client environm
ent:java.compiler=<NA>
2016-10-22 17:46:54,594 [myid:] - INFO  [main:Environment@100] - Client environm
ent:os.name=Windows 7
2016-10-22 17:46:54,594 [myid:] - INFO  [main:Environment@100] - Client environm
ent:os.arch=amd64
2016-10-22 17:46:54,594 [myid:] - INFO  [main:Environment@100] - Client environm
ent:os.version=6.1
2016-10-22 17:46:54,595 [myid:] - INFO  [main:Environment@100] - Client environm
ent:user.name=ansonlivingroom
2016-10-22 17:46:54,595 [myid:] - INFO  [main:Environment@100] - Client environm
ent:user.home=C:\Users\ansonlivingroom
2016-10-22 17:46:54,595 [myid:] - INFO  [main:Environment@100] - Client environm
ent:user.dir=H:\bigdata\zk\bin
2016-10-22 17:46:54,596 [myid:] - INFO  [main:ZooKeeper@438] - Initiating client
 connection, connectString=192.168.99.100:2181 sessionTimeout=30000 watcher=org.
apache.zookeeper.ZooKeeperMain$MyWatcher@506c589e
Welcome to ZooKeeper!
2016-10-22 17:46:54,724 [myid:] - INFO  [main-SendThread(192.168.99.100:2181):Cl
ientCnxn$SendThread@1032] - Opening socket connection to server 192.168.99.100/1
92.168.99.100:2181. Will not attempt to authenticate using SASL (unknown error)
2016-10-22 17:46:54,725 [myid:] - INFO  [main-SendThread(192.168.99.100:2181):Cl
ientCnxn$SendThread@876] - Socket connection established to 192.168.99.100/192.1
68.99.100:2181, initiating session
JLine support is enabled
2016-10-22 17:46:54,730 [myid:] - INFO  [main-SendThread(192.168.99.100:2181):Cl
ientCnxn$SendThread@1299] - Session establishment complete on server 192.168.99.
100/192.168.99.100:2181, sessionid = 0x157eeee36b60003, negotiated timeout = 300
00

WATCHER::

WatchedEvent state:SyncConnected type:None path:null
[zk: 192.168.99.100:2181(CONNECTED) 0] ls /
[controller, controller_epoch, brokers, zookeeper, admin, isr_change_notificatio
n, consumers, config]

[zk: 192.168.99.100:2181(CONNECTED) 1] quit
Quitting...
2016-10-22 17:49:19,886 [myid:] - INFO  [main:ZooKeeper@684] - Session: 0x157eee
e36b60003 closed
2016-10-22 17:49:19,890 [myid:] - INFO  [main-EventThread:ClientCnxn$EventThread
@519] - EventThread shut down for session: 0x157eeee36b60003

**Produce Messages**

H:\bigdata\zk\bin>c:

C:\kafka\bin\windows>kafka-console-producer.bat --broker-list 192.168.99.100:909
2 --topic bigdata
abadfadfafa
adhfuifyuj
fhjfdhj
123456

*In another cmd window*

C:\Users\ansonlivingroom>cd..

C:\Users>cd..

C:\>cd kafka

C:\kafka>cd bin

C:\kafka\bin>cd windows

C:\kafka\bin\windows>kafka-console-consumer.bat --zookeeper 192.168.99.100:2181
--topic bigdata
abadfadfafa
adhfuifyuj
fhjfdhj
123456

C:\kafka\bin\windows>kafka-console-consumer.bat --zookeeper 192.168.99.100:2181
--topic bigdata --from-beginning
abadfadfafa
adhfuifyuj
fhjfdhj
123456

**Look Into Kafka Broker**

C:\kafka\bin\windows>docker exec -it kafka bash
confluent@8e0ea68ea6d3:/$ cd /var/lib/kafka
confluent@8e0ea68ea6d3:/var/lib/kafka$ ls
bigdata-0                  recovery-point-offset-checkpoint
cleaner-offset-checkpoint  replication-offset-checkpoint
meta.properties

**Browse Znode Data**

C:\kafka\bin\windows>H:

H:\bigdata\zk\bin>zkCli.cmd -server 192.168.99.100:2181
Connecting to 192.168.99.100:2181
2016-10-22 18:02:10,613 [myid:] - INFO  [main:Environment@100] - Client environm
ent:zookeeper.version=3.4.8--1, built on 02/06/2016 03:18 GMT
2016-10-22 18:02:10,615 [myid:] - INFO  [main:Environment@100] - Client environm
ent:host.name=livingroom-pc
2016-10-22 18:02:10,615 [myid:] - INFO  [main:Environment@100] - Client environm
ent:java.version=1.8.0_102
2016-10-22 18:02:10,616 [myid:] - INFO  [main:Environment@100] - Client environm
ent:java.vendor=Oracle Corporation
2016-10-22 18:02:10,616 [myid:] - INFO  [main:Environment@100] - Client environm
ent:java.home=C:\Java\jdk1.8.0_102\jre
2016-10-22 18:02:10,616 [myid:] - INFO  [main:Environment@100] - Client environm
ent:java.class.path=H:\bigdata\zk\bin\..\build\classes;H:\bigdata\zk\bin\..\buil
d\lib\*;H:\bigdata\zk\bin\..\zookeeper-3.4.8.jar;H:\bigdata\zk\bin\..\lib\jline-
0.9.94.jar;H:\bigdata\zk\bin\..\lib\log4j-1.2.16.jar;H:\bigdata\zk\bin\..\lib\ne
tty-3.7.0.Final.jar;H:\bigdata\zk\bin\..\lib\slf4j-api-1.6.1.jar;H:\bigdata\zk\b
in\..\lib\slf4j-log4j12-1.6.1.jar;H:\bigdata\zk\bin\..\conf
2016-10-22 18:02:10,616 [myid:] - INFO  [main:Environment@100] - Client environm
ent:java.library.path=C:\Java\jdk1.8.0_102\bin;C:\Windows\Sun\Java\bin;C:\Window
s\system32;C:\Windows;C:\ProgramData\Oracle\Java\javapath;%SCALA_HOME%\bin;%SCAL
A_HOME%\jre\bin;C:\Python27\;C:\Python27\Scripts;C:\Program Files (x86)\Intel\iC
LS Client\;C:\Program Files\Intel\iCLS Client\;C:\Windows\system32;C:\Windows;C:
\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Program Fi
les (x86)\AMD\ATI.ACE\Core-Static;C:\Program Files\Intel\Intel(R) Management Eng
ine Components\DAL;C:\Program Files (x86)\Intel\Intel(R) Management Engine Compo
nents\DAL;C:\Program Files\Intel\Intel(R) Management Engine Components\IPT;C:\Pr
ogram Files (x86)\Intel\Intel(R) Management Engine Components\IPT;C:\Program Fil
es (x86)\scala\bin;C:\Program Files (x86)\sbt\\bin;C:\Program Files\Git\cmd;C:\J
ava\jdk1.8.0_102\bin;C:\Java\jdk1.8.0_102\jre\bin;C:\Program Files\Docker Toolbo
x;.
2016-10-22 18:02:10,617 [myid:] - INFO  [main:Environment@100] - Client environm
ent:java.io.tmpdir=C:\Users\ANSONL~1\AppData\Local\Temp\
2016-10-22 18:02:10,617 [myid:] - INFO  [main:Environment@100] - Client environm
ent:java.compiler=<NA>
2016-10-22 18:02:10,617 [myid:] - INFO  [main:Environment@100] - Client environm
ent:os.name=Windows 7
2016-10-22 18:02:10,617 [myid:] - INFO  [main:Environment@100] - Client environm
ent:os.arch=amd64
2016-10-22 18:02:10,617 [myid:] - INFO  [main:Environment@100] - Client environm
ent:os.version=6.1
2016-10-22 18:02:10,617 [myid:] - INFO  [main:Environment@100] - Client environm
ent:user.name=ansonlivingroom
2016-10-22 18:02:10,617 [myid:] - INFO  [main:Environment@100] - Client environm
ent:user.home=C:\Users\ansonlivingroom
2016-10-22 18:02:10,617 [myid:] - INFO  [main:Environment@100] - Client environm
ent:user.dir=H:\bigdata\zk\bin
2016-10-22 18:02:10,618 [myid:] - INFO  [main:ZooKeeper@438] - Initiating client
 connection, connectString=192.168.99.100:2181 sessionTimeout=30000 watcher=org.
apache.zookeeper.ZooKeeperMain$MyWatcher@506c589e
Welcome to ZooKeeper!
2016-10-22 18:02:10,733 [myid:] - INFO  [main-SendThread(192.168.99.100:2181):Cl
ientCnxn$SendThread@1032] - Opening socket connection to server 192.168.99.100/1
92.168.99.100:2181. Will not attempt to authenticate using SASL (unknown error)
2016-10-22 18:02:10,734 [myid:] - INFO  [main-SendThread(192.168.99.100:2181):Cl
ientCnxn$SendThread@876] - Socket connection established to 192.168.99.100/192.1
68.99.100:2181, initiating session
JLine support is enabled
2016-10-22 18:02:10,739 [myid:] - INFO  [main-SendThread(192.168.99.100:2181):Cl
ientCnxn$SendThread@1299] - Session establishment complete on server 192.168.99.
100/192.168.99.100:2181, sessionid = 0x157eeee36b6000b, negotiated timeout = 300
00

WATCHER::

WatchedEvent state:SyncConnected type:None path:null
[zk: 192.168.99.100:2181(CONNECTED) 0] ls /
[controller, controller_epoch, brokers, zookeeper, admin, isr_change_notificatio
n, consumers, config]
[zk: 192.168.99.100:2181(CONNECTED) 1] ls /zookeeper
[quota]
[zk: 192.168.99.100:2181(CONNECTED) 2] get /zookeeper/quota

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

**Create Znode Data**

[zk: 192.168.99.100:2181(CONNECTED) 3] create /workers "bittiger"
Created /workers
[zk: 192.168.99.100:2181(CONNECTED) 4] ls /
[controller, controller_epoch, brokers, zookeeper, admin, isr_change_notificatio
n, consumers, config, workers]
[zk: 192.168.99.100:2181(CONNECTED) 5] ls /workers
[]
[zk: 192.168.99.100:2181(CONNECTED) 6] get /workers
bittiger
cZxid = 0x57
ctime = Sat Oct 22 18:04:01 PDT 2016
mZxid = 0x57
mtime = Sat Oct 22 18:04:01 PDT 2016
pZxid = 0x57
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 8
numChildren = 0

**Delete Znode Data**

[zk: 192.168.99.100:2181(CONNECTED) 7] delete /workers
[zk: 192.168.99.100:2181(CONNECTED) 8] ls /
[controller, controller_epoch, brokers, zookeeper, admin, isr_change_notificatio
n, consumers, config]
[zk: 192.168.99.100:2181(CONNECTED) 9] ls /workers
Node does not exist: /workers
[zk: 192.168.99.100:2181(CONNECTED) 10] get /workers
Node does not exist: /workers
[zk: 192.168.99.100:2181(CONNECTED) 11]

**Create Ephemeral Znode Data**

[zk: 192.168.99.100:2181(CONNECTED) 11] create -e /workers "unclebarney"
Created /workers
[zk: 192.168.99.100:2181(CONNECTED) 12] ls /
[controller, controller_epoch, brokers, zookeeper, admin, isr_change_notificatio
n, consumers, config, workers]
[zk: 192.168.99.100:2181(CONNECTED) 13] ls /workers
[]
[zk: 192.168.99.100:2181(CONNECTED) 14] get /workers
unclebarney
cZxid = 0x59
ctime = Sat Oct 22 18:08:06 PDT 2016
mZxid = 0x59
mtime = Sat Oct 22 18:08:06 PDT 2016
pZxid = 0x59
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x157eeee36b6000b
dataLength = 11
numChildren = 0
[zk: 192.168.99.100:2181(CONNECTED) 15]

**Watcher**

[zk: 192.168.99.100:2181(CONNECTED) 15] get /workers true
unclebarney
cZxid = 0x59
ctime = Sat Oct 22 18:08:06 PDT 2016
mZxid = 0x59
mtime = Sat Oct 22 18:08:06 PDT 2016
pZxid = 0x59
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x157eeee36b6000b
dataLength = 11
numChildren = 0
[zk: 192.168.99.100:2181(CONNECTED) 16]


















