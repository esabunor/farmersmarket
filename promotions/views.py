from oscar.apps.promotions.views import HomeView as CoreHomeView
from oscar.apps.catalogue.models import ProductCategory
class HomeView(CoreHomeView):
    template_name = "home.html"
    

    """
    superclassing get_context_data to retrieve the context from django-oscar's promotions.views.homeview and add more
    """
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        fish = ProductCategory.objects.filter(category__name__iexact='fish')
        seafood = ProductCategory.objects.filter(category__name__iexact='seafood')
        poultry = ProductCategory.objects.filter(category__name__iexact='poultry')
        meat = ProductCategory.objects.filter(category__name__iexact='meat')
        context['products_categories'] = [fish, seafood, poultry, meat]
        return context 