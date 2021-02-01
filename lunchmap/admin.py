from django.contrib import admin

# Register your models here.
from .models import Category, Shop

# 管理サイトにモデルを登録
admin.site.register(Category)
admin.site.register(Shop)