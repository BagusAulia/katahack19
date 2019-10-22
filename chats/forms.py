from django import forms
from .models import Chat

class ChatForm(forms.ModelForm):
    attachment = forms.ImageField()
    user       = forms.CharField(widget=forms.HiddenInput(), initial="user", required=False)
    message    = forms.CharField(widget=forms.HiddenInput(), initial="-", required=False)
    is_sent    = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)

    class Meta:
        model  = Chat
        fields = ['attachment', 'user', 'message', 'is_sent']