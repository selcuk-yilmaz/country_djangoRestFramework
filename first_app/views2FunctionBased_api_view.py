from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Country
from .serializers import CountrySerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response



@api_view(["GET","POST"])
def country_list(request):
    if request.method == "GET":
        obj = Country.objects.all()
        serializer = CountrySerializer (obj,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        # data = JSONParser().parse(request)api_view
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def country_detail(request,pk):
    try:
        country = Country.objects.get(pk=pk)
    except Country.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        serializer = CountrySerializer(country)
        return Response(serializer.data)
    elif request.method == "PUT":
        # data = JSONParser().parse(request)
        serializer = CountrySerializer(country,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        country.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)