from rest_framework import serializers
from author.models import Author
from book.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta():
        model = Book
        fields = ['id', 'name', 'description', 'count']


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    class Meta():
        model = Author
        fields = ['id', 'name', 'surname', 'patronymic', 'books']