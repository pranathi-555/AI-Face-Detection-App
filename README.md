# 😀 AI Face Detection App

An AI-powered web application that detects human faces in uploaded images using **OpenCV Haar Cascade Classifier** and **Streamlit**.

🔗 **Live Demo:** https://ai-face-detection-app-xs6kqzydmmgay4zdidbcq4.streamlit.app/

🔗 **GitHub Repository:** https://github.com/pranathi-555/AI-Face-Detection-App

---

# 📌 Project Overview

The AI Face Detection App is a computer vision application that allows users to upload an image and automatically detect human faces.

The application uses the **Haar Cascade Face Detection** algorithm provided by OpenCV to identify faces, draw bounding boxes around them, and display the total number of detected faces.

The project is built with **Python**, **OpenCV**, and **Streamlit**, providing an interactive and user-friendly web interface.

---

# 🚀 Live Demo

👉 https://ai-face-detection-app-xs6kqzydmmgay4zdidbcq4.streamlit.app/

---

# ✨ Features

- 📤 Upload JPG, JPEG, and PNG images
- 😀 Detect one or multiple human faces
- 🟩 Draw bounding boxes around detected faces
- 📊 Display the total number of detected faces
- 📥 Download the processed image
- ⚡ Fast image processing
- 🌐 Responsive Streamlit web interface

---

# 🛠 Tech Stack

- Python
- OpenCV
- Haar Cascade Classifier
- Streamlit
- NumPy
- Pillow

---

# 📂 Project Structure

```
AI-Face-Detection-App/
│
├── app.py
├── detector.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── images/
│   ├── home.png
│   ├── upload.png
│   ├── detection.png
│   └── download.png
│
├── test_images/
├── output_images/
└── face_detection.ipynb
```

---

# 📸 Application Screenshots

## 🏠 Home Page

<img width="1366" height="768" alt="Screenshot (132)" src="https://github.com/user-attachments/assets/ce248418-1de9-4c82-aa0b-576c68775840" />


---

## 📤 Upload Image

<img width="1366" height="768" alt="Screenshot (133)" src="https://github.com/user-attachments/assets/320bb82b-9be4-48c1-8a99-3ced27cbb483" />


---

## 😀 Face Detection Result

<img width="1366" height="768" alt="Screenshot (134)" src="https://github.com/user-attachments/assets/46d5b9be-693f-496f-b85f-649f1a1068ac" />


---


# ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/pranathi-555/AI-Face-Detection-App.git
```

### Navigate to the Project Folder

```bash
cd AI-Face-Detection-App
```

### Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

# 📊 Workflow

```
Upload Image
      │
      ▼
Convert Image to NumPy Array
      │
      ▼
Convert RGB → BGR
      │
      ▼
Convert to Grayscale
      │
      ▼
Detect Faces using Haar Cascade
      │
      ▼
Draw Bounding Boxes
      │
      ▼
Count Faces
      │
      ▼
Display Result
      │
      ▼
Download Processed Image
```

---

# 💡 Future Enhancements

- 🎥 Real-time webcam face detection
- 🧠 YOLOv8 Face Detection
- 👤 Face Recognition
- 😊 Emotion Detection
- 👶 Age & Gender Prediction
- 😷 Face Mask Detection
- 📱 Mobile-friendly interface

---

# 🎯 Learning Outcomes

Through this project, I learned:

- OpenCV fundamentals
- Image preprocessing
- Haar Cascade face detection
- Image handling using NumPy
- Streamlit web application development
- Deploying AI applications on Streamlit Community Cloud
- Git & GitHub version control

---

# 👩‍💻 Developed By

**Pranathi Kurapati**

Electronics & Communication Engineering Student

AI | Machine Learning | Computer Vision | Python Developer

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub!
