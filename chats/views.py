from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Chat

def send(request): 
    chat = Chat.objects
    if request.method == 'POST':
        chat.create(
            user = "user",
            message = request.POST['message'],
            attachment_name = "",
            is_sent = 1
        )

        return HttpResponse(request.POST['message'])
    
    return HttpResponse('error')

def receive(request): 
    chat = Chat.objects
    if request.method == 'POST':
        types = request.POST['type']
        chat = Chat.objects.filter(user = "admin", is_sent = 0)

        if chat.count() :
            chat.is_sent = 1
            chat.save()

            return HttpResponse(chat.message)
        return HttpResponse('')
    
    return HttpResponse('error')

def image(request):
    return "image"
    