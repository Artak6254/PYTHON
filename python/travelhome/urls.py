from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('book/', views.book, name='book'),
    path('success/<int:booking_id>/', views.success, name='success'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/<int:contact_id>/', views.contact_success, name='contact_success'),
]