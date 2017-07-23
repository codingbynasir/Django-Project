from django.db import models

# Create your models here.
class books(models.Model):
	book_name=models.CharField(max_length=220, blank=False, null=False)
	book_author=models.CharField(max_length=200, blank=False, null=False)
	def __str__(self):
		return self.book_name
class categories(models.Model):
    category_name=models.CharField(max_length=200, blank=False, null=False)
    description=models.TextField(blank=True, null=True)
    def __str__(self):
    	return self.category_name

class hadith(models.Model):
	body = models.TextField(blank=False, null=False)
	translate = models.TextField(blank=False, null=False)
	book_name=models.ManyToManyField(books)
	cat_name=models.ManyToManyField(categories)
	def __str__(self):
		return self.translate[0:100]