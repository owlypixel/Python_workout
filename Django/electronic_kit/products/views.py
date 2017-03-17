from django.shortcuts import render
from .models import Product, Category
from django.views.generic import View, DetailView
from django.db.models import Count
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

class CategoriesList(View):
	def get(self, request):
		categories = Category.objects.annotate(
			all_products = Count('products')
		)

		context = {
			'categories': categories,
		}

		return render(request, 'categories.html', context)

class ProductDetail(DetailView):
	model = Product
	template_name = 'product.html'

class CategoryDetail(DetailView):
	model = Category
	template_name = 'category.html'