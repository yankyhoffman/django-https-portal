from django import forms


class MessageForm(forms.Form):
    message = forms.CharField(required=True, max_length=255)
