def list_versions(bucket_name, file_name):
    versions = s3.list_object_versions(Bucket=bucket_name, Prefix=file_name)
    for version in versions['Versions']:
        print(f"VersionId: {version['VersionId']} - LastModified: {version['LastModified']}")

# List all versions of a specific patient record
list_versions('patient-records-bucket', 'patient123_test_results.pdf')
