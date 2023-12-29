
from django.urls import path
from . import views

urlpatterns = [
   path("",views.index,name="index"),
   path("getresponse/",views.getresponse,name="getresponse"),

]
