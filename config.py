import os

class Config:
    # AWS Configuration
    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY", "your-access-key")
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", "your-secret-key")
    AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME", "your-bucket-name")
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

    # Database Configuration
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "forensics_db")
    DB_USER = os.getenv("DB_USER", "admin")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
    
    # Other settings
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
