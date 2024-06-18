from rest_framework import status
from rest_framework.response import Response
from .models import Profile, Member
from .serializers import ProfileSerializer, MemberSerializer
from rest_framework.views import APIView


# Create your views here.
#BELOW CLASS BASED APİ VİEWS    
class ProfileView(APIView):
    def get(self, request):
        obj = Profile.objects.all()
        serializer = ProfileSerializer(obj, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class MemberView(APIView):
    def get(self, request):
        obj = Member.objects.all()
        serializer = MemberSerializer(obj, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = MemberSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)