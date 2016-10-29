```
cqlsh> USE stock;
cqlsh:stock> DESCRIBE KEYSPACE;

CREATE KEYSPACE stock WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}  AND durable_writes = true;
```



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



```
cqlsh:stock> INSERT INTO user (first_name,last_name) VALUES ('uncle','barney');
cqlsh:stock> SELECT COUNT (*) FROM USER;

 count
-------
     1

(1 rows)

Warnings :
Aggregation query used without partition key

cqlsh:stock> SELECT * FROM user WHERE first_name='uncle';

 first_name | last_name
------------+-----------
      uncle |    barney

(1 rows)

cqlsh:stock> SELECT * FROM user WHERE last_name='barney';
InvalidRequest: Error from server: code=2200 [Invalid query] message="Cannot execute this query as it might involve data filtering and thus may have unpredictable performance. If you want to execute this query despite the performance unpredictability, use ALLOW FILTERING"

```



```
root@2b112e18d3f6:/var/lib/cassandra# ls
commitlog  data  hints  saved_caches
root@2b112e18d3f6:/var/lib/cassandra#
```



```

```