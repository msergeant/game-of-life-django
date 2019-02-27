from django.urls import path

from . import views

app_name = 'worlds'
urlpatterns = [
    path('next', views.next_world, name='vote'),
]
