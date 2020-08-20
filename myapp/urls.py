from django.urls import path
from . import views


app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('model_form/', views.model_form, name='model_form')
]
