import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from todolist.models import Task
from todolist.forms import TaskForms
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/todolist/login/')

def show_todolist(request):
    data_todolist_item = Task.objects.all()
    current_user = request.user.username
    context = {
        'list_item': data_todolist_item,
        'last_login': request.COOKIES['last_login'],
        'user':current_user,
    }
    return render(request, "todolist.html",context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('todolist:login')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # login first
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # create response
            response.set_cookie('last_login', str(datetime.datetime.now())) # create last_login cookie and add it to response
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return redirect('todolist:login')

def my_form(request):
  form = TaskForms()
  if request.method == "POST":
    form = TaskForms(request.POST)
    if form.is_valid():
      last_user = form.save()
      last_user.user = request.user
      last_user.save()
      return redirect('todolist:show_todolist')
  return render(request, 'cv-form.html', {'form': form})
