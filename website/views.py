from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages
from django.views import View
def index_view(request) :
    return render(request, "website/index.html")

def about_view(request) :
    return render (request, "website/about.html")

def contact_view(request) :
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.cleaned_data['name'] = 'Unknown'
            
            contact = form.save(commit=False)
            contact.name = form.cleaned_data['name']
            contact.subject = form.cleaned_data['subject']
            contact.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited successfully .')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt submited successfully .')

    form = ContactForm ()        
    return render (request, 'website/contact.html', {'form': form})


def newsletter_view(request) :
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your email address submited successfully .')
            return HttpResponseRedirect('/')

    else :
        messages.add_message(request,messages.ERROR,'your email address did not submited successfully .')
        return HttpResponseRedirect('/')




class ComingSoonView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h1> our website will available coming soon :) </h1>')



