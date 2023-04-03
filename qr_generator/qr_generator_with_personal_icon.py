import qrcode
from PIL import Image

# input URL
url = input("Enter your target URL: ")
# url = "https://www.example.com/"

# generate QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(url)
qr.make(fit=True)
img_qr = qr.make_image(fill_color="black", back_color="white")

# open the persona icon image
img_icon = Image.open("personal_icon.png")

# resize the icon to fit the QR code
img_icon = img_icon.resize((80, 80))

# calculate the position of the icon in the QR code
pos = ((img_qr.size[0] - img_icon.size[0]) // 2, (img_qr.size[1] - img_icon.size[1]) // 2)

# paste the icon on the QR code
img_qr.paste(img_icon, pos)

# save the QR code as a PNG file
img_qr.save("qr_code.png")