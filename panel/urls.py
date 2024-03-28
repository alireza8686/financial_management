from django.urls import path
from .views import panel

urlpatterns = [
    path('<int:user_id>/', panel, name='panel'),
]
