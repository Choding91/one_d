from rest_framework import serializers
from users.models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
        )
        user.set_password(validated_data["password"])
        user.is_active = True
        user.save()
        return user

    def update(self, validated_data):
        user = User(
            username=validated_data["username"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Profile
        fields = "__all__"


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)
