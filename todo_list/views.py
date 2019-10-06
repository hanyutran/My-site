from django.shortcuts import render, redirect
from todo_list.models import TodoList

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
    