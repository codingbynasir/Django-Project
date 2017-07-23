from django.contrib import admin
from .models import books, categories, hadith
# Register your models here.
admin.site.register(books)
admin.site.register(categories)
admin.site.register(hadith)