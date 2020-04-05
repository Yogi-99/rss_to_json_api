from rest_framework import serializers


class RestSerializer(serializers.Serializer):
    url = serializers.CharField()
