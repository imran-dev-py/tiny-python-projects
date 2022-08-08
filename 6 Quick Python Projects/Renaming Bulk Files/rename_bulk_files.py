import os 

def renaming(path, names):
	for index, filename in enumerate(os.listdir(path)):
		extension = filename.split('.')[1]
		new_filename = f'{names[index]}.{extension}'
		old_dir = f'{path}{filename}'
		new_dir = f'{path}{new_filename}'
		os.rename(old_dir, new_dir)

if __name__ == '__main__':
	path = r"F:/Upload/temp/"
	names = ["Python Design Patters Playbook","Python Coding Interviews-Tips & Best Practices", "Structuring a Python Application"]
	renaming(path, names)