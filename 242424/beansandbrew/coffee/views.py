from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import MenuItem, Contact, Message

def index(request):
    return render(request, 'coffee/index.html')

def menu(request):
    search = request.GET.get('search', '')
    category = request.GET.get('category', '')

    items = MenuItem.objects.all()

    if search:
        items = items.filter(name__icontains=search)
    if category:
        items = items.filter(category=category)

    return render(request, 'coffee/menu.html', {
        'items': items,
        'search': search,
        'category': category
    })

def contact(request):
    contact = Contact.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name')
        msg = request.POST.get('message')

        if name and msg:
            Message.objects.create(name=name, message=msg)

    return render(request, 'coffee/contact.html', {'contact': contact})

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('index')
    return render(request, 'coffee/register.html', {'form': form})

def login_view(request):
    form = AuthenticationForm(data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        return redirect('index')
    return render(request, 'coffee/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')