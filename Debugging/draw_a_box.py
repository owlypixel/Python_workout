import traceback

def print_a_box(symbol, width, height):
	if len(symbol) != 1:
		raise Exception('Symbol needs to be a string with the length 1')
	if (width < 2) or (height < 2):
		raise Exception('Width and height must be greater or equal than 2 ')
	print(symbol * width)
	for i in range(height - 2):
		print(symbol + (' ' * (width - 2)) + symbol)
	print(symbol * width)

try:
	print_a_box('**', 20, 5)
except: 
	error_file = open('error_log.txt', 'a')
	error_file.write(traceback.format_exc())
	error_file.write("-"*60)
	error_file.close()
	print('Traceback info was written to error_log.txt')