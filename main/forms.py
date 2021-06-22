from django import forms
from .models import Image
from django.forms import TextInput


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')
        widgets = {
            'name': TextInput(attrs={
                'class':"form-control",
                'style':'margin-left:100px;'
            })
        }
