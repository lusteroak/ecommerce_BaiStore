from django.views.generic import TemplateView

from .helper import CategorySubcategoryHelperMixin, ProductHeroImagesHelperMixin

class Home(TemplateView, CategorySubcategoryHelperMixin, ProductHeroImagesHelperMixin):
    template_name = "core/homepage.html"