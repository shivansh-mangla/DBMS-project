from flask import Flask, render_template, request, jsonify , redirect
from database import firebase
from werkzeug.utils import secure_filename
import os
import hashlib


app = Flask(__name__)

# SETTING UP AUTHENTICATION

def sign_up():
  name = request.form.get('name')
  roll_number = request.form.get('rollNumber')
  email = request.form.get('email')
  password = request.form.get('password')
  photo = request.files['profilePhoto']
  try:
      filename = secure_filename(photo.filename)
      local_path = os.path.join('uploads', filename)
      photo.save(local_path)  # Save file locally
      storage_path = f"profilePhoto/{email}"
    
      storage = firebase.storage()
      storage.child(storage_path).put(local_path)
      # Clean up local file
      os.remove(local_path)

      # Setting up authentication
      auth = firebase.auth()
      user = auth.create_user_with_email_and_password(email, password)

      # Store additional user data in Firebase Database
      user_data = {
          "name": name,
          "roll_number": roll_number,
          "email": email
      }
      db = firebase.database()
      db.child(email).set(user_data)
      return render_template('login.html', message="Sign Up Successful")

  except Exception as e:
      return render_template('register.html', message="Email already exists")



def login():
  email = request.form.get('email')
  password = request.form.get('password')
  try:
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(email, password)
    return render_template('home.html', message="Login Successful")

  except:
    return render_template('login.html' , message = "Invalid Credentials")



@app.route("/register" , methods=['POST','GET'])
def register_route():
  if request.method == 'POST':
    return sign_up()
  else:
    return render_template('register.html')
  

@app.route("/login", methods=['POST','GET'])
def login_route():
  if request.method == 'POST':
    return login()
  else:
    return render_template('login.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
