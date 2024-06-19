from django.contrib import admin

from catagory.models import Catagory
# Register your models here.


class adminclass(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['slug','name']


admin.site.register(Catagory,adminclass)