from django.contrib import admin
from todo_list.models import TodoList

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(TodoList)
