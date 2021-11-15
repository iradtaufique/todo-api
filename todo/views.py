from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from todo.models import Todo

from todo.serializers import TodaSerializer


""" CreateAPIView is used to handle post request"""
class CreateTodoAPIView(CreateAPIView):
    serializer_class = TodaSerializer

    """permission_class is used to handle permission or login required"""
    permission_classes = (IsAuthenticated,)

    """assign todo to the login user"""
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


"""ListAPIView is used to handle or retrieve data from db """
class TodoListAPIView(ListAPIView):
    serializer_class = TodaSerializer
    permission_class = (IsAuthenticated,)

    """retrieve todos assigned to user"""
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)



"""This view will create and list todos at the same time"""
class CreateListTodos(ListCreateAPIView):
    serializer_class = TodaSerializer
    permission_class = (IsAuthenticated,)

    """retrieve todos assigned to user"""
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

    """assign todo to the login user"""
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodaSerializer
    permission_class = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

