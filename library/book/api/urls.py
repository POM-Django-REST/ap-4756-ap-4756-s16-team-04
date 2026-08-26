from django.urls import path
from rest_framework import routers

book_router = routers.SimpleRouter()

# book_router.register('', <NameView>.as_view(), basename='book_router')

# urlpatterns = [
#     path('<int:book_id>', )
# ]