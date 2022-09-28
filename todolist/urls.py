from django.urls import path
from todolist.views import show_todolist
from todolist.views import my_form
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('create-task/', my_form, name='create-forms'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]