from .models import InputData
from rest_framework import serializers


class UserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputData
        fields = ['input_values', 'user_id', 'input_time']
