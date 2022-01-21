from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('book/<int:book_id>', views.get_book_by_id, name = "get_book_by_id")
]