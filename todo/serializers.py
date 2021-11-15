from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from todo.models import Todo

""" serialiers is used to handle commninication between views and model
so that they can both understand each other. convert Json file into python code and vece versa """

class TodaSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title', 'desc', 'is_complete')
