from django.conf.urls import url
from testapp import views

urlpatterns = [
  url(r'^keyboard/?$', views.keyboard),
  url(r'^keyboard2/?$', views.keyboard2),
  url(r'^message', views.message)
]