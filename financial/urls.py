from django.urls import path
from .views import create_cost, create_thing, create_category


urlpatterns = [
    path('create_cost/<int:user_id>/', create_cost, name='create_cost'),
    path('create_thing/<int:user_id>/', create_thing, name='create_thing'),
    path('create_category/<int:user_id>/', create_category, name='create_category'),
]
