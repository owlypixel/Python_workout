from django.db import models
from django.utils.timezone import now

class Product(models.Model):
	title = models.CharField(max_length=150)
	description = models.TextField(help_text="Full product description")
	categories = models.ManyToManyField("Category", related_name="products")
	date = models.DateTimeField(blank=True, null=True)
	is_new = models.BooleanField(default=False, verbose_name="Is this shit new?")
	image = models.FileField( blank=True)

	def __str__(self):
		return "{} in categories: {}".format(self.title, self.list_categories())

	def list_categories(self):
		return ', '.join([category.title for category in self.categories.all()])

	def save(self, *args, **kwargs):
		self.date = now()

		super(Product, self).save(*args, **kwargs)

class Category(models.Model):
	title = models.CharField(max_length=150, help_text="Category title", unique=True)

	def __str__(self):
		return self.title