from flask import Blueprint, request, redirect, render_template, session, jsonify
from app.services.functions import *

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST", "GET"])
def login():
  if request.method == "POST":
    
    data = request.get_json()
    
    res = verify_user(data["email"], data["password"])
    
    if res["access"]:
      session["user"] = data["email"]
      return jsonify({"msg":"Access granted!", "access":True, "status":200})
    
    return jsonify(res)
  
  if "user" in session:
    return redirect("/")
  
  return render_template("login.html")

@auth_bp.route("/signup", methods=["POST", "GET"])
def signup():
  if request.method == "POST":
    data = request.get_json()
    
    res = create_user(data["username"], data["password"], data["email"])
    
    
    return jsonify(res)
  
  if "user" in session:
    return redirect("/")
  
  return render_template("signup.html")

@auth_bp.route("/get_user")
def get_user():
  
  if "user" not in session:
    return jsonify({"current_user":None, "username":None, "status":200})
  
  username = get_username(session["user"])
  
  if username["status"] != 200:
    return username
  
  return jsonify({"current_user":session["user"], "status":200, "username":username["username"]})

@auth_bp.route("/logout")
def logout():
  session.clear()
  return redirect("/")