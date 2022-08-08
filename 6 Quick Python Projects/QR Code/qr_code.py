import os
import qrcode

def generate_qrcode(data, image_name, extension):
	image = qrcode.make(data=data)
	image.save(f'{os.getcwd()}/{image_name}.{extension}')

text = input("Enter the text for put inside QR: ")
image_name, extension = input('Enter filename with extension: ').split('.')
generate_qrcode(text, image_name, extension)
print("QR Code Successfully Generated")