from rest_framework import serializers
from .models import Board

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = '__all__'

def creat(self, validated_data):
    return Board.objects.create(*validated_data)