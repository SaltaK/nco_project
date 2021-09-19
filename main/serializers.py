from rest_framework import serializers
from main.models import *


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = 'id title publication_date image short_description'.split()


class ImageNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageNews
        fields = 'id image'.split()


class NewsItemSerializer(serializers.ModelSerializer):
    images = ImageNewsSerializer(many=True)

    class Meta:
        model = News
        fields = 'id title link full_description images'.split()


class FavouriteLawSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteLaws
        fields = 'id name'.split()


class LawsByTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = 'id title text'.split()


class LawItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = 'id title text law_type'.split()


class PublicationByTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = 'id title text file'.split()


class PublicationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = 'id title text file types'.split()