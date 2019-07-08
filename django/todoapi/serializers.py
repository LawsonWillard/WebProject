from rest_framework import serializers
from .models import activities

class activitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = activities
        fields = ('name', 'description', 'tag')