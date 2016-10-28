
cmd input:
```
cqlsh> CREATE KEYSPACE "stock" WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1} AND durable_writes = 'true';
```
cmd output:
```
AlreadyExists: Keyspace 'stock' already exists
```
cmd input:
```
cqlsh> USE stock ;
cqlsh:stock> DESCRIBE KEYSPACE;
```
cmd output:
```
CREATE KEYSPACE stock WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}  AND durable_writes = true;
```
cmd input:
```
cqlsh:stock> CREATE TABLE user (first_name text, last_name text, Primary KEY (first_name)) ;
cqlsh:stock> DESCRIBE TABLE user;
```
cmd output:
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
cmd input:
```
cqlsh:stock> INSERT INTO user (first_name , last_name ) VALUES ( 'boxuan', 'zhang') ;
cqlsh:stock> SELECT count (*) FROM user ;
```
cmd output:
```
 count
-------
     1

(1 rows)

Warnings :
Aggregation query used without partition key
```
cmd input:
```
cqlsh:stock> SELECT * FROM user WHERE first_name='boxuan';
```
cmd output:
```
 first_name | last_name
------------+-----------
     boxuan |     zhang

(1 rows)
```
cmd input:
```
cqlsh:stock> SELECT * FROM user WHERE last_name='zhang';
```
cmd output:
```
InvalidRequest: code=2200 [Invalid query] message="Cannot execute this query as it might involve data filtering and thus may have unpredictable performance. If you want to execute this query despite the performance unpredictability, use ALLOW FILTERING"
```
cmd input:
```
C:\Users\Think>docker exec -it cassandra bash
root@bd5ef4f55c31:/# cd /var/lib/cassandra/
root@bd5ef4f55c31:/var/lib/cassandra# ls
```
cmd output:
```
commitlog  data  hints  saved_caches
```
cmd input:
```
cqlsh:stock> DELETE last_name FROM user WHERE first_name='boxuan';
cqlsh:stock> SELECT * FROM user WHERE first_name='boxuan';
```
cmd output:
```
 first_name | last_name
------------+-----------
     boxuan |      null

(1 rows)
```
cmd input:
```
cqlsh:stock> DELETE FROM user WHERE first_name='boxuan';
cqlsh:stock> SELECT * FROM user WHERE first_name='boxuan';
```
cmd output:
```
 first_name | last_name
------------+-----------

(0 rows)
```
cmd input:
```
cqlsh:stock> TRUNCATE user;
cqlsh:stock> DROP TABLE user;
cqlsh:stock> DESCRIBE TABLE user;
```
cmd output:
```
Column family 'user' not found
```