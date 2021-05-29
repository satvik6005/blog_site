from django.conf.urls import url
from blog import views
from django.urls import path

app_name='blog'

urlpatterns=[
    path('list',views.list,name='list'),
    path('view/<int:data>',views.vew,name='view'),
    path('writting',views.writting,name='writting')
]
