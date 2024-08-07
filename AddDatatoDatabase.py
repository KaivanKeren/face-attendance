import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from dotenv import load_dotenv

load_dotenv()

firebase_credentials_path = os.getenv('FIREBASE_CREDENTIALS_PATH')
database_url = os.getenv('DATABASE_URL')

# Initialize Firebase Admin SDK
cred = credentials.Certificate(firebase_credentials_path)
firebase_admin.initialize_app(cred, {
    'databaseURL': database_url,
})

# Reference to 'Students' node
ref = db.reference('Students')

# Data to be added
data = {
    "3123112": {
        "name": "Ismail",
        "major": "Computer",
        "starting_year": 2022,
        "total_attendance": 9,
        "standing": "G",
        "year": 3,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "2174875": {
        "name": "Junia Zahra",
        "major": "SMP",
        "starting_year": 2024,
        "total_attendance": 12,
        "standing": "B",
        "year": 1,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "4121643": {
        "name": "Khayatun",
        "major": "Teacher",
        "starting_year": 2000,
        "total_attendance": 12,
        "standing": "G",
        "year": 1,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
}

# Add data to the 'Students' reference
try:
    for key, value in data.items():
        ref.child(key).set(value)
    print("Data successfully written to Firebase Realtime Database.")
except Exception as e:
    print(f"Error writing data to Firebase: {e}")
