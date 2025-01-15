def get_specific_version(bucket_name, file_name, version_id):
    s3.download_file(bucket_name, file_name, f'/path/to/download/{file_name}_{version_id}')
    print(f"Downloaded {file_name} version {version_id}")

# Download a specific version of a patient record
get_specific_version('patient-records-bucket', 'patient123_test_results.pdf', 'abc123xyz')
