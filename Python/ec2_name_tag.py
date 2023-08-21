"""
- Name tag if user is missed to add during EC2 deployment 
- Lambda function will trigger based on EventBridge rule
- EventBridge Rule - Create rule based on EC2 event pattern 
    - EC2 - EC2 instance state change notification 
"""
#!/usr/bin/python
import boto3
import logging

#setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#define the connection
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    # Use the filter() method of the instances collection to retrieve
    # all running EC2 instances.
    filters = [{
            'Name': 'tag:Name',
            'Values': ['']
        },
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]

    #filter the instances
    instances = ec2.instances.filter(Filters=filters)

    #locate all running instances
    RunningInstances = [instance.id for instance in instances]

    #print the instances for logging purposes
    #print RunningInstances

    #make sure there are actually instances to shut down.
    if len(RunningInstances) > 0:
        #perform the shutdown
        shuttingDown = ec2.instances.filter(InstanceIds=RunningInstances).stop()
        print shuttingDown
    else:
        print "Nothing to see here" 
