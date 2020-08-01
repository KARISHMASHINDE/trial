from django.contrib import admin
from django.db import models
from .models import Posts,Tag

# Register your models here.
admin.site.register(Posts)
admin.site.register(Tag)