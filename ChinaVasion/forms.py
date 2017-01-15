from django import forms
from django.forms import ModelForm

MP4_CHOICES = ('240p', '360p', '720p', '1080p')
class SearchForm(forms.Form):
    Search = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control",'placeholder':'Enter Model Here'}))

class mpForm(forms.Form):
    mpImages = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
    # check this link later:
    #http://stackoverflow.com/questions/19326852/django-iterating-over-checkboxselectmultiple-renders-numbers


