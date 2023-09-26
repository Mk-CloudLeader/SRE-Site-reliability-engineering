import boto3

def lambda_handler(event, context):
   # Initialize the S3 client
   s3 = boto3.client('s3')

   # Specify the desired bucket name (replace 'your-unique-bucket-name')
   bucket_name = 'muk-poc-test-sre'

   # Create the S3 bucket
   s3.create_bucket(Bucket=bucket_name)

   # Define the bucket policy to make it private
"""
   bucket_policy = {
       'Version': '2012-10-17',
       'Statement': [
           {
               'Sid': 'PrivateBucketPolicy',
               'Effect': 'Deny',
               'Principal': '*',
               'Action': 's3:GetObject',
               'Resource': 'arn:aws:s3:::{bucket_name}/*'
           }
       ]
   }
"""
   # Apply the bucket policy to make the bucket private
   # s3.put_bucket_policy(Bucket=bucket_name, Policy=str(bucket_policy))

   #return f"Created private S3 bucket: {bucket_name}"
