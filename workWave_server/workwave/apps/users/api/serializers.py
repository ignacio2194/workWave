from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from workwave.apps.users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True, required=False)
    password2 = serializers.CharField(write_only=True, required=False)
    avatar_url = serializers.ReadOnlyField(required=False)
    banner_url = serializers.ReadOnlyField(required=False)

    class Meta:
        model = CustomUser
        fields = ("id", "email", "password", "password2", "first_name", "last_name", "phone_number", "country", "headline", "about", "avatar_url", "banner_url")

    def create(self, validated_data):
        """
        Create and return a 'CustomUser' instance, given the validated data.
        """
        if validated_data["password"] != validated_data["password2"]:
            raise serializers.ValidationError("Passwords do not match.")
        validate_password(validated_data["password"])
        validated_data.pop("password2")
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Update and return an existing 'CustomUser' instance, given the validated data.
        """
        instance.name = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.country = validated_data.get('country', instance.country)
        instance.headline = validated_data.get('headline', instance.headline)
        instance.about = validated_data.get('about', instance.about)
        instance.save()
        return instance
        

class CustomUserImageSerializer(serializers.ModelSerializer):
    avatar_url = serializers.ReadOnlyField()
    banner_url = serializers.ReadOnlyField()

    class Meta:
        model = CustomUser
        fields = ("avatar_url", "avatar", "banner_url", "banner")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop("avatar")
        representation.pop("banner")
        return representation
    
class CustomUserPasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True)
    new_password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ("new_password", "new_password2")

    def update(self, instance, validated_data):
        """
        Update and return a new password for user, given the validated data.
        """
        if validated_data["new_password"] != validated_data["new_password2"]:
            raise serializers.ValidationError("Passwords do not match.")
        validate_password(validated_data["new_password"])
        validated_data.pop("new_password2")
        instance.set_password(validated_data["new_password"])
        instance.save()
        return instance
