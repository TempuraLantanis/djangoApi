from django.shortcuts import render

from rest_framework import viewsets
from .serializers import UserSerializer
from .models import user

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all().order_by('name')
    serializer_class = UserSerializer