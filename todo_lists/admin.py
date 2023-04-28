from django.contrib import admin

from todo_lists.models import TodoList


class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title','user','is_complate','created_at','updated_at','completion_at')
    
    fieldsets = (
        ('Todo', {
            'fields': ('title',)
        }),
        ('작성자', {
            'fields': ('user',)
        }),
        ('완료 여부', {
            'fields': ('is_complate', 'completion_at')
        }),
    )

admin.site.register(TodoList, TodoListAdmin)