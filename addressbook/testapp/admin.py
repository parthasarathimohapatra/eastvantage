from django.contrib import admin
from .models import *
# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display=['id','latitude','longitude','is_deleted']
admin.site.register(Address,AddressAdmin)
