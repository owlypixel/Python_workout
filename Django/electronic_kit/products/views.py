from django.shortcuts import render
from .models import Product
# from django.http import HttpResponse

# Create your views here.
def list_products(request):
	"""
	List all products

	"""
	products = Product.objects.all().prefetch_related('categories')

	context = {
		'products': products,
	}
	return render(request, 'list.html', context)