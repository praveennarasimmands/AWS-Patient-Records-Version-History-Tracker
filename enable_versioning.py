import os
import boto3
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv() 

# Get AWS credentials and region from environment variables
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_REGION')  # Fetch the region from the .env file

# Check if all required environment variables are set
if not aws_access_key_id or not aws_secret_access_key or not aws_region:
    print("Error: AWS credentials or region are not set in environment variables.")
    exit(1)

# Initialize the S3 client with the environment variables for credentials and region
s3 = boto3.client('s3',
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  region_name=aws_region) 

# Optional: Function to enable versioning on the S3 bucket
def enable_versioning(bucket_name):
    # Enable versioning for the S3 bucket
    s3.put_bucket_versioning(
        Bucket=bucket_name,
        VersioningConfiguration={
            'Status': 'Enabled'
        }
    )
    print(f"S3 Versioning enabled for bucket: {bucket_name}")

# Enable versioning on the S3 bucket
enable_versioning('Your_Bucket_Name')
