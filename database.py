import pyrebase

firebaseConfig = {
    'apiKey':
    "AIzaSyCNAozYgMzvr5pjZ3Q83Mh1qCJ-Yj6ab_U",
    'authDomain':
    "studentresult-d5b18.firebaseapp.com",
    'projectId':
    "studentresult-d5b18",
    'storageBucket':
    "studentresult-d5b18.appspot.com",
    'messagingSenderId':
    "579422163544",
    'appId':
    "1:579422163544:web:b8ee320ba407bccb8a302d",
    'measurementId':
    "G-WMQ9YML0FY",
    'databaseURL':
    "https://studentresult-d5b18-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)