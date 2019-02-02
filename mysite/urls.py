"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from movie_site import views


admin.site.site_header = "FILM CAST"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('movie_site.urls', namespace="movie_site")),
    url(r'^logout/$',views.logout_view,name="logout"),
    url(r'^register/', views.register,name='register'),
    url(r'^logged_in/$',views.logged_in,name='login'),
    url(r'^search/$',views.search_movie,name="search"),
    url(r'^player/', views.player,name='player'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

