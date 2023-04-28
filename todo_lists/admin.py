from django.contrib import admin

from todo_lists.models import TodoList


class TodoListAdmin(admin.ModelAdmin):
    list_display = ('user','title','is_complate','created_at','updated_at','completion_at')

admin.site.register(TodoList, TodoListAdmin)