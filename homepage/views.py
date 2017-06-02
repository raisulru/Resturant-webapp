from django.shortcuts import render, get_object_or_404
from homepage.models import SliderImage, GallaryImage, Category, Food, TableDescription, Table

def HomeView(request):
	slider = SliderImage.objects.all()
	gallary = GallaryImage.objects.all()
	lastimage = gallary.latest('id')
	return render(request,'homepage/homepage.html', {'slider': slider, 'gallary': gallary, 'lastimage': lastimage})

def FoodView(request, category_slug = None):
	category = None
	categories = Category.objects.all()
	foods = Food.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug = category_slug)
		foods = foods.filter(category=category)
	return render(request,'homepage/food.html',{'category': category,'categories': categories,'foods': foods})

def TableView(request):
	tables = Table.objects.all()
	InTables = Table.objects.all().filter(table_places = 'Indoor')
	context = {}
	template = 'homepage/table.html'
	return render(request,template, context)