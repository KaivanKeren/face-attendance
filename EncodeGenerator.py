import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from dotenv import load_dotenv

load_dotenv()

firebase_credentials_path = os.getenv('FIREBASE_CREDENTIALS_PATH')
database_url = os.getenv('DATABASE_URL')
storage_bucket = os.getenv('STORAGE_BUCKET')

# Initialize Firebase
cred = credentials.Certificate(firebase_credentials_path)
firebase_admin.initialize_app(cred, {
    'databaseURL': database_url,
    'storageBucket': storage_bucket
})

# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print("Image paths:", pathList)

imgList = []
studentIds = []

# Load images and upload them to Firebase
for path in pathList:
    fileName = os.path.join(folderPath, path)
    img = cv2.imread(fileName)
    if img is not None:
        imgList.append(img)
        studentIds.append(os.path.splitext(path)[0])

        # Upload to Firebase Storage
        bucket = storage.bucket()
        blob = bucket.blob(f'Images/{path}')
        try:
            blob.upload_from_filename(fileName)
            print(f"Uploaded {path} to Firebase Storage.")
        except Exception as e:
            print(f"Failed to upload {path}: {e}")
    else:
        print(f"Failed to load image {path}")

print("Student IDs:", studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        try:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encodings = face_recognition.face_encodings(img)
            if encodings:
                encodeList.append(encodings[0])
            else:
                print("No face found in image.")
        except Exception as e:
            print(f"Error encoding image: {e}")

    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

# Save encodings to file
try:
    with open("EncodeFile.p", 'wb') as file:
        pickle.dump(encodeListKnownWithIds, file)
    print("File Saved")
except Exception as e:
    print(f"Failed to save encoding file: {e}")
