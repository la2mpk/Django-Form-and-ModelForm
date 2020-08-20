from django.shortcuts import render, redirect
from . import forms
from .models import Snippet


def index(request):
    return render(request, 'base.html')

def form(request):

    form = forms.ContactForm()

    if request.method == 'POST':
        form = forms.ContactForm(request.POST)

        if form.is_valid():

            name_data = form.cleaned_data['name']
            body_data = form.cleaned_data['email']
            
            Snippet.objects.create(name=name_data, body=body_data).save()

        return redirect('myapp:form')

    context = {'form': form}
    return render(request, 'myapp/form.html', context)


def model_form(request):

    form = forms.SnippetForm()

    if request.method == 'POST':
        form = forms.SnippetForm(request.POST)

        if form.is_valid():

            form.save()
        
        return redirect('myapp:model_form')
    
    context = {'form': form}
    return render(request, 'myapp/form.html', context)
