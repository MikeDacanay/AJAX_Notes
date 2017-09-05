from django.conf.urls import url, include
from . import views

urlpatterns = [
    url( r'^$' , views.index),
    url( r'^title$' , views.title),
    url( r'^delete_form$' , views.delete),
    url( r'^texter$' , views.texter),
]