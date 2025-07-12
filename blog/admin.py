from django.contrib import admin
from blog.models import Post, Postlike, PostComment

# Register your models here.
admin.site.register([Post,Postlike,PostComment])