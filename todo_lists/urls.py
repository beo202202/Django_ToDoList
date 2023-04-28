from django.urls import path
from todo_lists import views

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todolist_view'),
    path('<int:todolist_id>/', views.TodoListDetailView.as_view(), name='todolist_detail_view'),
]
