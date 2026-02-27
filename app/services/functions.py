from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from app.services.db_functions import *
from app.services.mailer import *
from flask import current_app
import random
import jwt

def generate_jwt(payload: dict, expires_in=30):
    SECRET_KEY = current_app.config["SECRET_KEY"]
    payload = payload.copy()  # avoid mutating original
    payload["exp"] = datetime.utcnow() + timedelta(seconds=expires_in)
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def generate_id():
  data = read_data("users", "uid")
  
  if data["status"] == 500:
    return None
  
  ids = []
  
  for i in data["data"]:
    ids.append(i["uid"])
  
  while True:
    generated_id = ""
    for i in range(15):
      generated_id += str(random.randint(0,9))
    if generated_id not in ids:
      return generated_id
      break

def isEmailExist(email):
  res = read_data("users", "email")
  for i in res["data"]:
    if i["email"] == email:
      return True
  
  return False

def create_user(name, pwd, email_adr):
  try:
    user_id = generate_id()
    
    if isEmailExist(email_adr):
      return {"msg":"Failed to create user.", "exist":True, "status":500}
    
    
    res = create_data("users", username=name.capitalize(), password=generate_password_hash(pwd), email=email_adr, uid=user_id)
    
    if res["status"] == 201:
      send_signup_confirm(email_adr, name.capitalize())
    
    return res
    
  except Exception as e:
    return {"msg":"Failed to create user.", "error":e, "status":500}

def verify_user(email, password):
  try:
    if not isEmailExist(email):
      return {"msg":"Invalid credentials", "status":200, "access":False}
    
    res = read_data("users", "password", "email = %s", (email,))
    
    if check_password_hash(res["data"][0]["password"], password):
      return {"msg":"Access granted.", "access":True, "status":200}
    
    return {"msg":"Invalid credentials", "status":200, "access":False}
  
  except Exception as e:
    return {"msg":"Failed to verify user.", "error":e, "status":500}

def get_username(email):
  try:
    username = read_data("users", "username", "email = %s", (email,))
    
    if username["status"] != 200:
      return username
    
    return {
      "username":username["data"][0]["username"],
      "status":200,
      "msg":"Data retrieved!"
    }
  except Exception as e:
<<<<<<< HEAD
=======
    return {"msg":f"Error: {e}", "status":500}

def get_balance(email):
  try:
    balance = read_data("users", "balance", "email = %s", (email,))
    
    if balance["status"] != 200:
      return balance
    
    return {
      "balance":int(balance["data"][0]["balance"]),
      "msg":"Data retrieved!",
      "status":200
    }
    
  except Exception as e:
>>>>>>> parent of 330ed95 (add withdraw function)
    return {"msg":f"Error: {e}", "status":500}