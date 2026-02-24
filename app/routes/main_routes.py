from flask import Blueprint, render_template, session, redirect

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
  if "user" not in session:
    return redirect("/login")
  
  return render_template("index.html")

@main_bp.route("/play")
def play():
  if "user" not in session:
    return redirect("/login")
  
  return render_template("play.html")

@main_bp.route("/grades")
def grades():
  if "user" not in session:
    return redirect("/login")
  
  return render_template("grades.html")

@main_bp.route("/profile")
def profile():
  if "user" not in session:
    return redirect("/login")
  
  return render_template("profile.html")