from django import forms
from django.forms import ModelForm

class SearchForm(forms.Form):
    Search = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control",'placeholder':'Enter Model Here'}))


