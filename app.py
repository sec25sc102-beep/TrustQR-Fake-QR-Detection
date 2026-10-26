
import streamlit as st
from urllib.parse import urlparse
from PIL import Image
from pyzbar.pyzbar import decode

st.set_page_config(page_title="TrustQR", page_icon="🔐")
st.title("🔐 TrustQR - QR Code Safety Checker")
st.write("Upload a QR code image to inspect it.")

def check_qr(text):
    warnings = []
    parsed = urlparse(text)

    if parsed.scheme == "http":
        warnings.append("Warning: This website does not use HTTPS.")

    if "@" in parsed.netloc or "xn--" in parsed.netloc:
        warnings.append("Warning: This URL contains a suspicious pattern.")

    if not warnings:
        warnings.append(
            "No basic warning patterns detected. Safety is not guaranteed."
        )

    return warnings

uploaded = st.file_uploader(
    "Upload QR code image",
    type=["png", "jpg", "jpeg"]
)

if uploaded:
    image = Image.open(uploaded)
    results = decode(image)

    if not results:
        st.error("No QR code detected in this image.")
    else:
        for item in results:
            text = item.data.decode("utf-8", errors="replace")
            st.subheader("QR contents")
            st.code(text)

            for warning in check_qr(text):
                st.warning(warning)

            st.info(
                "Verify the recipient's UPI ID before making payments. "
                "This prototype cannot guarantee QR code safety."
            )
