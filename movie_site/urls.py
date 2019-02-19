from django.conf.urls import url
from . import views




urlpatterns = [
  url(r'^home/$', views.home,name='home'),
  url(r'^hollywood/', views.hollywood,name='hollywood'),
  url(r'^tollywood/', views.tollywood,name='tollywood'),
  url(r'^bollywood/', views.bollywood,name='bollywood'),
  url(r'^player/', views.player,name='player'),
  url(r'^contact/$',views.contact,name="contact"),
  ]
