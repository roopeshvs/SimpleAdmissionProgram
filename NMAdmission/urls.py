from django.conf.urls import url, include
from . import views

urlpatterns = [
    #core_functions
    url(r'',views.home, name="home"),
]