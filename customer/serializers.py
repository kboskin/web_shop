from django.contrib.auth.models import User
from rest_framework import serializers

from customer.models import Profile, VisitLog


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'name', 'email', 'address']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class VisitLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitLog
        fields = ['id', 'user', 'activity_type', 'activity_date']
