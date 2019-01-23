from django.contrib import messages
from django.shortcuts import render
from .models import Contact, Post
import requests


def index(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        result = requests.get(
            'http://api.icndb.com/jokes/random?firstName='+first_name+'&lastName='+last_name).json()

        context = {
            'joke': result
        }

        return render(request, 'mysite/index.html', context)
    else:
        first_name = 'Mahmudul'
        last_name = 'Alam'

        result = requests.get(
            'http://api.icndb.com/jokes/random?firstName='+first_name+'&lastName='+last_name).json()

        context = {
            'joke': result
        }

        return render(request, 'mysite/index.html', context)


def portfolio(request):
    posts = Post.objects.all()
    return render(request, 'mysite/portfolio.html', {'posts': posts})


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, 'Email sent successfully',
                         extra_tags='alert-success')
        return render(request, 'mysite/contact.html')
    else:
        return render(request, 'mysite/contact.html')
