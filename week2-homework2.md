# Play with Apache Cassandra
## Start Cassandra Server
> $ docker run -d -p 7199:7199 -p 9042:9042 -p 9160:9160 -p 7001:7001 --name cassandra cassandra:3.7
```
Unable to find image 'cassandra:3.7' locally
3.7: Pulling from library/cassandra
6a5a5368e0c2: Pull complete
97e4c6575710: Pull complete
d8288e3be5a2: Pull complete
d111f542073e: Pull complete
2549cfb76ce6: Pull complete
a375ee20c601: Pull complete
2e678e60bfc4: Pull complete
c2d5e7ed7dfc: Pull complete
21015df69ccb: Pull complete
a5b3a5d43f72: Pull complete
Digest: sha256:bce66127d99ff99020f2c5370b585744c851df7a21b42e7843195a0b143b94e7
Status: Downloaded newer image for cassandra:3.7
9f1286f798e9565e0e64b973f3fe8541cf50933461fdd9188b51dd4456294878
```
> $ docker images
```
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
cassandra               3.7                 25427f353269        3 weeks ago         382.4 MB
hello-world             latest              c54a2cc56cbb        3 months ago        1.848 kB
confluent/zookeeper     latest              4a1778ad1528        4 months ago        584.5 MB
confluent/kafka         latest              2b9ba35e1775        4 months ago        584.5 MB
unclebarney/chit-chat   latest              639e46d7a14a        8 months ago        31.86 MB
```
> $ docker ps
```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                                                                                      NAMES
9f1286f798e9        cassandra:3.7       "/docker-entrypoint.s"   10 seconds ago      Up 12 seconds       0.0.0.0:7001->7001/tcp, 0.0.0.0:7199->7199/tcp, 0.0.0.0:9042->9042/tcp, 7000/tcp, 0.0.0.0:9160->9160/tcp   cassandra
```

## Start Cassandra CLI
> $ cd cassandra/bin<br/>
> $ ./cqlsh \`docker-machine ip bigdata\` 9042
```
Connected to Test Cluster at 192.168.99.100:9042.
[cqlsh 5.0.1 | Cassandra 3.7 | CQL spec 3.4.2 | Native protocol v4]
Use HELP for help.
cqlsh>
```

## Create Keyspace
> cqlsh> CREATE KEYSPACE "stock" WITH replication = {'class':'SimpleStrategy','replication_factor':1} AND durable_writes = 'true';
> cqlsh> USE stock;<br/>
> cqlsh:stock> DESCRIBE KEYSPACE;
```
CREATE KEYSPACE stock WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}  AND durable_writes = true;
```

## Create Table
> cqlsh:stock> CREATE TABLE user (first_name text, last_name text, PRIMARY KEY (first_name));<br/>
> cqlsh:stock> DESCRIBE TABLE user;
```
CREATE TABLE stock.user (
    first_name text PRIMARY KEY,
    last_name text
) WITH bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND dclocal_read_repair_chance = 0.1
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair_chance = 0.0
    AND speculative_retry = '99PERCENTILE';
```

## Insert Data
> cqlsh:stock> INSERT INTO user (first_name, last_name) VALUES ('uncle', 'barney');

## Query Data
> cqlsh:stock> SELECT COUNT(*) FROM USER;
```
 count
-------
     1
<br/>
(1 rows)
<br/>
Warnings :
Aggregation query used without partition key
```
> cqlsh:stock> SELECT * FROM user WHERE first_name='uncle';
```
 first_name | last_name
------------+-----------
      uncle |    barney
<br/>
(1 rows)
```
> cqlsh:stock> SELECT * FROM user WHERE last_name='barney';
```
InvalidRequest: code=2200 [Invalid query] message="Cannot execute this query as it might involve data filtering and thus may have unpredictable performance. If you want to execute this query despite the performance unpredictability, use ALLOW FILTERING"
```

## Look Into Cassandra Node
> $ docker exec -it cassandra bash
```
root@9f1286f798e9:/#
```
> root@9f1286f798e9:/# cd /var/lib/cassandra/ <br/>
> root@9f1286f798e9:/var/lib/cassandra# ls
```
commitlog  data  hints  saved_caches
```

## Delete Data
> cqlsh:stock> DELETE last_name FROM user WHERE first_name='uncle'; <br/>
> cqlsh:stock> select * from user;
```
 first_name | last_name
-------------+-----------
       uncle |      null
<br/>
(1 rows)
```
> cqlsh:stock> DELETE FROM user WHERE first_name='uncle'; <br/>
> cqlsh:stock> select * from user;
```
 first_name | last_name
------------+-----------
<br/>
(0 rows)
```

## Remove Table
> cqlsh:stock> TRUNCATE user;<br/>
> cqlsh:stock> DROP TABLE user;<br/>
> DESC TABLES;
```
<empty>
``` 