from django.urls import path
from . import views

# Template tagging
app_name =  'basicapp'

urlpatterns = [
    path('relative/',views.relative,name = 'relative'),
    path('other/',views.other,name = 'other')
]