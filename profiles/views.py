from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(APIView):
    """
    Handles GET requests to list all user profiles. Profiles are listed only
    if the user has appropriate permissions.
    """

    def get(self, request):
        """
        Retrieves and serializes all profiles.
        Returns an object containing serialized profiles and HTTP 200 OK
        status.
        """
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileDetail(APIView):
    """
    Handles GET and PUT requests for a single user profile. Access is
    restricted to authorized users.
    """

    serializer_class = ProfileSerializer

    def get_object(self, pk):
        """
        Fetches a single profile by primary key (pk) or raises Http404 if not
        found.
        """
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieves and serializes a specific profile.
        Returns an object with the serialized profile data.
        """
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Updates a specific profile, validated against data from the request.
        Returns an object with updated profile data or error messages.
        """
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
