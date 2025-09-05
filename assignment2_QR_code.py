"""
QR Code Generator Application
Author: Mohit Gokul Murali
Date: Sep 5, 2025
Description: This Python program generates a QR code from the Biox Systems URL.
"""

import qrcode

def generate_qr(url: str, filename: str = "qr_code.png"):
    """
    Generates a QR code from the provided URL and saves it as an image.
    
    Args:
        url (str): The URL to be converted into a QR code.
        filename (str): The filename to save the QR code image.
    """
    try:
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,  # controls size of the QR code
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
            box_size=10,
            border=4
        )
        
        # Add data to the QR code
        qr.add_data(url)
        qr.make(fit=True)

        # Generate image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save QR code image
        img.save(filename)
        print(f"QR code successfully generated for {url} and saved as {filename}")

    except Exception as e:
        print(f"Error generating QR code: {e}")


if __name__ == "__main__":
    # Assignment requirement: Biox Systems website QR code
    url_input = "https://www.bioxsystems.com/"
    generate_qr(url_input)
