from rest_framework.request import Request
from rest_framework.response import Response
from .models import Todo
from rest_framework import status
# from rest_framework.decorators import api_view
from .serializers import TodoSerializer
from rest_framework.views import APIView
# from rest_framework import generics
# from rest_framework import viewsets
from apps.utils.paginations import NotePagination


#region class base view

class NoteList(APIView):
    pagination_class = NotePagination
    def get(self, request: Request):
        todos = Todo.objects.order_by('id').all()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class NoteEditeList(APIView):
    pagination_class = NotePagination
    def get_object(self, todo_id:int):
        try:
            note = Todo.objects.get(pk=todo_id)
            return note
        except:
            return None

    def get(self, request: Request, todo_id: int):
        todo = self.get_object(todo_id)
        if todo is None:
            return Response({'detail': 'object not found'}, status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request: Request, todo_id:int):
        todo = self.get_object(todo_id)
        if todo is None:
            return Response({'detail': 'object not found'}, status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, todo_id:int):
        todo = self.get_object(todo_id)
        if todo is None:
            return Response({'detail': 'object not found'}, status.HTTP_404_NOT_FOUND)
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)


#endregion

# #region function base views
#
# @api_view(['GET', 'POST'])
# def note(request: Request):
#     if request.method == 'GET':
#         todos = Todo.objects.order_by('priority').all()
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return  Response(serializer.data, status.HTTP_201_CREATED)
#     return Response(None, status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def note_detail_view(request: Request, todo_id:int):
#     try:
#         todo = Todo.objects.get(pk=todo_id)
#     except Todo.DoesNotExist:
#         return Response(None, status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     elif request.method == 'PUT':
#         serializer = TodoSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#         return Response(None, status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         todo.delete()
#         return Response(None, status.HTTP_204_NO_CONTENT)
#
# #endregion
#
# #region generics
#
# class NoteList(generics.ListCreateAPIView):
#     pagination_class = NotePagination
#     queryset = Todo.objects.order_by('priority').all()
#     serializer_class = TodoSerializer
#
# class EditeNote(generics.RetrieveUpdateDestroyAPIView):
#     pagination_class = NotePagination
#     queryset = Todo.objects.order_by('priority').all()
#     serializer_class = TodoSerializer
#
# #endregion
#
# #region viewsets
#
# class Note(viewsets.ModelViewSet):
#     pagination_class = NotePagination
#     queryset = Todo.objects.order_by('priority').all()
#     serializer_class = TodoSerializer
#
# #endregion
