from oscar.apps.promotions.views import HomeView as CoreHomeView
from oscar.apps.catalogue.models import ProductCategory, Category
class HomeView(CoreHomeView):
    template_name = "home.html"
    

    """
    superclassing get_context_data to retrieve the context from django-oscar's promotions.views.homeview and add more
    """
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        meatproductcategory = ProductCategory.objects.filter(category__name__iexact="meat")
        context['all_products_categories'] = (meatproductcategory,)
        context['customfooter'] = True
        context['customnavaccount'] = True
        context['user_less'] = False
        return context 