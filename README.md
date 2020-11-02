# Introduction

`rexec` lets you run your software remotely - on any sized virtual machine - without any change to your existing development process, as long as you have a working Dockerfile.

We currently support Amazon and Google cloud services and will be adding more.

# Dependencies

* Python3 
* Docker version 19 or higher
* A folder/project with a working `Dockerfile`

# Installation 

`git clone https://github.com/datahub-projects/rexec.git && cd rexec && pip install -r requirements.txt`

or 

`pip install -e git+ssh://git@github.com/datahub-projects/rexec#egg=rexec`

# Configuring Cloud Service Providers for Ephemeral Virtual Machines 

Our configuration is currently manual. You will need to do the following: 

`mkdir -p ~/.rexec` # create config folder if it the folder does not exist

Edit `~/.rexec/config.yml` with:

```
default: myaws

myaws:
  provider: EC2
  access: <Amazon AWS Access Key>
  secret: <Amazon AWS Access Secret>
  region: us-west-2
  default_image: ami-0ba3ac9cd67195659
  default_size: t2.small
  default_gpu_image: ami-038b493084f00b948 
  default_gpu_size: g4dn.xlarge

mygoogle:
  provider: GCE
  access: <Google Cloud Account Key>
  secret: ~/.rexec/<Google Cloud Account Private Key Filename>.json
  region: us-west1-b
  project: <Google Cloud Project ID>
  default_image: rexec-nogpu
```

# Configuring Cloud Service Providers for Cloud Storage Access

Using cloud storage is optional but can provide faster performance, better protection of your data and easier sharing of work than using local files.

We use [rclone](https://rclone.org/) for configuring cloud storage providers. After configuring a provider with [rclone config](https://rclone.org/commands/rclone_config/), copy the `rclone.conf` to the ~/.rexec folder and then you can read and write from this drive by using `--cloudmap <rclone-provider>:<local-folder>` syntax.

For example, if you have a provider named `googledrive`, you can list the files from an ephemeral VM with this command => `rexec --cloudmap googledrive:googledrive ls googledrive`

TODO: provide an example with timing where using cloud storage provides a large performance improvement.

# Run `rexec` tests

```
% cd tests
% ../bin/rexec python3 test_script.py 
ARGV: ['python3', 'test_script.py']
REXARGS: []
CMDARGS: ['python3', 'test_script.py']
ARGS: Namespace(access=None, command=None, delay=0, dockerfile='Dockerfile', gpus=None, image=None, list_servers=False, local=False, p=None, pubkey=None, region=None, rexecuser=None, secret=None, shutdown=900, size=None, sshuser='ubuntu', stop_instance_by_url=None, terminate_servers=False, url=None, uuid=None)
Rexec username: kevincollins
Waiting for sshd
['ssh', '-o StrictHostKeyChecking=no', 'ubuntu@34.221.2.128', 'echo', "'sshd responding'"]
SSH returns -->sshd responding
|True<--
['ssh', '-o StrictHostKeyChecking=no', '-NL', '2376:/var/run/docker.sock', 'ubuntu@34.221.2.128']
['docker', '-H localhost:2376', 'ps', '--format', '{{json .}}']
Removing topmost layer
['docker', '-H localhost:2376', 'rmi', '--no-prune', 'rexec_image']
Error: No such image: rexec_image

rexec: name rexec_kevincollins size t2.small image ami-0ba3ac9cd67195659 url 34.221.2.128
rsync -vrltzu /Users/kevincollins/datahub/rexec/tests/* ubuntu@34.221.2.128:/home/ubuntu/_REXEC_datahub_rexec_tests/
building file list ... done
created directory /home/ubuntu/_REXEC_datahub_rexec_tests
Dockerfile
foo
longtest.py
test_local
test_remote
test_remote2
test_remote3
test_script.py
data/
data/touched_by_fire

sent 1498 bytes  received 224 bytes  688.80 bytes/sec
total size is 1273  speedup is 0.74
docker -H localhost:2376 build . --file Dockerfile -t rexec_image
Sending build context to Docker daemon  3.072kB
Step 1/6 : FROM ubuntu:20.04
 ---> adafef2e596e
Step 2/6 : RUN apt-get update && apt-get install -y python3 python3-pip nano fish git curl
 ---> Using cache
 ---> b1a602f9a279
Step 3/6 : RUN pip3 install git+https://github.com/datahub-projects/rexec#egg=rexec
 ---> Using cache
 ---> 1e59e57c8cfe
Step 4/6 : RUN adduser --disabled-password --gecos '' ubuntu
 ---> Using cache
 ---> 6fb6472103f2
Step 5/6 : WORKDIR /home/rexec
 ---> Using cache
 ---> 178b736f8ae9
Step 6/6 : CMD ["/bin/bash"]
 ---> Running in 7039377cb232
Removing intermediate container 7039377cb232
 ---> 44c0f2e4825f
Successfully built 44c0f2e4825f
Successfully tagged rexec_image:latest
docker -H localhost:2376 run   --rm -it -v /home/ubuntu/_REXEC_datahub_rexec_tests:/home/rexec rexec_image python3 test_script.py


---------------------OUTPUT-----------------------
test_script running, args: []
----------------------END-------------------------


rsync -vrltzu 'ubuntu@34.221.2.128:/home/ubuntu/_REXEC_datahub_rexec_tests/*' /Users/kevincollins/datahub/rexec/tests/
receiving file list ... done
foo

sent 44 bytes  received 248 bytes  116.80 bytes/sec
total size is 1274  speedup is 4.36
Scheduling shutdown of VM at 34.221.2.128 for 900 seconds from now
docker -H localhost:2376 run --rm -d rexec_image rexec --stop_instance_by_url 34...
Shutdown process container ID:
b518a1110e7f9f6607166637f012d36c96b93c3d38be3f0c2c50bcc6302f11ce
DONE
```

# Run Examples

TODO - add GPU-enabled machine learning examples! 


