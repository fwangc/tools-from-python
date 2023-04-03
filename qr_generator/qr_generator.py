import qrcode

# input URL
url = input("Enter your target URL: ")
# url = "https://www.example.com/"

# generate QR code
img = qrcode.make(url)

# save the QR code as a PNG file
img.save("qr_code.png")