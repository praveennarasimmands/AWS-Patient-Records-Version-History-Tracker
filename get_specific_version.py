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

def get_specific_version(bucket_name, file_name, version_id):
    try:
        # Define the download path
        download_path = fr'Path\{file_name}_{version_id}'  
        
        # Download the specified version of the file from the S3 bucket
        s3.download_file(bucket_name, file_name, download_path, ExtraArgs={'VersionId': version_id})
        print(f"Downloaded {file_name} version {version_id} to {download_path}")
    except Exception as e:
        print(f"Error downloading file: {e}")

# Example usage: Download a specific version of a file (replace with your bucket, file, and version ID)
get_specific_version('Your_Bucket_Name', 'File Name','Version Id')
