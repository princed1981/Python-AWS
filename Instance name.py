import boto3
import sys
##
##ec2 = boto3.resource('ec2')
##
##for instance in ec2.instances.all():
##    print(instance.id,instance.state)
#---------------------------------------

import boto3

ec2 = boto3.resource('ec2')
instance = ec2.create_instances(ImageId='ami-14c5486b',MinCount=1,MaxCount=1,InstanceType='t2.micro')
print(instance[0].id)

##ec2 = boto3.resource('ec2')
##
####for instance_id in sys.argv[1:]:
##instance = ec2.Instance('i-0f9b99beeefbb0955')
##response = instance.terminate()
##print(response)
