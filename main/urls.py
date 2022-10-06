from django.urls import path
from .views import *

urlpatterns = [
    path('', Group),
    path('chat/<str:group>/<str:username>/', Chat),
    path('direct/<str:group>/<str:username>/', Direct)
]