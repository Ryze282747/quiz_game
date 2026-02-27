from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from app.services.db_functions import *
from app.services.mailer import *
from flask import current_app
import random
import jwt
import uuid

def generate_jwt(payload: dict, expires_in=30):
    SECRET_KEY = current_app.config["SECRET_KEY"]
    payload = payload.copy()  # avoid mutating original
    payload["exp"] = datetime.utcnow() + timedelta(seconds=expires_in)
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def generate_id(transaction_id=False):
  if transaction_id:
    return "TXN-" + uuid.uuid4().hex[:12].upper()
  
  return str(uuid.uuid4())

def isEmailExist(email):
  res = read_data("users", "email", "email = %s", (email,))
  return res["status"] == 200 and bool(res["data"])

def create_user(name, pwd, email_adr):
  try:
    user_id = generate_id()
    
    if isEmailExist(email_adr):
      return {"msg":"Failed to create user.", "exist":True, "status":409}
    
    
    res = create_data("users", username=name.capitalize(), password=generate_password_hash(pwd), email=email_adr, uid=user_id)
    
    if res["status"] == 201:
      send_signup_confirm(email_adr, name.capitalize())
    
    return res
    
  except Exception as e:
    return {"msg":"Failed to create user.", "error":e, "status":500}

def verify_user(email, password):
  try:
    if not isEmailExist(email):
      return {"msg":"Invalid credentials", "status":401, "access":False}
    
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
    return {"msg":f"Error: {e}", "status":500}

def get_points(email):
  try:
    points = read_data("users", "total_points", "email = %s", (email,))
    
    
    if points["status"] != 200:
      return points
    
    return {
      "points":int(points["data"][0]["total_points"]),
      "msg":"Data retrieved!",
      "status":200
    }
    
  except Exception as e:
    return {"msg":f"Error: {e}", "status":500}

def get_earnings(email):
  try:
    earnings = read_data("users", "total_earnings", "email = %s", (email,))
    
    
    if earnings["status"] != 200:
      return earnings
    
    return {
      "earnings":int(earnings["data"][0]["total_earnings"]),
      "msg":"Data retrieved!",
      "status":200
    }
    
  except Exception as e:
    return {"msg":f"Error: {e}", "status":500}

def get_rank(email):
  try:
    res = read_data_ordered("users", order_by="total_points", limit=100, desc=True)
  
    
    for i in res["data"]:
      if i["email"] == email:
        rank = res["data"].index(i) + 1
        
        return {
          "rank":rank,
          "msg":"Data retrieved!",
          "status":200
        }
    
    return {
      "rank":"100+",
      "msg":"Data retrieved!",
      "status":200
    }
    
  except Exception as e:
    return {"msg":f"Error: {e}", "status":500}

def process_withdraw(email, withdraw_amount):
  try:
    curr_balance = get_balance(email)
    curr_earnings = get_earnings(email)
    
    if withdraw_amount > curr_balance["balance"]:
      return {"msg":"Insufficient balance.", "status":422}
    
    transact_id = generate_id(True)
    
    new_balance = curr_balance["balance"] - withdraw_amount
    new_earnings = curr_earnings["earnings"] + withdraw_amount
    
    raw_data_user_id = read_data("users", "uid", "email = %s", (email,))
    user_id = raw_data_user_id["data"][0]["uid"]
    
    new_withdraw_history = create_data("withdraws", amount=withdraw_amount, uid=user_id, transaction_id=transact_id)
    
    if new_withdraw_history["status"] != 201:
      return {"msg":"An error occured. Please try again.", "status":500}
    
    update_balance = update_data("users", f"email = '{email}'", new_balance, "balance")
    
    if update_balance["status"] != 200:
      return {"msg":"An error occured. Please try again.", "status":500}
    
    update_earnings = update_data("users", f"email = '{email}'", new_earnings, "total_earnings")
    
    if update_earnings["status"] != 200:
      return {"msg":"An error occured. Please try again.", "status":500}
    
    return {
      "status":200,
      "msg":"Withdrawal successful!",
    }
    
  except Exception as e:
    return {"msg":"An error occured. Please try again.", "status":500}