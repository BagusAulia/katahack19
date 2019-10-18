from django.urls import path, include
from django.contrib import admin
from . import views

admin.autodiscover()

import hello.views

urlpatterns = [
    # path("", hello.views.index, name="index"),
    # path("db/", hello.views.db, name="db"),
    path('',       views.index, name="home"),
    path('chat/',  include('chats.urls', namespace="chats")),
    path("admin/", admin.site.urls),
]
