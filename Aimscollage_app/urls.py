
from django.urls import path
from . import views

app_name = "Aimscollage_app"

urlpatterns = [
    path('',views.demo,name="demo"),
    path('about',views.about,name="about"),
    path('staffs',views.staff,name="staffs"),
    path('events',views.events,name="events")

]