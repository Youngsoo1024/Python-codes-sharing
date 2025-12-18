import qrcode

# Data to be encoded in the QR code
data = "https://www.youtube.com/@bdokim6396" 

# Generate QR code
img = qrcode.make(data)

# Save the QR code as an image file (e.g., PNG)
img.save("bdokim_qrcode.png") 