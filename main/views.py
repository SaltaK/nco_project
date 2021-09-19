from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class NewsListApiView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    pagination_class = PageNumberPagination


class NewsItemApiView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsItemSerializer


class FavouriteNewsApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        news_id = request.data.get('news_id')
        try:
            favourite = FavouriteNews.objects.get(news_id=news_id, user=request.user)
            print('GET')
        except:
            favourite = FavouriteNews.objects.create(news_id=news_id, user=request.user)
            print('CREATE')
        favourite.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request):
        news_id = request.data.get('news_id')
        favourite = FavouriteNews.objects.filter(news_id=news_id, user=request.user)
        favourite.delete()
        return Response(status=status.HTTP_200_OK)


class FavouriteLawsApiView(APIView):
    def get(self, request):
        types = FavouriteLaws.objects.all()
        data = FavouriteLawSerializer(types, many=True).data
        return Response(data=data)


class LawsTypeApiView(APIView):
    def get(self, request):
        search = request.query_params.get('type_id', '')
        laws = Law.objects.filter(law_type=search)
        data = LawsByTypeSerializer(laws, many=True).data
        return Response(data=data)


class LawsItemApiView(APIView):
    def get(self, request, id):
        law = Law.objects.get(pk=id)
        data = LawItemSerializer(law).data
        return Response(data=data)


class PublicationsTypeApiView(APIView):
    def get(self, request):
        search = request.query_params.get('type_id', '')
        publications = Publication.objects.filter(types=search)
        data = PublicationByTypeSerializer(publications, many=True).data
        return Response(data=data)


class PublicationItemApiView(APIView):
    def get(self, request, id):
        publication = Publication.objects.get(pk=id)
        data = PublicationItemSerializer(publication).data
        return Response(data=data)
