# CS202-1603

## Week 0 - setup notes

* download homebrew
* install scala: `homebrew install scala`, might need to install java first
* brew install sbt
* install docker with docker toolbox

## Play with docker
* install docker machine with docker toolbox
* `docker-machine create --driver virtualbox --virtualbox-cpu-count 2 --virtualbox-memory 2048
bigdata` creat a machine called __bigdata__ 
* if created before, `eval $(docker-machine env bigdata)` each time use a new terminal need to run this, which connect the docker and server
* `docker run -d -p 3000:3000 unclebarney/chit-chat` run a webserver []pulling image from the web and