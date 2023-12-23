from django.urls import path

from . import views

app_name = 'apartments'

urlpatterns = [
    path('/', views.apartments, name='all_apartments'),
    path('/<str:category_id>/', views.apartments, name='category'),
    path('/<int:apartment_id>', views.single_apartment, name='single_apartment')
]
