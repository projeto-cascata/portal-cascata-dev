from django import forms

from .models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'uploaded_file']