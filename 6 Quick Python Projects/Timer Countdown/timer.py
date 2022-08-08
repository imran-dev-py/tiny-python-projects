from time import sleep

def countdown(time_in_sec):
	while time_in_sec:
		minutes, seconds = divmod(time_in_sec, 60)
		timer = f'{minutes:02d}:{seconds:02d}'
		print(timer, end='\r')
		sleep(1)
		time_in_sec -= 1
	print('Timer Completed')

seconds = int(input('Enter time in seconds: '))
countdown(seconds)