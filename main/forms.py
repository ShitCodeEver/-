from django import forms

class FormLatter(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': 'form-control'}))
    surname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ваша фамилия', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Ваш Email', 'class': 'form-control'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ваш Email', 'class': 'form-control', 'rows': 5}))