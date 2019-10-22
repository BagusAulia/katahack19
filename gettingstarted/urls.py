from django.urls import path, include
from django.contrib import admin
from .views import Index

from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

import hello.views

urlpatterns = [
    # path("", hello.views.index, name="index"),
    # path("db/", hello.views.db, name="db"),
    path('',       Index.as_view(), name="home"),
    path('chat/',  include('chats.urls', namespace="chats")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)