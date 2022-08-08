import os

def file_renaming(path, file):
	with open(file) as file:
		for filename in os.listdir(path):
			new_name = file.readline().strip()
			old_location = f'{path}{filename}'
			new_location = f'{path}{new_name}'
		try:
			os.rename(old_location, new_location)
		except FileExistsError as e:
			print('Renaming Already done')

if __name__ == '__main__':
	path = r"F:/Upload/temp/"
	file = 'abc.txt'
	file_renaming(path, file)
