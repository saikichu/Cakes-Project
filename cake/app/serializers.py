from rest_framework import serializers

from .models import Cake,Category,Shape,Weight


class CategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Category

        fields = '__all__'

class ShapeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Shape

        fields = '__all__'

class WeightSerializer(serializers.ModelSerializer):

    class Meta:

        model = Weight

        fields = '__all__'

class CakeSerializer(serializers.ModelSerializer):

    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    shape = serializers.PrimaryKeyRelatedField(queryset=Shape.objects.all())
    weight = serializers.PrimaryKeyRelatedField(queryset=Weight.objects.all())

    class Meta:

        model = Cake

        fields = '__all__'
