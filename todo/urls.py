from django.urls import path
from todo.views import (CreateTodoAPIView, TodoListAPIView, CreateListTodos,
                        TodoDetailAPIView)

urlpatterns = [
    path('create-todo', CreateTodoAPIView.as_view(), name='create_todo'),
    path('list-todo', TodoListAPIView.as_view(), name='list_todos'),

    path('list-create-todos', CreateListTodos.as_view(), name='list_create_todos'),
    path('<int:id>', TodoDetailAPIView.as_view(), name='todos_details'),
    

]