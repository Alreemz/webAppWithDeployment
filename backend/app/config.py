import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:pass@db:5432/app_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
