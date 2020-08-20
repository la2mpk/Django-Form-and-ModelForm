from django import forms
from . import models


class ContactForm(forms.Form):
    categories = [
        ('question', 'Question'),
        ('other', 'Other')
    ]

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    category = forms.ChoiceField(choices=categories, widget=forms.Select(attrs={'class':'form-control'}))
    subject = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class SnippetForm(forms.ModelForm):

    class Meta:
        model = models.Snippet
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
