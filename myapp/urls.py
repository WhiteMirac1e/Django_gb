from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('add_product/', views.add_product, name='add_product'),
    path('show_product/<int:user_id>/', views.show_product, name='show_product'),
]
