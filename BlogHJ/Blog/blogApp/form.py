from django import forms
from .models import Blog

class LionForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']


class EditForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'pub_date', 'body']