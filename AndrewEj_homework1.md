```
zkCli.cmd -server 192.168.99.100:2181
ls /

WatchedEvent state:SyncConnected type:None path:null
[zk: 192.168.99.100:2181(CONNECTED) 0] ls
[zk: 192.168.99.100:2181(CONNECTED) 1] ls /
[controller_epoch, brokers, zookeeper, admin, isr_change_notification, consumers, config]
[zk: 192.168.99.100:2181(CONNECTED) 2]
```

```
C:\Users\enjio>kafka-console-producer.bat --broker-list 192.168.99.100:9092 --topic bigdata
what is up


C:\Users\enjio>kafka-console-consumer.bat --zookeeper 192.168.99.100:2181 --topic bigdata
what is up


```

```
C:\Users\enjio>kafka-console-consumer.bat --zookeeper 192.168.99.100:2181 --topic bigdata --from-beginning

exit
what is up
whhello
what is up
lol
hello boy
lol
hello
```

```
confluent@3afac736e93a:/$ cd var/lib/kafka
confluent@3afac736e93a:/var/lib/kafka$ ls

bigdata-0                  meta.properties                   replication-offset-checkpoint
cleaner-offset-checkpoint  recovery-point-offset-checkpoint  stock-ananlyzer-0
```

```
[zk: 192.168.99.100:2181(CONNECTED) 0] ls /zookeeper
[quota]

[zk: 192.168.99.100:2181(CONNECTED) 3] get /zookeeper/quota

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

```
[zk: 192.168.99.100:2181(CONNECTED) 4] create /workers "bittiger"
Created /workers
[zk: 192.168.99.100:2181(CONNECTED) 5] ls /
[controller_epoch, controller, brokers, zookeeper, admin, isr_change_notification, consumers, config, workers]
[zk: 192.168.99.100:2181(CONNECTED) 6] ls /workers
[]
[zk: 192.168.99.100:2181(CONNECTED) 7] get /workers
bittiger
cZxid = 0xc9
ctime = Thu Oct 20 11:56:15 PDT 2016
mZxid = 0xc9
mtime = Thu Oct 20 11:56:15 PDT 2016
pZxid = 0xc9
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 8
numChildren = 0
[zk: 192.168.99.100:2181(CONNECTED) 8]
```

```
[zk: 192.168.99.100:2181(CONNECTED) 8] delete /workers
[zk: 192.168.99.100:2181(CONNECTED) 9] ls /
[controller_epoch, controller, brokers, zookeeper, admin, isr_change_notification, consumers, config]
[zk: 192.168.99.100:2181(CONNECTED) 10] ls /workers
Node does not exist: /workers
[zk: 192.168.99.100:2181(CONNECTED) 11] get /workers
Node does not exist: /workers
```

```
[controller_epoch, controller, brokers, zookeeper, admin, isr_change_notification, consumers, config, workers]
[zk: 192.168.99.100:2181(CONNECTED) 14] ls /workers
[]
[zk: 192.168.99.100:2181(CONNECTED) 15] get /workers
unclebarney
cZxid = 0xcb
ctime = Thu Oct 20 11:58:47 PDT 2016
mZxid = 0xcb
mtime = Thu Oct 20 11:58:47 PDT 2016
pZxid = 0xcb
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x157e34961f20011
dataLength = 11
numChildren = 0
```

```
[zk: 192.168.99.100:2181(CONNECTED) 26] get /workers true
uncle
cZxid = 0xce
ctime = Thu Oct 20 12:02:59 PDT 2016
mZxid = 0xce
mtime = Thu Oct 20 12:02:59 PDT 2016
pZxid = 0xce
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x157e34961f20011
dataLength = 5
numChildren = 0
```