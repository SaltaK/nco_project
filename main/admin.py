from django.contrib import admin
from .models import *


admin.site.register(News)
admin.site.register(ImageNews)
admin.site.register(Law)
admin.site.register(Publication)
admin.site.register(FavouriteNews)
admin.site.register(FavouriteLaws)
admin.site.register(FavouritePublication)