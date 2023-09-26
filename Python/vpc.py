import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Create a VPC
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')

# Enable DNS support and hostname for the VPC
ec2.modify_vpc_attribute(VpcId=vpc['Vpc']['VpcId'], EnableDnsSupport={'Value': True})
ec2.modify_vpc_attribute(VpcId=vpc['Vpc']['VpcId'], EnableDnsHostnames={'Value': True})

# Create a public subnet within the VPC
public_subnet = ec2.create_subnet(
   VpcId=vpc['Vpc']['VpcId'],
   CidrBlock='10.0.0.0/24'
)

# Create a private subnet within the VPC
private_subnet = ec2.create_subnet(
   VpcId=vpc['Vpc']['VpcId'],
   CidrBlock='10.0.1.0/24'
)

# Tag the subnets for identification
ec2.create_tags(Resources=[public_subnet['Subnet']['SubnetId']], Tags=[{'Key': 'Name', 'Value': 'Public_Subnet'}])
ec2.create_tags(Resources=[private_subnet['Subnet']['SubnetId']], Tags=[{'Key': 'Name', 'Value': 'Private_Subnet'}])

print("VPC ID:", vpc['Vpc']['VpcId'])
print("Public Subnet ID:", public_subnet['Subnet']['SubnetId'])
print("Private Subnet ID:", private_subnet['Subnet']['SubnetId'])
