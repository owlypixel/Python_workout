import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	query = ' '.join(sys.argv[1:])
else:
	query = pyperclip.paste()
webbrowser.open('http://codepen.io/search/pens?q=' + query)
