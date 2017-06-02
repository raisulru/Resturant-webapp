from django.db import models
from django.core.urlresolvers import reverse


class SliderImage(models.Model):
	name = models.CharField(max_length=100,db_index = True, blank=True)
	image = models.ImageField(upload_to = 'slider/%Y/%m/%d',height_field=None, width_field=None, blank =  False)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

class GallaryImage(models.Model):
	name = models.CharField(max_length=100, db_index=True)
	image = models.ImageField(upload_to = 'slider/%Y/%m/%d', blank =  False)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)


class Category(models.Model):
	name = models.CharField(max_length = 200,db_index = True)
	slug = models.SlugField(max_length = 200, db_index = True, unique = True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'Category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name
	#reverse function
	def get_absolute_url(self):
		return reverse('homepage:food_list_by_category',
						args=[self.slug])

class Food(models.Model):
	category = models.ForeignKey(Category, related_name = 'foods')
	name = models.CharField(max_length = 200, db_index = True)
	slug = models.SlugField(max_length = 200, db_index = True)
	image = models.ImageField(upload_to = 'food/%Y/%m/%d', blank =  True)
	description = models.TextField(blank = True)
	available = models.BooleanField(default = True)
	price = models.DecimalField(max_digits = 10, decimal_places = 2)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)

	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)
		 
	def __str__(self):
		return self.name


class TableDescription(models.Model):
	description = models.CharField(max_length=200, db_index=True)


class Table(models.Model):
	category = (
		('IN', 'Indoor'),
		('OUT', 'Outdoor'),
	)
	table_places = models.CharField(max_length=9, choices=category, default='Indoor')
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to = 'Table/%Y/%m/%d')
	available = models.BooleanField(default = True)
	price = models.DecimalField(max_digits = 10, decimal_places = 2)
	description = models.ManyToManyField(TableDescription)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)
