from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='pageone_home'),
]