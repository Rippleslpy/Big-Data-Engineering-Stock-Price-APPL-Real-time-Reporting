# CS202-setups on Macbook 
## Week 0-setups
* install homebrew[http://brew.sh/]
* install scala (might need java first)
* brew install sbt

### Play with docker
* install docker machine with docker toolbox
* `docker-machine create --driver virtualbox --virtualbox-cpu-count 2 --virtualbox-memory 2048
bigdata` creat a machine called __bigdata__ 
* if created before, `eval $(docker-machine env bigdata)` each time use a new terminal need to run this, which connect the docker and server
* `docker run -d -p 3000:3000 unclebarney/chit-chat` run a webserver []pulling image from the web and 

