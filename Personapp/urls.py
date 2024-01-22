from django.urls import path
from . import views

app_name = 'Personapp'

urlpatterns = [
    path('',views.Create_Person,name="person_add"),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'), # AJAX
    path('order_confirm',views.Confirm,name='order_confirm')
]