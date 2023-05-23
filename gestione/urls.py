from django.contrib import admin
from django.urls import path, include
from .views import *

app_name="gestione"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ciao', home, name="home" )

   ]