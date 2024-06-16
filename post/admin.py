from django.contrib import admin

from post.models import Post

# Register your models here.
from .import models
# Register your models here.
admin.site.register(models.Post)