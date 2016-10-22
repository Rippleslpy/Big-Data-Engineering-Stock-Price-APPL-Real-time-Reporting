### Homework 1

- List existing docker-machine by
  ```
  docker-machine ls
  ```
  shows
  ```
  NAME      ACTIVE   DRIVER       STATE     URL   SWARM   DOCKER    ERRORS
  
  bigdata   -        virtualbox   Stopped                 Unknown
  ```
  
- Start the `bigdata` docker-machine by
  ```
  docker-machine start bigdata
  ```
  shows
  ```
  Starting "bigdata"...
  (bigdata) Check network to re-create if needed...
  (bigdata) Waiting for an IP...
  Machine "bigdata" was started.
  Waiting for SSH to be available...
  Detecting the provisioner...
  Started machines may have new IP addresses. You may need to re-run the `docker-machine env` command.
  ```

- Show the `bigdata` docker-machine ip address by
  ```
  docker-machine ip bigdata
  ```
  shows
  ```
  192.168.99.100
  ```

- Create an isolated environment for the `bigdata` docker-machine by
  ```
  eval $(docker-machine env bigdata)
  ```
  shows
  ```
  
  ```

- List all images in the `bigdata` docker-machine by
  ```
  docker images
  ```
  shows
  ```
  REPOSITORY            TAG                 IMAGE ID            CREATED             SIZE
  confluent/zookeeper   latest              4a1778ad1528        4 months ago        584.5 MB
  confluent/kafka       latest              2b9ba35e1775        4 months ago        584.5 MB
  ```

- List all containers in the `bigdata` docker-machine by
  ```
  docker ps
  ```
  shows
  ```
  CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
  ```

