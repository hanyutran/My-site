from django.urls import path
from . import views

app_name = 'todo_list'

urlpatterns = [
    path("", views.create_todolist, name="todolist_index"),
    path('todo/<int:pk>/remove', views.remove_todolist, name='todo_remove'),
    path('todo/<int:pk>/done', views.done_todolist, name='todo_done')
]