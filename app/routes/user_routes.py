from flask import Blueprint, request, redirect, render_template, session, jsonify
from app.services.functions import *

user_bp = Blueprint("user", __name__)

@user_bp.route("/user/balance")
def balance():
  
  if "user" not in session:
    return jsonify({"balance":None, "status":400})
  
  balance = get_balance(session["user"])
  
  return jsonify(balance)

@user_bp.route("/user/points")
def total_points():
  
  if "user" not in session:
    return jsonify({"points":None, "status":400})
  
  points = get_points(session["user"])
  
  return jsonify(points)

@user_bp.route("/user/rank")
def rank():
  
  if "user" not in session:
    return jsonify({"rank":None, "status":400})
  
  rank = get_rank(session["user"])
  
  
  return jsonify(rank)

@user_bp.route("/user/earnings")
def total_earnings():
  
  if "user" not in session:
    return jsonify({"earnings":None, "status":400})
  
  earnings = get_earnings(session["user"])
  
  return jsonify(earnings)


@user_bp.route("/user/balance/withdraw", methods=["POST"])
def withdraw():
  
  data = request.get_json()
  
  res = process_withdraw(session["user"], data["amount"])
  
  return jsonify(res)
  