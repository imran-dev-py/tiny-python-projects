from PIL import Image
from pyzbar.pyzbar import decode
from os import getcwd

def decode_image(image):
	try:
		img = Image.open(f'{getcwd()}/{image}')
	except FileNotFoundError:
		print('File not found, make sure you inserted correct file')
	else:
		decoding_message = decode(img)
		string = decoding_message[0][0].decode('utf-8')
		return string

img = input('Enter the image name: ')
message = decode_image(img) or ''
print(f'Decoded Message is `{message}`')