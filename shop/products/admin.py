from django.contrib import admin
from .models import Product, Category, Hashtag, Review

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Hashtag)
admin.site.register(Review)