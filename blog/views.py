from django.http import HttpResponse
from django.shortcuts import render, loader
from .forms import ContactForm


# Create your views here.


def index(request, *args, **kwargs):
    return render(request, 'blog/index.html')

def about(request, *args, **kwargs):
    return render(request, 'blog/about.html')

def blog(request, *args, **kwargs):
    return render(request, 'blog/blog.html')

def post(request, *args, **kwargs):
    return render(request, 'blog/single-blog.html')

def portfolio(request, *args, **kwargs):
    return render(request, 'blog/portfolio.html')

def contact(request, *args, **kwargs):
    return render(request, 'blog/contact.html')


def product_create_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, "blog/form.tpl", context)

