from django.urls import path,re_path
from basicapp import views

app_name = 'basicapp'

urlpatterns=[
    path(r'',views.SchoolListView.as_view(),name='list'),
    # pk: primaryKey
    re_path(r'^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name='detail'),
    path(r'create/',views.SchoolCreateView.as_view(),name='create'),
    re_path(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='update'),
    re_path(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='delete'),
]