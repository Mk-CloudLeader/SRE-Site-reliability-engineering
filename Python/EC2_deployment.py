"""
- this is used to create EC2. 
- Need enough permission for Lambda's  execution Role and Increase Lambda default runtime

"""

import boto3

def lambda_handler(event, context):
   # Initialize the EC2 client
   ec2 = boto3.client('ec2')

   # Specify the parameters for the new instance
   instance_params = {
       'ImageId': 'ami-03a6eaae9938c858c',  # Replace with your desired AMI ID
       'InstanceType': 't2.micro',           # Replace with your desired instance type
       'KeyName': 'test1',           # Replace with your key pair name
       'MinCount': 1,
       'MaxCount': 1
       
   }

   # Create the EC2 instance
   response = ec2.run_instances(**instance_params)

   # Extract the instance ID from the response
   instance_id = response['Instances'][0]['InstanceId']

   return f"Created EC2 instance with ID: {instance_id}"
