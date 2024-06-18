from rest_framework import serializers
from .models import Profile, Member


from datetime import datetime
from datetime import date
from django.utils.timesince import timesince



class ProfileSerializer(serializers.ModelSerializer):

    # time_since_pub = serializers.SerializerMethodField()
    # yazar = serializers.StringRelatedField()

    class Meta:
        model = Profile
        fields = '__all__'
        # fields = ['yazar', 'baslik', 'metin']
        # exclude = ['yazar', 'baslik', 'metin']
        # read_only_fields = ['id', 'yaratilma_tarihi', 'güncelleneme_tarihi']

    # def get_time_since_pub(self,object):
    #     now = datetime.now()
    #     pub_date = object.yayımlanma_tarihi
    #     if object.aktif == True:
    #         time_delta = timesince(pub_date, now)
    #         return time_delta
    #     else:
    #         return 'Aktif Degil!'

    # def validate_yayımlanma_tarihi(self, tarihdegeri):
    #     today = date.today()
    #     if tarihdegeri > today:
    #         raise serializers.ValidationError('Yayımlanma tarihi ileri bir tarih olamaz!')
    #     return tarihdegeri



class MemberSerializer(serializers.ModelSerializer):

    # makaleler = MakaleSerializer(many=True, read_only=True)
    # makaleler = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='makale-detay',
    # )

    class Meta:
        model = Member
        fields = '__all__'