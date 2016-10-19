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
> docker run -d -p 2181:2181 -p 2888:2888 -p 3888:3888 --name zookeeper confluent/zookeeper

```
>>==首次执行时：==<<
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
>>==第二次及以后执行时：==<<
74f2770cd5e66178dfe1598d37aeb2624f4e2a483b42a54bd9fef710e8250314
```
>$ docker images
```
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
hello-world             latest              c54a2cc56cbb        3 months ago        1.848 kB
confluent/zookeeper     latest              4a1778ad1528        4 months ago        584.5 MB
confluent/kafka         latest              2b9ba35e1775        4 months ago        584.5 MB
unclebarney/chit-chat   latest              639e46d7a14a        8 months ago        31.86 MB
```
>$ docker ps
```
CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                                                                    NAMES
74f2770cd5e6        confluent/zookeeper   "/usr/local/bin/zk-do"   2 minutes ago       Up 2 minutes        0.0.0.0:2181->2181/tcp, 0.0.0.0:2888->2888/tcp, 0.0.0.0:3888->3888/tcp   zookeeper
```
