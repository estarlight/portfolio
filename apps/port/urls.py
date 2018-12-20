from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^projects/travel_itineraries', views.travel_itineraries),
    url(r'^projects/skin_deep', views.skin_deep),
    url(r'^projects/handy_helper', views.handy_helper),
    url(r'^projects/restaurant_reviewer', views.restaurant_reviewer),
    url(r'^projects/courses', views.courses),
    url(r'projects/justyoufitness', views.justyoufitness),


]