from flask import Blueprint, request, redirect, render_template, session, jsonify
from app.services.functions import *

user_bp = Blueprint("user", __name__)

@user_bp.route("/user/balance")
def balance():
  
  if "user" not in session:
    return jsonify({"balance":None, "status":400})
  
  balance = get_balance(session["user"])
  
  return jsonify(balance)

@user_bp.route("/user/balance/withdraw", methods=["POST"])
def withdraw():
  
  return jsonify({"msg":"test"})
  