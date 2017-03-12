from django.db import models

class Book(models.Model):
	# identificator = models.AutoField(primary_key=True)
	title = models.CharField(max_length=50, null=True)
