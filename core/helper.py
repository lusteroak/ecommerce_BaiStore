from typing import Any, Dict
from django.views.generic.base import ContextMixin

from products.models import Category, SubCategory,Product, ProductHeroImages

class CategorySubcategoryHelperMixin(ContextMixin):
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['product_categories'] = Category.objects.filter().order_by('name')
        context['product_sub_categories'] = SubCategory.objects.filter().order_by('sub_category')
        return context
    
class ProductHeroImagesHelperMixin(ContextMixin):
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['product_hero_images'] = ProductHeroImages.objects.all()
        return context