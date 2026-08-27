from rest_framework import serializers
from book.models import Book

class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'count', 'authors']