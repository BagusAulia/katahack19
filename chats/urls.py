from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'chats'

urlpatterns = [
    path('send/',       views.send,       name='send'),
    path('receive/',    views.receive,    name='receive'),
    path('attachment/', views.attachment, name='attachment'),
]
