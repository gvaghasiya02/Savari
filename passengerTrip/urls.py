from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="passenger_home"),
    path('book/',views.bookRide,name="book_ride"),
    path('confirm/<int:pk>/',views.confirmRide,name="confirm_ride"),
]
