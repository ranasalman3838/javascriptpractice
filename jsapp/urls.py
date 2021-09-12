from django.urls import path
from .import views

urlpatterns = [
    path('',views.base,name="base"),
    path('day1',views.day1 ,name='day1'),
    path('day2',views.day2 ,name='day2'),
    path('day3',views.day3 ,name='day3'),
    path('day4',views.day4 ,name='day4'),
]