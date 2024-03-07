from django.contrib import admin
from django.urls import path
from main.views import main

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main),
]
