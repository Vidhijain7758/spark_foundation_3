from rest_framework import serializers
from django.db import models
from accounts.models import Country
from rest_framework import exceptions
from django.contrib.auth import authenticate,login

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields  = ('id','Country_name','Country_code')



