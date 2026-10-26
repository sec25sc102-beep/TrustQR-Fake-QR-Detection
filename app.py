
import streamlit as st
import cv2
import numpy as np
from urllib.parse import urlparse

st.set_page_config(page_title="TrustQR", page_icon="🔐")
st.title("🔐 TrustQR - QR Code Safety Checker")
st.write("Upload a QR code image to inspect it.")

def check_qr(text):
    warnings = []
    parsed = urlparse(text)

    if parsed.scheme.lower() == "http":
        warnings.append("Warning: This website does not use HTTPS.")

    if "@" in parsed.netloc or "xn--" in parsed.netloc:
        warnings.append("Warning: This URL contains a suspicious pattern.")

    if not warnings:
        warnings.append(
            "No basic warning patterns detected. "
            "Safety is not guaranteed."
        )

    return warnings

uploaded = st.file_uploader(
    "Upload QR code image",
    type=["png", "jpg", "jpeg"]
)

if uploaded:
    image_bytes = np.frombuffer(uploaded.getvalue(), np.uint8)
    image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)

    if image is None:
        st.error("Unable to read this image.")
    else:
        detector = cv2.QRCodeDetector()
        text, points, _ = detector.detectAndDecode(image)

        if not text:
            st.error("No readable QR code detected.")
        else:
            st.subheader("QR contents")
            st.code(text)

            for warning in check_qr(text):
                st.warning(warning)

            st.info(
                "Verify the recipient's UPI ID before paying. "
                "This prototype cannot guarantee QR code safety."
            )
