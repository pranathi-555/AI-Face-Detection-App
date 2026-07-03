import streamlit as st
import cv2
import numpy as np
from PIL import Image
from detector import detect_faces

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="AI Face Detection App",
    page_icon="😀",
    layout="wide"
)

# ---------------- HEADER ---------------- #
st.title("😀 AI Face Detection App")

st.markdown("""
Detect human faces in images using **OpenCV Haar Cascade Classifier**.

📤 Upload an image and the application will automatically detect faces,
draw bounding boxes, and display the total number of detected faces.
""")

# ---------------- SIDEBAR ---------------- #
st.sidebar.header("📌 About Project")

st.sidebar.info("""
### AI Face Detection

**Technologies Used**

- Python
- OpenCV
- Haar Cascade Classifier
- Streamlit
- NumPy
- Pillow

This project detects human faces in uploaded images using classical computer vision techniques.
""")

st.sidebar.markdown("---")

st.sidebar.success("Developed for AI Internship Project")

# ---------------- FILE UPLOAD ---------------- #
uploaded_file = st.file_uploader(
    "📤 Upload an Image",
    type=["jpg", "jpeg", "png"]
)

# ---------------- MAIN APP ---------------- #
if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    image_np = np.array(image)

    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    with st.spinner("🔍 Detecting faces..."):

        result, face_count = detect_faces(image_bgr)

    result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    # Display Images
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🖼 Original Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("✅ Face Detection Result")
        st.image(result_rgb, use_container_width=True)

    st.markdown("---")

    # Detection Summary
    st.subheader("📊 Detection Summary")

    metric1, metric2 = st.columns(2)

    with metric1:
        col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Faces", face_count)

    with col2:
        st.metric("Image Width", image.width)

    with col3:
        st.metric("Image Height", image.height)

    with metric2:
        if face_count == 0:
            st.metric("Status", "No Faces")
        else:
            st.metric("Status", "Success")

    # Success / Warning Message
    if face_count == 0:
        st.warning("⚠️ No faces were detected in the uploaded image.")
    else:
        st.success(f"✅ Successfully detected **{face_count}** face(s).")

    # Download Button
    success, encoded_image = cv2.imencode(".jpg", result)

    if success:
        st.download_button(
            label="📥 Download Processed Image",
            data=encoded_image.tobytes(),
            file_name="detected_faces.jpg",
            mime="image/jpeg"
        )

# ---------------- FOOTER ---------------- #
st.markdown("---")

st.caption("© 2026 AI Face Detection App | Built with ❤️ using Python, OpenCV & Streamlit")