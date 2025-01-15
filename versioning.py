import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

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
enable_versioning('patient-records-bucket')
