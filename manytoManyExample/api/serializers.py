from rest_framework import serializers
from manytoManyExample.models import Customer, Product, Order
from datetime import datetime
from datetime import date
from django.utils.timesince import timesince

class ProductsSerializer(serializers.ModelSerializer):

    # time_since_pub = serializers.SerializerMethodField()
    # yazar = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['yazar', 'baslik', 'metin']
        # exclude = ['yazar', 'baslik', 'metin']
        # read_only_fields = ['id', 'yaratilma_tarihi', 'güncelleneme_tarihi']


class CustomerSerializer(serializers.ModelSerializer):

    # makaleler = MakaleSerializer(many=True, read_only=True)
    # makaleler = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='makale-detay',
    # )

    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    # makaleler = MakaleSerializer(many=True, read_only=True)
    # makaleler = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='makale-detay',
    # )

    class Meta:
        model = Order
        fields = '__all__'

