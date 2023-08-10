from typing import Any, Dict
from django.views.generic.base import ContextMixin

from products.models import Product, ProductHeroImages

class CategorySubcategoryHelperMixin(ContextMixin):
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['product_categories'] = Product.objects.all()
        return context
    
class ProductHeroImagesHelperMixin(ContextMixin):
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['product_hero_images'] = ProductHeroImages.objects.all()
        return context