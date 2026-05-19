from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='aboutus'),
    path('chicken/', views.chicken, name='chicken'),
    path('cows/', views.cows, name='cows'),
    path('crop/', views.crop, name='crop'),
    path('customer/', views.customer, name='customer'),
    path('ducks/', views.ducks, name='ducks'),
    path('goat/', views.goat, name='goat'),
    path('goose/', views.goose, name='goose'),
    path('groundnuts/', views.groundnuts, name='groundnuts'),
    path('apiculture/', views.apiculture, name='apiculture'),
    path('livestock/', views.livestock, name='livestock'),
    path('onion/', views.onion, name='onion'),
    path('poultry/', views.poultry, name='poultry'),
    path('sheep/', views.sheep, name='sheep'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('watermelon/', views.watermelon, name='watermelon'),
    path('pay', views.pay, name='pay'),
    path('mpesa/callback/', views.mpesa_callback, name='mpesa_callback'),
]