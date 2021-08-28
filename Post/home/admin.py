from django.contrib import admin
from home.models import post,intresting_url,unintresting_url
# Register your models here.
@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','company','address','validthrough','datePosted']

@admin.register(intresting_url)
class InterstingAdmin(admin.ModelAdmin):
    list_display = ['id','url']


@admin.register(unintresting_url)
class UnInterstingAdmin(admin.ModelAdmin):
    list_display = ['id','url']
