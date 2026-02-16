import os

class Config:
  SECRET_KEY = os.getenv("SECRET_KEY")
  DB_HOST = os.getenv("DB_HOST")
  DB_USER = os.getenv("DB_USER")
  DB_PASS = os.getenv("DB_PASS")
  DB_NAME = os.getenv("DB_NAME")
  
  MAIL_SERVER = "smtp.gmail.com"
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.getenv("MAIL_USER")
  MAIL_PASSWORD = os.getenv("MAIL_PWD")