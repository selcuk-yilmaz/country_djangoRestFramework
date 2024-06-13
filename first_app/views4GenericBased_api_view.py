from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Country
from .serializers import CountrySerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

#BELOW GENERİC APİ VİEWS
class GenericApiView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
    mixins.UpdateModelMixin, mixins.DestroyModelMixin,
):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated, HasAInUsername]

    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    lookup_field = "pk"

    def get(self, request, pk=None):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)
#BELOW CLASS BASED APİ VİEWS    
class CountryView(APIView):
    def get(self, request):
        obj = Country.objects.all()
        serializer = CountrySerializer(obj, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = CountrySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


class CountryDetailView(APIView):
    def get_object(self, pk):
        try:
            country = Country.objects.get(pk=pk)
            return country
        except Country.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        country = self.get_object(pk)
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    def put(self, request, pk):
        country = self.get_object(pk)
        serializer = CountrySerializer(country, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        country = self.get_object(pk)

        country.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


#BELOW FUNCTİON BASED APİ VİEWS
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