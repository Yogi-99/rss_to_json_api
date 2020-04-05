from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api import serializers
from api import rss_to_json


# Create your views here.
class RestAPIView(APIView):
    serializer_class = serializers.RestSerializer

    def get(self, request, format=None):
        result = [1, 2, 3, 4, 5, 6]
        return Response({
            'status': 'OK',
            'result': result,
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data.get('url')
            parsed_url = rss_to_json.parse(url)
            json_data = rss_to_json.get_books(parsed_url)

            return Response({'message': 'OK', 'result': json_data})
