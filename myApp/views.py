from django.template import loader
from django.http import HttpResponse
from .models import hadith

# Create your views here.
def index(request):
	all_hadiths= hadith.objects.all()
	template = loader.get_template('pages/index.html')
	context={
		'all_hadiths' : all_hadiths,
	}
	return HttpResponse(template.render(context,request))

def book(request, books_id):
	return HttpResponse('<h1>book id is: '+str(books_id)+'</h1>')
def category(request):
	return HttpResponse('<h1>This is a category page</h1>')
def single_category(request, cat_id):
	return HttpResponse('<h1>Category id: '+str(cat_id)+'</h1>')
def login(request):
	template=loader.get_template('pages/login.html')
	context={

	}
	return HttpResponse(template.render(context, request))