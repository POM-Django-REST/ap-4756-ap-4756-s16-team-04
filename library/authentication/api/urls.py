from django.urls import path
from rest_framework import routers

user_router = routers.SimpleRouter()

# user_router.register('', <NameView>.as_view(), basename='user_router')

# urlpatterns = [
#     path('<int:user_id>', ),
#     path('<int:user_id>/order/<int:order_id>', )
# ]
