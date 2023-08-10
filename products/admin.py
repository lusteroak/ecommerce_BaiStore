from django.contrib import admin
from .models import Category, SubCategory,Product, ProductHeroImages

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",),}

class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_sub_category": ("sub_category",),}

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(ProductHeroImages)
admin.site.register(Product, ProductAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Category, CategoryAdmin)