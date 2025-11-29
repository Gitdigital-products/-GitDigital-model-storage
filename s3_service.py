import boto3
from config.settings import settings

s3 = boto3.client(
    "s3",
    aws_access_key_id=settings.AWS_KEY,
    aws_secret_access_key=settings.AWS_SECRET
)

def upload_model(file_path, key):
    s3.upload_file(file_path, settings.BUCKET_NAME, key)

def download_model(key, file_path):
    s3.download_file(settings.BUCKET_NAME, key, file_path)
