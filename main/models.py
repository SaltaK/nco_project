from django.contrib.auth.models import User
from django.db import models


def upload_to(instance, filename):
    return f'{filename}'


class News(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateTimeField(auto_now=True)
    short_description = models.CharField(max_length=1000)
    full_description = models.TextField()
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.title


class FavouriteNews(models.Model):
    favourite_news = models.ForeignKey(News, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class ImageNews(models.Model):
    image = models.ImageField(upload_to=upload_to)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.news.title


PUBLICATION_TYPES = (
    (1, 'Публикации NCO'),
    (2, 'Другие публикации')
)


class Publication(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    file = models.FileField(null=True, blank=True)
    favourite_publication = models.IntegerField(choices=PUBLICATION_TYPES, default=1)


class FavouritePublication(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


LAW_TYPES = (
    (1, 'Действующее законадестльство'),
    (2, 'Проекты'),
    (3, 'Международные документы')
)


class Law(models.Model):
    type = models.IntegerField(choices=LAW_TYPES, default=1)
    title = models.CharField(max_length=180)
    text = models.TextField()


class FavouriteLaws(models.Model):
    name = models.CharField(max_length=100)
    laws = models.ForeignKey(Law, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

