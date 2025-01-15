from django.urls import path, include
from . import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('', views.Note)

urlpatterns = [
    # path('funcnote/', views.note),
    # path('funcnote/<int:todo_id>', views.note_detail_view),
    path('', views.NoteList.as_view()),
    path('<int:todo_id>', views.NoteEditeList.as_view()),
    # path('genericnote/', views.NoteList.as_view()),
    # path('genericnote/<pk>', views.EditeNote.as_view()),
    # path('viewnote/', include(router.urls)),
]