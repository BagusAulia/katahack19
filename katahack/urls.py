from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('',       views.index, name="home"),
    path('chat/',  include('chats.urls', namespace="chats")),
    path('admin/', admin.site.urls),
]
