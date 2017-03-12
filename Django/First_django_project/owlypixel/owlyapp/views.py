from django.shortcuts import render

def homepage(request):
	context = {'a': 123}
	name = 'owlyapp/home.html'
	return render(request, name, context)


def greet(request, name):
	return render(request, 'owlyapp/greet.html', {'name': name})
