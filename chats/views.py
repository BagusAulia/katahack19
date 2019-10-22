from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Chat

from io import BytesIO
from PIL import Image
import requests
import pytesseract

def send(request): 
    chat = Chat.objects
    if request.method == 'POST':
        chat.create(
            user = "user",
            message = request.POST['message'],
            is_sent = 1
        )

        url      = 'https://kanal.kata.ai/receive_message/b2541886-e3b7-4de3-96c7-9cb06c0acc58'
        # url      = endpoint.format(source_lang='en', word_id=word)
        headers  = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization' : 'Bearer RayleighPlasma'}
        response = requests.get(url, headers=headers)

        return HttpResponse(response)
    
    return HttpResponse('error')

def receive(request): 
    if request.method == 'POST':
        types = request.POST['type']
        chatss = Chat.objects.filter(user = "admin", is_sent = 0)

        if chatss.count() :
            for chat in chatss :
                chat.is_sent = 1
                chat.save()

            return HttpResponse(chat.message)
        return HttpResponse('')
    
    return HttpResponse('error')

def attachment(request):
    if request.method == 'POST':
        chats = Chat.objects.filter(user = "user", is_sent = 0)

        if chats.count() :
            for chat in chats :
        
                if chat.attachment :
                    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
                    response   = requests.get("https://warm-citadel-64062.herokuapp.com" + chat.attachment.url)
                    # response   = requests.get("http://localhost:5000" + chat.attachment.url)
                    img        = Image.open(BytesIO(response.content))
                    transcript = pytesseract.image_to_string(img)
                    
                    chat.message = transcript
                    chat.is_sent = 1
                    chat.save()

                    return JsonResponse({'transcript' : transcript, 'img_url' : chat.attachment.url})

            return HttpResponse('')
            # return HttpResponse(chats.attachment.url)
			
        return HttpResponse('')
    
    return HttpResponse('error')
