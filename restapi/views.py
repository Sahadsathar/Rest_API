

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest.serializers import StudentSerializer
from rest.models import Student

class TestView(APIView):
    def get(self, requests, *args, **kw):
        data= {
            "username":'admin',
            'no. of years': 10,
        }
        return Response(data)

    def post(self, requests, *args, **kw):
        serializer = StudentSerializer(data = requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)