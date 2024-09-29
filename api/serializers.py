from rest_framework import serializers
from dealership.models import WellcomeHerro, Vehicles, Services, ClientsReviews, Partner, TopBrands


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WellcomeHerro
        fields = ['id', 'title', 'sub_title', 'background_img']


class VehiclesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicles  # Correct the spelling here
        fields = ['id', 'year', 'body', 'manufactor', 'condition', 'model', 'price',
                  'kilometers', 'horse_power', 'transmission', 'short_description',
                  'long_description', 'img']


class ServicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Services
        fields = ['id', 'icon', 'title', 'sub_title']


class ClientsReviewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClientsReviews
        fields = ['id', 'user_email', 'full_name', 'message', 'location']


class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'partner_logo']


class TopBrandsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TopBrands
        fields = ['id', 'name']
