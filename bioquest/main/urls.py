from django.urls import path, include
from . import views

from django.conf.urls import url

urlpatterns = [
    path('', views.index, name = 'home'),
    path('dev', views.dev, name = 'develop'),
    path('test', views.test, name = 'testing'),
    path('personal', views.personal, name = 'personal'),
    path('check', views.check, name = 'check'),
    path('tag/<str:slug>/', views.tag_detail, name = 'tag_url'),
    path('tag/<str:slug>/solve', views.check, name = 'tag_url_check'),
    path('instructions', views.instructions,name='instructions'),
    path('dev_cont', views.dev, name='dev_cont'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.user_login, name='login'),
]