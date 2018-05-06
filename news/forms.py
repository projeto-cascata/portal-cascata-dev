from django import forms
from django.contrib.auth.models import Group

from tinymce import TinyMCE

from .models import NewsItem 


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class NewsForm(forms.ModelForm):
    body = forms.CharField(
        widget = TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    visible_to = forms.ModelMultipleChoiceField(
        queryset = Group.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

    class Meta:
        model = NewsItem
        fields = ['title', 'body', 'visible_to']