from django.contrib import admin
from .models import *


class CenterImagesInline(admin.TabularInline):
    model = CenterImages


@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    inlines = [CenterImagesInline,]


class ShopImagesInline(admin.TabularInline):
    model = ShopImages


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    inlines = [ShopImagesInline,]


class NewImagesInline(admin.TabularInline):
    model = NewImages


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    inlines = [NewImagesInline,]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
# Register your models here.
