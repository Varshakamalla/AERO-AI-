from django.urls import path
from .views import ask_question, home

urlpatterns = [
    path('', home),         # root path
    path('ask/', ask_question),
]
