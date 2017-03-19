from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
	fieldsets = [
		('Product details', {'fields': ['title', 'categories', 'description', 'image']}),
		('Is new', {'fields': ['is_new', 'date']})
	]

	readonly_fields = ("date",)

	def product_categories(self, obj):
		return obj.list_categories()

	list_display = ('title', 'product_categories', 'date', 'is_new', 'image')
	list_editable = ('is_new',)
	list_display_links = ('title', 'date')
	list_filter = ('is_new',)
	search_fields = ('title', 'categories__title')

# Register your models here.
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
