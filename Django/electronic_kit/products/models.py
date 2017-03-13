from django.db import models

class Product(models.Model):
	title = models.CharField(max_length=150)
	description = models.TextField(help_text="Full product description")
	categories = models.ManyToManyField("Category", related_name="products")
	date = models.DateTimeField(blank=True, null=True)
	is_new = models.BooleanField(default=False, verbose_name="Is this shit new?")

	def __str__(self):
		return self.title

class Category(models.Model):
	title = models.CharField(max_length=150, help_text="Category title", unique=True)

	def __str__(self):
		return self.title