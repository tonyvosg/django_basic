from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path("<str:name>", views.greet, name="greet"),
    path("", views.index),
    path("brian", views.brian, name="brian"),
    path("david", views.david, name="david"),
]
