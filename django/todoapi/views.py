from django.shortcuts import render
from .models import activities
from .serializers import activitiesSerializer

from rest_framework import generics


class ActivitiesList(generics.ListAPIView):
    queryset = activities.objects.all()
    serializer_class = activitiesSerializer