import pyqrcode
import cv2
from pyzbar import pyzbar

print('welcome to pyQR')
ccc = input('write 1 if you want to generate QR code, or write 2 if you want to read QR code: ')

if ccc == '1':
    x = input('please write your data that you want on your QR code: ')

    # Generate QR code
    data = x
    qr = pyqrcode.create(data)

    # Save QR code as an image file
    qr.png("qr_code.png", scale=6)
else:
    if ccc == '2':
        input('rename your QR code to "qr_code.png" and put it to this folder, then press [ENTER]')
        # Read image
        image = cv2.imread("qr_code.png")

        # Find and decode QR codes
        barcodes = pyzbar.decode(image)

        # Iterate over detected QR codes
        for barcode in barcodes:
            data = barcode.data.decode("utf-8")
            print("QR Code:", data)
input()
