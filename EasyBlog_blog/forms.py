

from django import forms
from django.forms import ModelForm, TextInput
from EasyBlog_blog.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "title", "message"]
        widgets = {
            'name': TextInput(attrs={'id': 'input_name', 'class': 'form-control', 'name': 'your-name', 'placeholder': 'Name'}),
            'email': TextInput(attrs={'id': 'input_email', 'class': 'form-control', 'name': 'your-email', 'placeholder': 'Email'}),
            'subject': TextInput(attrs={'id': 'subject', 'class': 'form-control', 'name': 'your-subject', 'placeholder': 'Subject'}),
            'message': TextInput(attrs={'id': 'subject', 'class': 'form-control', 'name': 'your-message', 'placeholder': 'Message'}),
        }
