from django.urls import path
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    path(r'register/',views.register,name='register'),
    path(r'userLogin/',views.userLogin,name='userLogin'),
]