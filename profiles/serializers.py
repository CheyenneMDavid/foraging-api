from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model, serializes Profile instances to and from
    JSON format.
    """

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        """
        Specifies the model and fields that will be serialized
        """

        model = Profile
        fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
            "name",
            "content",
            "image",
        ]
