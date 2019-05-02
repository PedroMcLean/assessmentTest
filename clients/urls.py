from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'clients'

urlpatterns = [
    path('', views.clients, name="list"),
]

urlpatterns += staticfiles_urlpatterns()
