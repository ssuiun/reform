from django import forms

class LinkForm(forms.Form):
    link = forms.URLField()
    link.widget.attrs.update({
        "class": 'Form-control',
        'placeholder': "Please enter link"})