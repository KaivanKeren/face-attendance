# Face Attendance System

This project is a face attendance system that uses facial recognition to identify individuals and update their attendance records. It integrates with Firebase for database and storage management and utilizes OpenCV and face_recognition libraries for face detection and recognition.

## Features

- **Real-time Face Detection and Recognition**: Uses the camera feed to detect and recognize faces in real-time.
- **Attendance Tracking**: Updates attendance records based on recognized faces and stores them in a Firebase Realtime Database.
- **Image Retrieval**: Fetches student images from Firebase Storage for display.
- **UI Display**: Provides a graphical user interface with real-time feedback on attendance status and student information.

## Prerequisites

Ensure you have the following software installed:

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy (`numpy`)
- Face Recognition (`face_recognition`)
- Firebase Admin SDK (`firebase-admin`)
- Python-dotenv (`python-dotenv`)
- cvzone (`cvzone`)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. **Install Dependencies**

   Create a virtual environment and install the required packages:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Setup Firebase**

   - Create a Firebase project and obtain the necessary credentials.
   - Download the Firebase Admin SDK private key and save it as `firebase_credentials.json`.
   - Set up your Firebase Realtime Database and Firebase Storage.

4. **Environment Variables**

   Create a `.env` file in the project root directory and add the following environment variables:

   ```ini
   FIREBASE_CREDENTIALS_PATH=path/to/firebase_credentials.json
   DATABASE_URL=https://your-database-url.firebaseio.com/
   STORAGE_BUCKET=your-storage-bucket-name
   ```

5. **Prepare Resources**

   - Place the background image and mode images in the `Resources` folder.
   - Ensure the encoding file (`EncodeFile.p`) is present in the project root.

## Usage

1. **Run the Script**

   Execute the main script to start the attendance system:

   ```bash
   python main.py
   ```

2. **Operation**

   - The application will display the camera feed with real-time face detection.
   - Recognized faces will update the attendance records and show student information on the screen.
   - Press `q` to quit the application.

## Code Overview

- **Imports and Setup**: Loads environment variables, initializes Firebase, and sets up video capture.
- **Resource Loading**: Loads images and encoding files.
- **Main Loop**: Captures frames from the camera, detects faces, recognizes them, and updates the attendance records.
- **Firebase Integration**: Fetches and updates student data in Firebase Realtime Database and retrieves images from Firebase Storage.
- **UI Update**: Updates the display with student information and attendance status.

## Troubleshooting

- Ensure that all paths in the `.env` file and code are correctly set.
- Check that the camera is properly connected and accessible.
- Verify that Firebase credentials and database URLs are correct.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes. For major changes, please open an issue to discuss the modifications.

## Contact

For any questions or feedback, you can reach out to me at [your-email@example.com](mailto:your-email@example.com).

---

Replace placeholders like `yourusername`, `your-repository`, and `your-email@example.com` with your actual information. This `README.md` provides a comprehensive overview of the project, including setup instructions, code functionality, and troubleshooting tips.
