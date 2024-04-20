from flask import Flask, render_template, request, jsonify , redirect
from database import firebase

app = Flask(__name__)

# SETTING UP AUTHENTICATION
auth = firebase.auth()

def sign_up():
  name = request.form.get('name')
  roll_number = request.form.get('rollNumber')
  email = request.form.get('email')
  password = request.form.get('password')
  try:
    user = auth.create_user_with_email_and_password(email, password)
    # Store additional user data in Firebase Database
    user_data = {
        "name": name,
        "roll_number": roll_number,
        "email": email
    }
    db = firebase.database()
    db.child("users").child(user['localId']).set(user_data)
    return render_template('login.html' , message = "Sign Up Successful")
    
  except:
    return render_template('register.html' , message = "Email already exists")


def login():
  email = request.form.get('email')
  password = request.form.get('password')
  try:
    user = auth.sign_in_with_email_and_password(email, password)
    return jsonify({"success": True})

  except:
    return render_template('login.html' , message = "Invalid Credentials")




"""
# SETTING UP STORAGE
storage = firebase.storage()

# uploading a file to storage
file = input("Enter the file name: ")
cloudFileName = input("Enter the the name of file for storage: ")
storage.child(cloudFileName).put(file)

#get url
print(storage.child(cloudFileName).get_url(None))

#download
downloadLink = input("Enter download url : ")
storage.child(downloadLink).download("downloaded.txt")

#read from a file
path = input("Enter the path of the file: ")






#USING DATABASE
db = firebase.database()

#push data
data = {"name": "Shivansh",
       "Age" : 20,
       "Married" : True }

cloudFileName = input("Enter the the name of file for database storage: ")
db.child(cloudFileName).set(data)
"""



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
