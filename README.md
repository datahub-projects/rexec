# Introduction

`rexec` is an open-source tool enabling developers to run their software remotely - on any sized virtual machine - without any change to their existing development process.

We currently support Amazon and Google cloud services, with the intent to add more over time.

# Dependencies

* Python3 
* Docker version 19 or higher
* A folder/project with a working `Dockerfile`

# Installation 

`pip install -e git+ssh://git@github.com/datahub-projects/rexec#egg=rexec`

# Configuration

Our configuration is currently manual. You will need to do the following: 

`mkdir -p ~/.rexec` # create config folder if it the folder does not exist

Edit `~/.rexec/config.py` with:

```
access="<your-aws-access-key>"
secret="<your-aws-secret>"
region="us-west-2"
```

# Run `rexec` tests

```
% cd $(dirname $(which python))/../src/rexec/tests/
% rexec python3 test_script.py 
ARGV: ['python3', 'test_script.py']
REXARGS: []
CMDARGS: ['python3', 'test_script.py']
ARGS: Namespace(access=None, cloudmap='', command=None, delay=0, dockerfile='Dockerfile', gpus=None, image=None, list_servers=False, local=False, p=None, pubkey=None, region=None, rexecuser=None, secret=None, shutdown=900, size=None, sshuser='ubuntu', stop_instance_by_url=None, terminate_servers=False, url=None, uuid=None, version=False)
Rexec username: kevincollins
Waiting for sshd
['ssh', '-o StrictHostKeyChecking=no', 'ubuntu@54.71.26.156', 'echo', "'sshd responding'"]
SSH returns -->sshd responding
|True<--
['ssh', '-o StrictHostKeyChecking=no', '-NL', '2376:/var/run/docker.sock', 'ubuntu@54.71.26.156']
['docker', '-H localhost:2376', 'ps', '--format', '{{json .}}']
Killing shutdown processes: ['1dd30be970ad']
docker -H localhost:2376 stop 1dd30be970ad
1dd30be970ad
Removing topmost layer
['docker', '-H localhost:2376', 'rmi', '--no-prune', 'rexec_image']
Untagged: rexec_image:latest
Deleted: sha256:1e42c04579adc4c78ceb98a4b0f684fe94c638a884ec64e56b7ee19c9a25c187

rexec: name rexec_kevincollins size t2.small image ami-0ba3ac9cd67195659 url 54.71.26.156
rsync -vrltzu /Users/kevincollins/datahub/venv.rexec/src/rexec/tests/* ubuntu@54.71.26.156:/home/ubuntu/_REXEC_datahub_venv.rexec_src_rexec_tests/
building file list ... done

sent 189 bytes  received 20 bytes  139.33 bytes/sec
total size is 1286  speedup is 6.15
docker -H localhost:2376 build . --file Dockerfile -t rexec_image
Sending build context to Docker daemon  3.072kB
Step 1/6 : FROM ubuntu:20.04
 ---> adafef2e596e
Step 2/6 : RUN apt-get update && apt-get install -y python3 python3-pip nano fish git curl rclone fuse
 ---> Using cache
 ---> 923b963b32cd
Step 3/6 : RUN pip3 install git+https://github.com/datahub-projects/rexec#egg=rexec
 ---> Using cache
 ---> dd8c13538bf5
Step 4/6 : RUN adduser --disabled-password --gecos '' ubuntu
 ---> Using cache
 ---> 3798e43c2ab5
Step 5/6 : WORKDIR /home/rexec
 ---> Using cache
 ---> 8c28cb61fc67
Step 6/6 : CMD ["/bin/bash"]
 ---> Running in b0ab00a5690c
Removing intermediate container b0ab00a5690c
 ---> a85335744c23
Successfully built a85335744c23
Successfully tagged rexec_image:latest
docker -H localhost:2376 run   --rm -it -v /home/ubuntu/_REXEC_datahub_venv.rexec_src_rexec_tests:/home/rexec  rexec_image python3 test_script.py


---------------------OUTPUT-----------------------
test_script running, args: []
----------------------END-------------------------


rsync -vrltzu 'ubuntu@54.71.26.156:/home/ubuntu/_REXEC_datahub_venv.rexec_src_rexec_tests/*' /Users/kevincollins/datahub/venv.rexec/src/rexec/tests/
receiving file list ... done
foo

sent 44 bytes  received 249 bytes  195.33 bytes/sec
total size is 1287  speedup is 4.39
Scheduling shutdown of VM at 54.71.26.156 for 900 seconds from now
docker -H localhost:2376 run --rm -d rexec_image rexec --stop_instance_by_url 54...
Shutdown process container ID:
00623d9646b3085a6782ad5c440fcd5433084d2e7904c5e3b5ed52c6ba7b0982
DONE




