import boto3
import logging
import os
from collections import defaultdict

counter = 0
region = 'us-east-1'

ACCESS_ID = os.environ['AWS_ACCESS_KEY_ID']
ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
TAGSEARCH = os.environ['MY_TAG']

# Connect to EC2
ec2r = boto3.resource('ec2',
                      region,
                      aws_access_key_id=ACCESS_ID,
                      aws_secret_access_key= ACCESS_KEY)

print("================================\n")
print("Getting AWS EC2 not tagged instances WITH TAG NAME: %s" % TAGSEARCH)
print("=================================\n")


# get a list of all instances
all_running_instances = [i for i in ec2r.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])]
for instance in all_running_instances:
    print("Running instance detected: %s" % instance.id)

# get instances with filter of running + with tag `Name`
#instances = [i for i in ec2r.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}, {'Name':'tag:nottagged', 'Values':['yes']}])]
instances = [i for i in ec2r.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}, {'Name':'tag:'+TAGSEARCH, 'Values':['yes']}])]

#for instance in instances:
#    print("Running instance with tag identified detected: %s" % instance.id)

# make a list of filtered instances IDs `[i.id for i in instances]`
# Filter from all instances the instance that are not in the filtered list
instances_to_delete = [to_del for to_del in all_running_instances if to_del.id not in [i.id for i in instances]]

ec2info = defaultdict()
# run over your `instances_to_delete` list and terminate each one of them
for instance in instances_to_delete:
#    instance.stop()
  print("================================\n")
  print("Instances without tag Id name detected: %s" % instance.id)
  print("=================================\n")
  counter +=1
  ec2info[instance.id] = {
             #'Name': name,
             'Type': instance.instance_type,
             #'State': instance.state['Name'],
             'Private IP': instance.private_ip_address,
             'Public IP': instance.public_ip_address,
             'Launch Time': instance.launch_time
           }
  

  attributes = ['Type', 'Private IP', 'Public IP', 'Launch Time']
  for instance_id, instance in ec2info.items():
      for key in attributes:
          print("{0}: {1}".format(key, instance[key]))
      #print("------")
  ec2info.clear()
  counterstr = int(counter)
  print("================================\n")
  print("Total instances detected without tag: %s " % counter )
  print("================================\n")

