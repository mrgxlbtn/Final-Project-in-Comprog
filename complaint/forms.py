from django import forms
from django.forms import ModelForm, widgets
from .models import Complaint

class ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = "__all__" 
        labels = {
            'name': '',
            'email': '',
            'address': '',
            'subject': '',
            'message': ''
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder':'Name',
                'class': 'form'
                }),
            'email': forms.EmailInput(attrs={
                'name': 'message_email',
                'placeholder':'Email',
                'class': 'form'
                }),
            'address': forms.TextInput(attrs={
                'placeholder':'Address',
                'class': 'form'
                }),
            'subject': forms.TextInput(attrs={
                'name': 'message_subject',
                'placeholder':'Subject of the Complaint',
                'class': 'form'
                }),
            'message': forms.Textarea(attrs={
                'name': 'message',
                'placeholder':'Leave your complaint here',
                'class': 'formBig form'
                }),
        }