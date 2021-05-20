from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models import NewUser
from .serializers import UserSerializer


class UserRecordView(APIView):
    def get(self, request, control):
        user = NewUser.objects.filter(control=control)
        serializer = UserSerializer(user, many=True)

        return Response(serializer.data)



