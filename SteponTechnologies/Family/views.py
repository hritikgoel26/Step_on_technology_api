from django.shortcuts import render
from .serializers import ParentsSerializer,ChildSerializer
from rest_framework import viewsets
from .models import Parents,Child

# Create your views here.
class ParentsViewSet(viewsets.ModelViewSet):
    queryset=Parents.objects.all()
    serializer_class=ParentsSerializer


class ChildViewSet(viewsets.ModelViewSet):
    queryset=Child.objects.all()
    serializer_class=ChildSerializer