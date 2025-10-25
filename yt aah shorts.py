import qrcode
from PIL import Image

# Create QR code instance
qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

# Add data to QR code
data = "https://www.youtube.com/"
qr.add_data(data)
qr.make(fit=True)

# Create QR code image
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Load YouTube logo image
logo_path = "Youtube_logo.png"  # Make sure this file exists in your working directory
logo = Image.open(logo_path)

# Calculate size and position for the logo
qr_width, qr_height = qr_img.size
logo_size = int(qr_width / 4)  # Resize logo to 1/4th of QR code width
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

# Calculate position to paste the logo (centered)
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# Paste the logo onto the QR code
qr_img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

# Save the final image
qr_img.save("yt.png")
