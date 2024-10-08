import qrcode

# Function to generate QR code
def generate_qr_code(data, file_name):
    # Create a QR code object with the provided data
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 to 40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box (pixel)
        border=4,  # Thickness of the border
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image to a file
    img.save(file_name)
    print(f"QR Code saved as {file_name}")

# Example usage:
data_to_encode = "https://www.example.com"
file_name = "qrcode_example.png"
generate_qr_code(data_to_encode, file_name)
