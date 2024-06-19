from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # path('clients/products/<int:customer_id>/<int:days_history>', views.user_products, name='user_products'),
    path('user_products/<int:user_id>/', views.user_products, name='user_products'),
    path('user_products/<int:user_id>/upload_image/', views.upload_image, name='upload_image'),
]
