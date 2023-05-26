import streamlit as st

import qrcode

def generate_qr_code(data):

    qr = qrcode.QRCode(version=1, box_size=10, border=5)

    qr.add_data(data)

    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")

    return qr_img

def main():

    st.title("QR Code Generator")

    st.write("Enter text or URL to generate a QR code")



    input_data = st.text_input("Enter text or URL")

    if st.button("Generate QR Code"):

        if input_data:



            qr_code = generate_qr_code(input_data)



            st.image(qr_code)

if __name__ == '__main__':

    main()

