from django.urls import path
from .views import BookListApiView

urlpatterns = [
    path('books/', BookListApiView.as_view()),
    path('books/<int:id>/', BookListApiView.as_view()),
]