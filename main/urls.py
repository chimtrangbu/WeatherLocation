from django.conf.urls import url
from django.contrib import admin
from main import views

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.home, name='home'),
  url(r'^get_weather_from_ip/', views.get_weather_from_ip, name="get_weather_from_ip"),
]
