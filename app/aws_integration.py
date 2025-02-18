import boto3

def upload_to_s3(file_path, bucket_name, object_name=None):
    """Uploads a file to an AWS S3 bucket."""
    s3 = boto3.client('s3')
    if object_name is None:
        object_name = file_path.split("/")[-1]
    
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"File {file_path} uploaded to {bucket_name}/{object_name}")
    except Exception as e:
        print(f"Error uploading file: {e}")

def download_from_s3(bucket_name, object_name, file_path):
    """Downloads a file from an AWS S3 bucket."""
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, object_name, file_path)
        print(f"File {object_name} downloaded to {file_path}")
    except Exception as e:
        print(f"Error downloading file: {e}")

def list_s3_files(bucket_name):
    """Lists files in an AWS S3 bucket."""
    s3 = boto3.client('s3')
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            files = [item['Key'] for item in response['Contents']]
            print("Files in S3 bucket:", files)
            return files
        else:
            print("No files found in the bucket.")
            return []
    except Exception as e:
        print(f"Error listing files: {e}")
        return []

if __name__ == "__main__":
    BUCKET_NAME = "your-bucket-name"  # Replace with your actual S3 bucket name
    
    # Example usage
    upload_to_s3("test.txt", BUCKET_NAME)
    download_from_s3(BUCKET_NAME, "test.txt", "downloaded_test.txt")
    list_s3_files(BUCKET_NAME)
