
from django import forms

class FormLatter(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()
    text = forms.TimeField()