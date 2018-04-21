from django import forms

from .models import NewsItem 


class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsItem
        fields = ['title', 'body']