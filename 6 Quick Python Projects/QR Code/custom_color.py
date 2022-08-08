import os
import qrcode

def generate_customColor_qrcode(data, image_name, extension):
	qr = qrcode.QRCode(
		version=1,
		error_correction=qrcode.constants.ERROR_CORRECT_L,
		box_size=10,
		border=2,
	)
	qr.add_data(data)
	qr.make(fit=True)
	img = qr.make_image(fill_color='grey', back_color='white')
	img.save(f'{os.getcwd()}/{image_name}.{extension}')

text = input("Enter the text for put inside QR: ")
image_name, extension = input('Enter filename with extension: ').split('.')
generate_customColor_qrcode(text, image_name, extension)
print("QR Code Successfully Generated")