from django.urls import path
from django.conf.urls import include, url
from . import views
app_name='posts'

urlpatterns=[
    path("",views.startt,name='startt'),
    path("index",views.index,name = 'index'),
    path("<int:person_id>",views.Blogs,name='Blogs'),
]
