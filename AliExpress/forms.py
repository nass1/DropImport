from django import forms

class SearchForm(forms.Form):
    Search = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control",'placeholder':'Enter Model Here'}), required=False)
