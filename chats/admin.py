from django.contrib import admin
from .models import Chat

class ChatAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'message', 'created_at' ]
    
admin.site.register(Chat, ChatAdmin)
# Register your models here.
