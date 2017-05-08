from django.shortcuts import render
from .models import Product, Category
from django.views.generic import View, DetailView
from django.db.models import Count
# from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import ProductSerializer, CategorySerializer

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

#API - Lists all products or creates a new one
class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


