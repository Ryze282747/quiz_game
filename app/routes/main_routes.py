from flask import Blueprint, render_template, session, redirect

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
  if "user" not in session:
    return redirect("/login")
  
  return render_template("index.html")

@main_bp.route("/dashboard")
def dashboard():
  if "user" not in session:
    return redirect("/login")
  
  return render_template("dashboard.html")

@main_bp.route("/calendar")
def calendar():
  if "user" not in session:
    return redirect("/login")
  
  return render_template("calendar.html")

@main_bp.route("/profile")
def profile():
  if "user" not in session:
    return redirect("/login")
  
  return render_template("profile.html")