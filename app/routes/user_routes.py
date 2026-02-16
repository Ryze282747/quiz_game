from flask import Blueprint, request, redirect, render_template, session, jsonify
from app.services.functions import *

user_bp = Blueprint("user", __name__)

@user_bp.route("/user/balance")
def balance():
  return jsonify({"msg":"test"})

@user_bp.route("/user/balance/withdraw", methods=["POST"])
def withdraw():
  return jsonify({"msg":"test"})

@user_bp.route("/user/balance/deposit", methods=["POST"])
def deposit():
  return jsonify({"msg":"test"})