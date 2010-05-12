#!/usr/bin/env python
from starcluster import static

config_template = """
####################################
## StarCluster Configuration File ##
####################################
[global]
# configure the default cluster template to use when starting a cluster
DEFAULT_TEMPLATE=smallcluster
# enable experimental features for this release
ENABLE_EXPERIMENTAL=False

# This is the AWS credentials section.
# These settings apply to all clusters
[aws info]
#replace these with your AWS keys
AWS_ACCESS_KEY_ID = #your_aws_access_key_id
AWS_SECRET_ACCESS_KEY = #your_secret_access_key
# replace this with your account number
AWS_USER_ID= #your userid

# Sections starting with "key" define your keypairs
# Section name should match your key name e.g.:
# (see the EC2 getting started guide tutorial on using ec2-add-keypair to learn
# how to create new keypairs)
[key gsg-keypair]
KEY_LOCATION=/home/myuser/.ssh/id_rsa-gsg-keypair

# You can of course have multiple keypair sections
# [key my-other-gsg-keypair]
# KEY_LOCATION=/home/myuser/.ssh/id_rsa-my-other-gsg-keypair

# Sections starting with "volume" define your EBS volumes
# Section name tags your volume e.g.:
[volume biodata]
# attach volume vol-c9999999 to /home on master node
VOLUME_ID = vol-c999999
MOUNT_PATH = /home

# Same volume as above, but mounts to different location
[volume biodata2]
# attach volume vol-c9999999 to /opt/ on master node
VOLUME_ID = vol-c999999
MOUNT_PATH = /opt/

[volume oceandata]
# attach volume vol-d7777777 to /mydata on master node 
VOLUME_ID = vol-d7777777
MOUNT_PATH = /mydata

# Sections starting with "plugin" define a custom python class
# which can perform additional configurations to StarCluster's default
# routines. These plugins can be assigned to a cluster section
# (see "smallcluster" below) to completely customize the setup procedure 
[plugin myplugin]
# myplugin module either lives in ~/.starcluster/plugins or is 
# in your PYTHONPATH
SETUP_CLASS = myplugin.SetupClass
# extra settings are passed as arguments to your plugin:
SOME_PARAM_FOR_MY_PLUGIN = 1
SOME_OTHER_PARAM = 2

# Sections starting with "cluster" define your cluster configurations
# Section name is the name you give to your cluster e.g.:
[cluster smallcluster]
# change this to the name of one of the keypair sections defined above 
KEYNAME = gsg-keypair

# number of ec2 instances to launch
CLUSTER_SIZE = 2

# create the following user on the cluster
CLUSTER_USER = sgeadmin
# optionally specify shell (defaults to bash)
# options: bash, zsh, csh, ksh, tcsh
CLUSTER_SHELL = bash

# AMI for master node. Defaults to NODE_IMAGE_ID if not specified
# The base i386 StarCluster AMI is %(x86_ami)s
# The base x86_64 StarCluster AMI is %(x86_64_ami)s
MASTER_IMAGE_ID = %(x86_ami)s

# instance type for the master node defaults to NODE_INSTANCE_TYPE if not
# specified
MASTER_INSTANCE_TYPE = m1.small

# AMI for worker nodes. Also used for the master node if MASTER_IMAGE_ID is not specified
# The base i386 StarCluster AMI is %(x86_ami)s
# The base x86_64 StarCluster AMI is %(x86_64_ami)s
NODE_IMAGE_ID = %(x86_ami)s

# instance type for all worker nodes (also applies to master if
# MASTER_INSTANCE_TYPE is not specified)
NODE_INSTANCE_TYPE = m1.small

# availability zone
AVAILABILITY_ZONE = us-east-1c

# list of volumes to attach to the cluster's master node
# and nfs mount to each cluster node
# (OPTIONAL)
VOLUMES = oceandata, biodata

# list of plugins to load after StarCluster's default ClusterSetup routine
# (OPTIONAL)
PLUGINS = myplugin

# You can also define multiple clusters.
# You can either supply all configuration options as with smallcluster above, or
# create an EXTENDS=<cluster_name> variable in the new cluster section to use all 
# settings from <cluster_name> as defaults e.g.:
[cluster mediumcluster]
# Declares that this cluster uses smallcluster as defaults
EXTENDS=smallcluster
# This section is the same as smallcluster except for the following settings:
KEYNAME=my-other-gsg-keypair
NODE_INSTANCE_TYPE = c1.xlarge
CLUSTER_SIZE=8
VOLUMES = biodata2

[cluster largecluster]
# Declares that this cluster uses mediumcluster as defaults
EXTENDS=mediumcluster
# This section is the same as mediumcluster except for the following variables:
CLUSTER_SIZE=16
""" % {
    'x86_ami': static.BASE_AMI_32,
    'x86_64_ami': static.BASE_AMI_64,
}

DASHES='-'*10
copy_paste_template=DASHES + ' COPY BELOW THIS LINE ' + DASHES  + \
    '\n' + config_template + '\n' + DASHES + ' END COPY ' + DASHES + '\n'
