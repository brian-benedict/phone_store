from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('phone/<int:phone_id>/', views.phone_details, name='phone_details'),
    path('contact/', views.contact_us, name='contact_us'),
    path('about/', views.about_us, name='about_us'),
    path('product-registration/', views.product_registration, name='product_registration'),
    # Additional paths can be added here for more views
]

