from django.shortcuts import render 
from .models import *
from rest_framework import generics, permissions, status
from .serializers import *
from django.http import HttpResponse 
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


@api_view(['POST'])
def deactivate_subscriber(request):
    try:
        serializer = GetSubscriberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        obj = Subscriber.objects.get(email=email)
        if obj.subscription_status == "active":
            obj.subscription_status = "inactive"
            obj.save()
            return Response("user deactivated",status=status.HTTP_200_OK)
        else:
            return Response("user already inactive",status=status.HTTP_200_OK)
    except Exception as e :
        return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])       
def add_subscriber(request):
    try:
        serializer = AddSubscriberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        first_name = serializer.validated_data['first_name']
        Subscriber.objects.create(email=email,first_name=first_name)
        return Response("subscriber created",status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        