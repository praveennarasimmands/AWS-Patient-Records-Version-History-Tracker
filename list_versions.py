import os
import boto3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get AWS credentials and region from environment variables
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_REGION')  # Fetch the region from the .env file

# Check if all required environment variables are set
if not aws_access_key_id or not aws_secret_access_key or not aws_region:
    print("Error: AWS credentials or region are not set in environment variables.")
    exit(1)

# Initialize the S3 client with the loaded credentials and region
s3 = boto3.client('s3', 
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  region_name=aws_region)  # Added region_name

def list_versions(bucket_name, file_name):
    try:
        # List all versions of the file in the S3 bucket
        versions = s3.list_object_versions(Bucket=bucket_name, Prefix=file_name)
        
        if 'Versions' not in versions:
            print("No versions found for this file.")
            return

        for version in versions['Versions']:
            print(f"VersionId: {version['VersionId']} - LastModified: {version['LastModified']}")
    except Exception as e:
        print(f"Error listing versions: {e}")

# List all versions of a specific file (Replace with your bucket and file)
list_versions('Your_Bucket_Name', 'File Name')
