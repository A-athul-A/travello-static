from django.urls import path

from newProjectapp import views

urlpatterns = [

    path('', views.my_func, name='my_func'),
    path('about/', views.about, name='about'),

]
