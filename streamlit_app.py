import streamlit as st

import qrcode

import matplotlib.pyplot as plt

from io import BytesIO

def generate_qr_code(data):

    qr = qrcode.QRCode(version=1, box_size=10, border=5)

    qr.add_data(data)

    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")

    return qr_img

def plot_qr_code(qr_img):

    # Convert PIL image to NumPy array

    qr_array = plt.imshow(qr_img)

    plt.axis('off')  # Hide axes

    buf = BytesIO()

    plt.savefig(buf, format='png')

    buf.seek(0)

    return buf

def main():

    st.title("QR Code Generator")

    st.write("Enter text or URL to generate a QR code")

    # User input

    input_data = st.text_input("Enter text or URL")

    if st.button("Generate QR Code"):

        if input_data:

            # Generate QR code

            qr_code = generate_qr_code(input_data)

            # Display the QR code image

            qr_buffer = plot_qr_code(qr_code)

            st.image(qr_buffer, use_column_width=True)

if __name__ == '__main__':

    main()



