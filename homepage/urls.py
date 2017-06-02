from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomeView, name='HomeView'),
    url(r'^food/$', views.FoodView, name='FoodView'),
    url(r'^reservation/$', views.TableView, name='TableView'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.FoodView, name='food_list_by_category'),
]