from django.conf.urls import url
from . import views


urlpatterns = [
  url(r'^$', views.home,name='home'),
  url(r'^register/', views.register,name='register'),
  url(r'^login/$',views.login,name='login'),
  url(r'^hollywood/', views.hollywood,name='hollywood'),
  url(r'^tollywood/', views.tollywood,name='tollywood'),
  url(r'^bollywood/', views.bollywood,name='bollywood'),
  ]
