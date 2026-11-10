from rest_framework import serializers

from .models import profile

class ProfileSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, trim_whitespace=False)

    class Meta:

        model = profile

        fields = ['username', 'first_name','email','password','role']
        extra_kwargs = {
            'email': {'required': False},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = profile(**validated_data)
        user.set_password(password)
        user.save()
        return user
