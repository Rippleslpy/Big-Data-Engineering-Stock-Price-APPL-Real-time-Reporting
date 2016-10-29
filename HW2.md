* __./cqlsh `docker-machine ip bigdata` 9042__
> onnected to Test Cluster at 192.168.99.102:9042.
[cqlsh 5.0.1 | Cassandra 3.7 | CQL spec 3.4.2 | Native protocol v4]
Use HELP for help.
* __CREATE KEYSPACE "stock" WITH replication = {'class': 'SimpleStrategy', 'replication_factor':1} AND durable_writes = 'true';__
* __USE stock;__
> cqlsh:stock>
* __DESCRIBE KEYSPACE;__
* > CREATE KEYSPACE stock WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}  AND durable_writes = true;
* __CREATE TABLE user ( first_name text, last_name text, PRIMARY KEY (first_name));__
* __DESCRIBE TABLE user;__
> CREATE TABLE stock.user (
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
* __INSERT INTO user (first_name, last_name) VALUES ('uncle', 'barney');__
* __SELECT COUNT (*) FROM USER;__
> count -------
1
(1 rows)

* __SELECT * FROM user WHERE first_name='gongda';__
> first_name | last_name
------------+-----------
     gongda |        ge
* __SELECT * FROM user WHERE last_name='ge';__
> InvalidRequest: code=2200 [Invalid query] message="Cannot execute this query as it might involve data filtering and thus may have unpredictable performance. If you want to execute this query despite the performance unpredictability, use ALLOW FILTERING"

* look into cassandra node
* __docker exec -it cassandra bash__
> root@51f4517905ad:/#
* __cd /var/lib/cassandra__
* __ls__
> commitlog  data  hints	saved_caches
* __DELETE last_name FROM user WHERE first_name='uncle';__
> 首先要进数据库, 然后use stock
* __DELETE FROM user WHERE first_name='uncle';__
* __TRUNCATE user;__
* __DROP TABLE user;__