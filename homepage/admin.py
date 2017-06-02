from django.contrib import admin
from .models import SliderImage, GallaryImage, Category, Food, Table, TableDescription

class SliderImageAdmin(admin.ModelAdmin):
	list_display = ['name']
admin.site.register(SliderImage, SliderImageAdmin)

class GallaryImageAdmin(admin.ModelAdmin):
	list_display = ['name']
admin.site.register(GallaryImage, GallaryImageAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class FoodAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
	list_filter = ['available', 'created', 'updated']
	list_editable = ['price', 'available']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Food, FoodAdmin)

class TableAdmin(admin.ModelAdmin):
	list_display = ['name', 'price', 'available']
	list_filter = ['available']
	list_editable = ['price', 'available']
admin.site.register(Table, TableAdmin)

class DescriptionAdmin(admin.ModelAdmin):
	list_display = ['description']
admin.site.register(TableDescription, DescriptionAdmin)