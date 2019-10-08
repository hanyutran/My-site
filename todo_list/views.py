from django.shortcuts import render, redirect, get_object_or_404
from todo_list.models import TodoList
from django.urls import reverse

def create_todolist(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        note =  request.POST.get('note')
        begin_time = request.POST.get('begin_time')
        end_time = request.POST.get('end_time')
        todo = TodoList(title = title,
                        note = note,
                        begin_time = begin_time,
                        end_time = end_time)
        todo.save()
        return redirect('todo_list:todolist_index')

    todo = TodoList.objects.all().order_by('created_time')    
    context = {
        "todolists": todo,
    }
    return render(request, "todo_list/todolist.html", context)


def remove_todolist(request, pk):
    todolist = get_object_or_404(TodoList, pk=pk)
    todolist.delete()

    return redirect('todo_list:todolist_index')

def done_todolist(request, pk):
    todolist = get_object_or_404(TodoList, pk=pk)
    todolist.done = True
    todolist.save()

    return redirect('todo_list:todolist_index')
    