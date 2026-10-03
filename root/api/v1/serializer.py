from rest_framework import serializers


class InfoSerialize(serializers.Serializer):
      
    name = serializers.CharField()
    family = serializers.CharField()
    