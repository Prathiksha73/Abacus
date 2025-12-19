from django.urls import path
from .views import TestProtectedAPI

urlpatterns = [
    path("test/", TestProtectedAPI.as_view()),
]
