from flask_mail import Message
from flask import current_app
from app import mail

def send_signup_confirm(email_adr, name):
  try:
    
    msg = Message(
      subject=f"Welcome! {name}",
      sender=current_app.config["MAIL_USERNAME"],
      recipients=[email_adr],
      body="Account Created! Thankyou for signing up!"
    )
    
    mail.send(msg)
    
    return {"msg":"Mail send succesfully!", "status":200}
    
  except Exception as e:
    return {"msg":f"Error {e}", "status":500}