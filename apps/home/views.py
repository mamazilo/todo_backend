from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from apps.notes.models import Todo
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def home_page(request: Request):
    todos = list(Todo.objects.order_by('priority').all().values('title'))
    #pagination -
    return Response({'todos': todos}, status.HTTP_200_OK)