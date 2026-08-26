from django.urls import path
from .views import AuthorListApiView

urlpatterns = [
    path('authors/', AuthorListApiView.as_view()),
    path('authors/<int:id>/', AuthorListApiView.as_view()),
]